from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text



def text_to_chunk(text ,chunk_size=500,overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


model = SentenceTransformer('all-MiniLM-L6-v2')  # Light and fast

def get_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings


# Extract text
result = extract_text("shreenath.pdf")
print(result) 

# Convert to chunk
chunk = text_to_chunk(result)
print(len(chunk))

#chunks to vector
vector = get_embeddings(chunks=chunk)
print(vector)