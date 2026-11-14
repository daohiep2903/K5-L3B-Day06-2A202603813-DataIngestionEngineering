"""Persistent pgvector exact cosine search with parameterized metadata filters."""
import json
import math
import psycopg
from psycopg.types.json import Jsonb


class PgVectorStore:
    def __init__(self, database_url, dimensions):
        if not isinstance(dimensions, int) or not 1 <= dimensions <= 16000:
            raise ValueError("Invalid embedding dimensions")
        self.url, self.dimensions = database_url, dimensions

    def _vector(self, values):
        if len(values) != self.dimensions or not all(math.isfinite(v) for v in values) or not any(values):
            raise ValueError("Invalid embedding vector")
        return "[" + ",".join(str(float(v)) for v in values) + "]"

    def create_schema(self):
        with psycopg.connect(self.url) as conn:
            conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
            conn.execute(f"CREATE TABLE IF NOT EXISTS day6_chunks (strategy text, chunk_id text, document_id text NOT NULL, source text NOT NULL, page integer NOT NULL, content text NOT NULL, metadata jsonb NOT NULL, embedding vector({self.dimensions}) NOT NULL, PRIMARY KEY(strategy, chunk_id))")
            actual = conn.execute("SELECT format_type(atttypid, atttypmod) FROM pg_attribute WHERE attrelid='day6_chunks'::regclass AND attname='embedding'").fetchone()[0]
            if actual != f"vector({self.dimensions})":
                raise ValueError("Stored vector dimensions differ from selected model")

    def upsert(self, strategy, chunks, vectors):
        if len(chunks) != len(vectors) or not chunks:
            raise ValueError("Require equal nonempty chunks/vectors")
        rows = [(strategy, c.chunk_id, c.document_id, c.source, c.page, c.text, Jsonb(c.metadata), self._vector(v)) for c,v in zip(chunks,vectors)]
        # Atomic complete replacement for this dedicated experiment strategy removes stale chunks.
        with psycopg.connect(self.url) as conn:
            conn.execute("DELETE FROM day6_chunks WHERE strategy=%s", (strategy,))
            with conn.cursor() as cursor:
                cursor.executemany("INSERT INTO day6_chunks VALUES (%s,%s,%s,%s,%s,%s,%s,%s::vector)", rows)

    def count(self, strategy):
        with psycopg.connect(self.url) as conn:
            return conn.execute("SELECT count(*) FROM day6_chunks WHERE strategy=%s", (strategy,)).fetchone()[0]

    def search(self, strategy, query_vector, top_k=3, filters=None):
        if top_k < 1:
            raise ValueError("top_k must be positive")
        filters = filters or {}
        if set(filters) - {"top_level_section", "language"}:
            raise ValueError("Unsupported metadata filter")
        vector = self._vector(query_vector)
        with psycopg.connect(self.url) as conn:
            rows = conn.execute("SELECT chunk_id,document_id,source,page,content,metadata,1-(embedding <=> %s::vector) AS score FROM day6_chunks WHERE strategy=%s AND metadata @> %s ORDER BY embedding <=> %s::vector, chunk_id LIMIT %s", (vector,strategy,Jsonb(filters),vector,top_k)).fetchall()
        return [dict(zip(["chunk_id","document_id","source","page","text","metadata","score"], row)) for row in rows]
