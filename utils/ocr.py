from pdf2image import convert_from_path
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(pdf_path):
    images = convert_from_path(
        pdf_path,
        poppler_path=r"C:\poppler\poppler-25.12.0\Library\bin"
    )

    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)

    return text