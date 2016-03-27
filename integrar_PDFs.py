#encoding=UTF-8
import PyPDF2 as f
import os

pdfFiles = []
#Colocar em uma lista os nomes de todos os PDFs em um diretório
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
#Com a lista pronta, colocá-la em ordem alfabética
pdfFiles.sort(key=str.lower)

pdfWriter = f.PdfFileWriter()
#print pdfFiles

#Abrir os PDFs e carregá-los em uma variável, a pdfReader
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = f.PdfFileReader(pdfFileObj)

    #Com todas as páginas abertas, iterá-la a partir da segunda página
    #para unir os PDFs na variável pdfWriter
    for pageNum in range (1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


#Com todas as páginas carregadas em pdfWriter,
#repassar o conteúdo para um novo PDF
pdfOutput = open('todos.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()