# ------------------------ Imports ------------------------ #

import numpy
import langchain
from tqdm import tqdm

# ----------------------- Variables ----------------------- #

chunk_size = 100
model = 'gte-large'

# ----------------------- Functions ----------------------- #

def split_document(text, chunk_size):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def get_embedding(chunk, model):
    return 

def store_in_redis(chunk, embedding, source):
    return

def process_document(text, chunk_size, model, source):
    return
