import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI

# ================= load env properties from .env
load_dotenv()

# ================ get the actual api key from .env file
api_key = os.getenv("OPENAI_API_KEY")

# =========== create openai client
client = OpenAI(api_key=api_key)

# ====== create chroma db client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# ===== create or get the collection
collection = chroma_client.get_or_create_collection(name="company_documents")

# ====== read file data
with open("documents/company.txt", "r", encoding="utf-8") as file:
    document = file.read()

    # === split document into multiple chunks
    chunks = document.split("\n\n")

    # === generate embeddings and store them
    for index, chunk in enumerate(chunks):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk,
        )
        embedding = response.data[0].embedding

        collection.add(
            ids=[f"chunk-{index}"],
            documents=[chunk],
            embeddings=[embedding]   # must be list
        )

        print(f"Chunk {index} stored successfully")
