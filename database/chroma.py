from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import chromadb
import uuid
import time

embedding_fn = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# client = chromadb.Client() for im memory storage
client = chromadb.PersistentClient(path="./chroma_store") # for persistent storage
client.list_collections()


collection = client.get_or_create_collection(
    name="agent_knowledge",
    embedding_function=embedding_fn
)

def get_from_chroma(query: str) -> str | None:
    results = collection.query(
        query_texts=[query],
        n_results=1
    )
    if results["documents"] and results["documents"][0]:
        if results["distances"][0][0] < 1.0:
            return results["documents"][0][0]
        
    return None

def add_to_chroma(query: str, result: str) -> None:
    collection.add(
        ids=[str(uuid.uuid4())],
        documents=[result],
        metadatas=[
            {
                "source": "web",
                "query": query,
                "timestamp": time.time()
            }
        ],
        embeddings=None
    )