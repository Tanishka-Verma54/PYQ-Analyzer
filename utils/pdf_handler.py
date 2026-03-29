from pypdf import PdfReader
import re

def extract_questions(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    # extract text from all pages
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # clean weird spacing
    text = text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)

    # split using question numbers (1. 2. 3. ...)
    raw_questions = re.split(r'(?=\d+\.\s)', text)

    questions = []

    for q in raw_questions:
        q = q.strip()

        # remove numbering like "1. "
        q = re.sub(r'^\d+\.\s*', '', q)

        # remove very small garbage text
        if len(q) > 15:
            questions.append(q)

    return questions