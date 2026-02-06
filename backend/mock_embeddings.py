'''import numpy as np

class FakeEmbeddings:
    """Mocks the OpenAI Embeddings API for local dev."""
    
    def embed_documents(self, texts):
        # Return a random vector for each text chunk
        return [np.random.rand(1536).tolist() for _ in texts]

    def embed_query(self, text):
        # Return a single random vector for a query
        return np.random.rand(1536).tolist()
'''

import numpy as np

class FakeEmbeddings:
    """Mocks the OpenAI Embeddings API for local dev."""

    def embed_documents(self, texts):
        # Return a random vector for each text chunk
        return [np.random.rand(1536).tolist() for _ in texts]

    def embed_query(self, text):
        # Return a single random vector for a query
        return np.random.rand(1536).tolist()

    def __call__(self, text):
        """
        Make the object callable. FAISS expects embeddings to be callable.
        If `text` is a list, call embed_documents; if str, call embed_query.
        """
        if isinstance(text, list):
            return self.embed_documents(text)
        return self.embed_query(text)
