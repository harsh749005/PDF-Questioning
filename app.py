from PyPDF2 import PdfReader

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

# Extract text
result = extract_text("shreenath.pdf")
print(result) 

# Convert to chunk
chunk = text_to_chunk(result)
print(len(chunk))
