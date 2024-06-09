from transformers import pipeline
import chromadb
from chromadb.config import Settings

def query_chroma(question):
    client = chromadb.Client(Settings(chroma_url="http://localhost:8000"))
    stored_document = client.get({"metadata.source": "path_to_your_pdf.pdf"})  # Adjust query as needed
    context = stored_document[0]["text"]
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=question, context=context)
    return result['answer']

if __name__ == "__main__":
    question = "What is the main topic of the document?"  # Replace with your question
    answer = query_chroma(question)
    print(f"Answer: {answer}")

