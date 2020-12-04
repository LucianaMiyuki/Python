import PyPDF2

template = PyPDF2.PdfFileReader(open('merge_final.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
  	output.write(file)