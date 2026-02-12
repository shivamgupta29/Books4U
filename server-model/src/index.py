from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    print(model.encode(text).tolist())  


get_embedding("The way of life is the way.")