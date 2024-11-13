import fitz
import pandas as pd

def extract_text_from_pdf(file_path):
    """Estrae il testo da un PDF usando PyMuPDF."""
    text = ''
    with fitz.open(file_path) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()

    return text.strip()

def save_data_to_csv(data, output_file):
    """Salva i dati in formato CSV usando Pandas."""
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
