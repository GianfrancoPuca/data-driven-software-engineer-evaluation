import os
from reportlab.pdfgen import canvas

PDF_DIR = './pdfs'
NUM_PDFS = 1000

def generate_pdf(file_path, content="Questo è un PDF di test"):
    """Genera un singolo file PDF con contenuto specificato."""
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, content)
    c.save()

def generate_multiple_pdfs(pdf_dir, num_pdfs):
    """Genera multipli file PDF nella cartella specificata."""
    os.makedirs(pdf_dir, exist_ok=True)
    for i in range(1, num_pdfs + 1):
        file_path = os.path.join(pdf_dir, f'test-sample-{i}.pdf')
        generate_pdf(file_path)
        if i % 100 == 0:
            print(f"Generati {i} file PDF.")

if __name__ == '__main__':
    print(f"Inizio generazione di {NUM_PDFS} file PDF...")
    generate_multiple_pdfs(PDF_DIR, NUM_PDFS)
    print(f"Completata la generazione di {NUM_PDFS} file PDF nella cartella {PDF_DIR}.")
