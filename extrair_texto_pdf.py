import PyPDF2
PDFobj = open("arquivo.pdf", "rb")
PDFreader = PyPDF2.PdfFileReader(PDFobj)
print(PDFreader.numPages)
print(PDFreader.isEncrypted)

conteudo = ""
for c in PDFreader.pages:
    print(c.extractText())

print(pageObj.extractText())

print("TERMO")