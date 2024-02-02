# ------------------------ Imports ------------------------ #

import redis
from redis.commands.search.field import TagField, TextField, NumericField, VectorField
from redis.commands.search.query import Query
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------- Variables ----------------------- #

model = SentenceTransformer('all-MiniLM-L6-v2')
redis_base = redis.Redis(host='localhost', port=6379, db=0)
VECTOR_DIMENSION = 384


# Creating index in Redisearch
redis_base.ft().create_index(
    [
        VectorField(
            "embedding",
            "HNSW",
            {
                "TYPE": "FLOAT32",
                "DIM": VECTOR_DIMENSION,
                "DISTANCE_METRIC": "COSINE",
            },
            as_name="vector",
        ),
        TextField("text_chunk"),
    ],
)
# ----------------------- Functions ----------------------- #

def get_embedding(text_chunks):
    """
    Generate embeddings for all chunks of text.

    Args:
        text_chunks (list): List of text chunks.

    Returns:
        list: List of embeddings.
    """
    embeddings = []
    for chunk in tqdm(text_chunks):
        embedding = model.encode(chunk)
        embeddings.append(embedding)
    return embeddings

def store_embeddings(text_chunks, embeddings, r=redis_base):
    """
    Store embeddings in Redis using Redisearch.

    Args:
        text_chunks (list): List of text chunks.
        embeddings (list): List of embeddings.
        r (Redis): Redis client object.
    """
    for i, (chunk, embedding) in enumerate(zip(text_chunks, embeddings)):
        r.ft()

def similarity_search(query, r=redis_base):
    """
    Search for the most similar document to the given query using Redisearch vector similarity.

    Args:
        query (str): The query string.
        r (Redis): Redis client object.

    Returns:
        The ID of the most similar document.
    """
    query_embedding = model.encode(query).tolist()  # Convert query embedding to list
    response = r.ft("idx:doc_embeddings").search(
        f"(@embedding:[{query_embedding}])=>[KNN 1]", # This syntax might vary
        sort_by="embedding",
        sort_asc=False
    )
    if response.docs:
        return response.docs[0].id  # Return the ID of the most similar document
    else:
        return None


def chop_text(text, max_length=512):
    """
    Chop the text into chunks of max_length.

    Args:
        text (str): The input text.
        max_length (int, optional): The maximum length of each chunk. Defaults to 512.

    Returns:
        list: List of chunks.
    """
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]
