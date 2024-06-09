import chromadb
from chromadb.config import Settings
import PyPDF2

def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    pdf_file.close()
    return text

def load_pdf_to_chroma(pdf_path):
    client = chromadb.Client(Settings(chroma_url="http://localhost:8000"))
    text = extract_text_from_pdf(pdf_path)
    document = {"text": text, "metadata": {"source": pdf_path}}
    client.store(document)

if __name__ == "__main__":
    pdf_path = "path_to_your_pdf.pdf"  # Replace with your PDF file path
    load_pdf_to_chroma(pdf_path)

