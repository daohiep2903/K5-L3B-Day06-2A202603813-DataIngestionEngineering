"""Persistent Qdrant local store with exact cosine search."""
import math
import uuid
from pathlib import Path
from qdrant_client import QdrantClient, models


class LocalVectorStore:
    def __init__(self, path, dimensions):
        self.client = QdrantClient(path=str(Path(path)))
        self.dimensions = dimensions

    def _validate(self, vector):
        if len(vector) != self.dimensions or not all(math.isfinite(v) for v in vector) or not any(vector):
            raise ValueError('Invalid embedding vector')

    def create_schema(self):
        for strategy in ('A', 'B', 'C'):
            name = f'day6_{strategy}'
            if not self.client.collection_exists(name):
                self.client.create_collection(name, vectors_config=models.VectorParams(size=self.dimensions, distance=models.Distance.COSINE))
            config = self.client.get_collection(name).config.params.vectors
            if config.size != self.dimensions or config.distance != models.Distance.COSINE:
                raise ValueError('Stored vector configuration differs from selected model')

    def upsert(self, strategy, chunks, vectors):
        if strategy not in ('A', 'B', 'C') or not chunks or len(chunks) != len(vectors):
            raise ValueError('Invalid strategy or chunks/vectors')
        points = []
        for chunk, vector in zip(chunks, vectors):
            self._validate(vector)
            payload = dict(chunk.metadata, chunk_id=chunk.chunk_id, document_id=chunk.document_id, source=chunk.source, page=chunk.page, text=chunk.text)
            points.append(models.PointStruct(id=str(uuid.uuid5(uuid.NAMESPACE_URL, chunk.chunk_id)), vector=vector, payload=payload))
        name = f'day6_{strategy}'
        # Remove stale IDs after writing current snapshot; dedicated lab collections only.
        for start in range(0, len(points), 64):
            self.client.upsert(name, points=points[start:start+64], wait=True)
        keep = {point.id for point in points}
        old, offset = self.client.scroll(name, limit=256, with_payload=False, with_vectors=False)
        existing = list(old)
        while offset is not None:
            old, offset = self.client.scroll(name, offset=offset, limit=256, with_payload=False, with_vectors=False)
            existing.extend(old)
        stale = [point.id for point in existing if str(point.id) not in keep]
        if stale:
            self.client.delete(name, points_selector=models.PointIdsList(points=stale), wait=True)

    def count(self, strategy):
        return self.client.count(f'day6_{strategy}', exact=True).count

    def search(self, strategy, query_vector, top_k=3, filters=None):
        self._validate(query_vector)
        filters = filters or {}
        if set(filters) - {'top_level_section', 'language'}:
            raise ValueError('Unsupported metadata filter')
        query_filter = models.Filter(must=[models.FieldCondition(key=key, match=models.MatchValue(value=value)) for key, value in filters.items()]) if filters else None
        points = self.client.query_points(f'day6_{strategy}', query=query_vector, query_filter=query_filter, limit=top_k,
                                          with_payload=True).points
        return [dict(chunk_id=p.payload['chunk_id'], document_id=p.payload['document_id'], source=p.payload['source'], page=p.payload['page'],
                     text=p.payload['text'], score=p.score, metadata={k: v for k, v in p.payload.items() if k not in {'chunk_id', 'document_id', 'source', 'page', 'text'}}) for p in points]

    def close(self):
        self.client.close()
