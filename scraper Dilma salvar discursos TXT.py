#encoding:utf-8
import csv
import urllib
import lxml.html
import unicodedata


#carregar o csv ou texto com todos os links
objeto = csv.reader(open('links.csv', 'rU'), dialect=csv.excel_tab)

for link in objeto:
    connection = urllib.urlopen(link[0])
    dom = lxml.html.fromstring(connection.read())
    discurso = []
    for d in dom.xpath('//div[@id="content-core"]/div/p/text()'):
        discurso.append(d)
    data = dom.xpath('//span[@class="documentPublished"]/text()[normalize-space()]')
    data1 = [date.strip() for date in data]
    print data1[0], discurso
    #arquivo1 = open(data[0]+'.txt', 'wb')
    #arquivo1 = arquivo.write(discurso)
    #arquivo1.close()

        #for para percorrer as linhas do csv/txt

    #scrape para pegar o link, correr o algoritmo para selecionar conteúdo


#guardar conteúdo da variável num txt com a data como nome

#fechar arquivo
arquivo.close()