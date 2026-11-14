"""Real local sentence-transformers embeddings; errors propagate."""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer


class MyEmbedder:
    def __init__(self, model_name, revision=None):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name, revision=revision, cache_folder=str(Path(__file__).resolve().parents[2] / 'local_models'))
        self.dimensions = self.model.get_sentence_embedding_dimension()

    def embed_documents(self, texts):
        vectors = self.model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
        if not np.isfinite(vectors).all():
            raise ValueError("Non-finite embeddings")
        return vectors.tolist()

    def embed_query(self, question):
        return self.embed_documents([question])[0]
