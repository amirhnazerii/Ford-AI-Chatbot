import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Initialize the model for generating sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text_data):
    """
    Generate embeddings for a list of text data using SentenceTransformer.
    Args:
    - text_data: list of strings representing data entries.

    Returns:
    - numpy array of embeddings.
    """
    embeddings = model.encode(text_data)
    return np.array(embeddings)

def create_faiss_index(embeddings):
    """
    Create a FAISS index for fast similarity search.
    Args:
    - embeddings: numpy array of embeddings.

    Returns:
    - FAISS index object populated with the embeddings.
    """
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def query_table_data(query, index, table_data, k=10):
    """
    Retrieve the most relevant entries from table_data based on a query.
    Args:
    - query: string representing the user's query.
    - index: FAISS index object.
    - table_data: list of strings representing data entries.
    - k: int, number of top results to retrieve.

    Returns:
    - list of relevant data entries.
    """
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=k)
    relevant_rows = [table_data[idx] for idx in indices[0]]
    return relevant_rows
