# ------------------------ Imports ------------------------ #

import redis
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------- Variables ----------------------- #

model = SentenceTransformer('all-MiniLM-L6-v2')
redis_base = redis.Redis(host='localhost', port=6379, db=0)

# ----------------------- Functions ----------------------- #

def get_embedding(text):
    for chunk in tqdm(text):
        embedding = model.encode(chunk)
    return embedding

def store_embeddings(embeddings, r):
    """
    Store embeddings in Redis.

    Args:
        embeddings (list): List of embeddings.
        r (Redis): Redis client object.

    Returns:
        None
    """
    for i, embedding in enumerate(embeddings):
        embedding_list = embedding.tolist()
        r.hset('doc_embeddings', f'doc_{i}', embedding_list)

def similarity_search(query, r):
    """
    Search for the most similar document to the given query.

    Args:
        query (str): The query string.
        r (Redis): Redis client object.

    Returns:
        int: The index of the most similar document.
    """
    query_embedding = get_embedding(query)
    query_embedding = np.array(query_embedding).reshape(1, -1)
    doc_embeddings = r.hgetall('doc_embeddings')
    doc_embeddings = [np.array(eval(v)) for v in doc_embeddings.values()]
    doc_embeddings = np.array(doc_embeddings)

    # Perform cosine similarity search in RedisAI
    r.execute_command('AI.TENSORSET', 'query_embedding', 'FLOAT', '1', '768', *query_embedding.flatten())
    r.execute_command('AI.TENSORSET', 'doc_embeddings', 'FLOAT', str(doc_embeddings.shape[0]), '768', *doc_embeddings.flatten())
    r.execute_command('AI.SIMILARITY', 'query_embedding', 'doc_embeddings', 'SIMILARITY', 'COSINE', 'WITHLABELS')

    # Get the index of the most similar document
    result = r.execute_command('AI.TENSORGET', 'SIMILARITY', 'VALUES')
    similarities = np.array(result[1:]).astype(float)
    return np.argmax(similarities)


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