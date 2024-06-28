# Description: This script takes a PDF file as input and 
# creates a new PDF file with each page split in half.
# pip install pypdf

from pypdf import PdfReader, PdfWriter
import sys

if len(sys.argv) != 3:
    print("Usage: python half_page.py <input_file> <output_file>")
    sys.exit(1)
    
reader0 = PdfReader(sys.argv[1])
reader1 = PdfReader(sys.argv[1])

writer = PdfWriter()

for page0, page1 in zip(reader0.pages, reader1.pages):
    height = page0.mediabox.height
    page0.mediabox.bottom = height / 2
    page1.mediabox.top = height / 2
    writer.add_page(page0)
    writer.add_page(page1)
    
with open(sys.argv[2], "wb") as f:
    writer.write(f)
    