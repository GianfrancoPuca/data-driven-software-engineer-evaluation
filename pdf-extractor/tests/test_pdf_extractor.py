import os
import pytest
from reportlab.pdfgen import canvas
from main_extractor import process_pdfs_in_parallel

@pytest.fixture
def setup_test_environment(tmpdir):
    test_pdf_dir = tmpdir.mkdir("pdfs")
    test_output_file = tmpdir.join("extracted_data.csv")
    pdf_path = test_pdf_dir.join("test-sample.pdf")
    c = canvas.Canvas(str(pdf_path))
    c.drawString(100, 750, "Questo è un PDF di test.")
    c.save()
    return str(test_pdf_dir), str(test_output_file)

def test_process_pdfs_in_parallel(setup_test_environment):
    pdf_dir, output_file = setup_test_environment
    process_pdfs_in_parallel(pdf_dir, output_file)
    assert os.path.exists(output_file), "Il file CSV non è stato creato"
