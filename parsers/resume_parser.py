import fitz

def parse_resume(resume_file):
    # Read the uploaded file
    doc = fitz.open(stream=resume_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
