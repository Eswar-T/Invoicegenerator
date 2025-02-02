import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("textfiles/*.txt")
# df = pd.read_fwf(filepath)
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:

    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.title()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=invoice_nr)
    pdf.output(f"PDFS/{filename}.pdf")


# pdf.output("output.pdf")