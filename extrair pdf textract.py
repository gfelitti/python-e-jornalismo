#encoding=utf-8
#instale o módulo textract
import textract
#carregue o arquivo, seja ele PDF ou CSV, em uma variável Texto
arquivo = textract.process('delcidio.pdf')

#salve o conteúdo tirado em um TXT
file = open("novo.txt", "w")
file.write(arquivo)
file.close()