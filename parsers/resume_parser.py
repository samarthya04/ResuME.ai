import fitz  # PyMuPDF

def parse_resume(resume_file):
    # Read the uploaded file directly
    doc = fitz.open(stream=resume_file.read(), filetype="pdf")  # Specify the correct filetype
    text = ""
    for page in doc:
        text += page.get_text()
    return text
