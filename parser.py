import pdfplumber

print("Parsing resumes...")

with pdfplumber.open("data/sample.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

print(text)