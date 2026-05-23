import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

# Load Dataset
df = pd.read_csv("data/incidents_dataset.csv")

# Load Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB
client = chromadb.PersistentClient(path="vectordb")

collection = client.get_or_create_collection("incidents")

# Store embeddings
for index, row in df.iterrows():

    incident = str(row["body"])
    solution = str(row["answer"])

    embedding = model.encode(incident).tolist()

    collection.add(
        ids=[str(index)],
        embeddings=[embedding],
        documents=[incident],
        metadatas=[{
            "solution": solution
        }]
    )

print("Dataset successfully ingested into ChromaDB")