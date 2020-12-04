import PyPDF2
import sys

# Para chamar esse programa:
# python merge_pdf.py Python.pdf Python_2.pdf tilt.pdf

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)
  merger.write('merge_final.pdf')

pdf_combiner(inputs)

