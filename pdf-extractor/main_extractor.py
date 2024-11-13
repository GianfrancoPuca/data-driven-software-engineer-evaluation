import os
import fitz
import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor
from utils import extract_text_from_pdf, save_data_to_csv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PDF_DIR = './pdfs'
OUTPUT_DIR = './output'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'extracted_data.csv')

def process_single_pdf(filename, pdf_dir=PDF_DIR):
    file_path = os.path.join(pdf_dir, filename)
    try:
        logger.info(f"Inizio elaborazione del file: {filename}")
        extracted_text = extract_text_from_pdf(file_path)
        logger.info(f"Completata elaborazione del file: {filename}")
        return {'filename': filename, 'content': extracted_text}
    except Exception as e:
        logger.error(f"Errore nell'elaborazione del file {filename}: {e}")
        return None


def process_pdfs_in_parallel(pdf_dir, output_file):
    """Elabora i PDF in parallelo e salva i risultati in un file CSV."""
    data = []
    pdf_files = []
    for root, dirs, files in os.walk(pdf_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))

    logger.info(f"Trovati {len(pdf_files)} file PDF da elaborare.")
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda f: process_single_pdf(os.path.basename(f), os.path.dirname(f)), pdf_files)
        data = [result for result in results if result is not None]
    if data:
        logger.info(f"Salvataggio dei dati estratti in {output_file}")
        save_data_to_csv(data, output_file)
        logger.info("Salvataggio completato.")


        
def run_pdf_processing():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logger.info("Inizio del processo di elaborazione dei PDF.")
    process_pdfs_in_parallel(PDF_DIR, OUTPUT_FILE)
    logger.info(f"Dati estratti e salvati in {OUTPUT_FILE}")

__all__ = ['process_single_pdf', 'process_pdfs_in_parallel', 'run_pdf_processing']


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logger.info("Inizio del processo di elaborazione dei PDF.")
    process_pdfs_in_parallel(PDF_DIR, OUTPUT_FILE)
    logger.info(f"Dati estratti e salvati in {OUTPUT_FILE}")
