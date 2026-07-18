from sentence_transformers import SentenceTransformer


class EmbeddingProvider:

    _model = None


    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = SentenceTransformer(
                "BAAI/bge-small-zh-v1.5"
            )

        return cls._model


    @classmethod
    def embed(cls, text: str):

        return cls.get_model().encode(text, normalize_embeddings=True)