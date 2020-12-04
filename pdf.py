import PyPDF2

with open('Python.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	print('Quantidade de páginas do arquivo.')
	print(reader.numPages)

	print('Conteúdo da página. Na memória.')
	print(reader.getPage(0))

	print('Rotaciona o documento em 90 graus.')
	page = reader.getPage(0)
	page.rotateCounterClockwise(90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)