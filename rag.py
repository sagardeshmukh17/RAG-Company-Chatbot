import os
from unittest import result

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

from ingest import response

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

def ask_question(question):
    # create embedding for the question
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question,
    )
    question_embedding = response.data[0].embedding

    # with question embedding search chromadb
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )
    print("Results: ", results)

    documents = results["documents"][0]
    print("Documents: ", documents)

    # combine list objects into context
    context = "\n\n".join(documents)
    print (context)

    # create RAG prompt (Augmentation)
    prompt = f"""
    
    Answer the only question using the context below:
    
    Context: {context}
    
    Question: {question}

    """

    response = client.responses.create(
        model = "gpt-6-astra",
        input = prompt,
    )

    return response.output_text

