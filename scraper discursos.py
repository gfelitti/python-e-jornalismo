#coding = utf-8
import urllib
import lxml.html
import csv
import unicodedata

data =[]
titulo = []
link = []
connection = urllib.urlopen('http://www2.planalto.gov.br/acompanhe-o-planalto/discursos/discursos-da-presidenta?b_start:int=900')
dom = lxml.html.fromstring(connection.read())

for c in dom.xpath('//span[@class="summary-view-icon"]/text()'):
    data.append(c)

#for row in data: # select the url in href for all a tags(links)
    #row[0] = data
    #writer.writerow(data)

#titulo
for d in dom.xpath('//a[@class="summary url"]/text()'):# select the url in href for all a tags(links)
    titulo.append(
        unicodedata.normalize('NFKD', d).encode('ascii', 'ignore')
    )

#links
for e in dom.xpath('//h2[@class="tileHeadline"]//a/@href'):# select the url in href for all a tags(links)
    link.append(e)

data = data[1::6]
print len(titulo)
print len(link)

nova = [item.strip() for item in data]
print len(nova)

with open('discurso1.csv', 'wb') as discurso_csv:
    discursowriter = csv.writer(discurso_csv, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    discursowriter.writerow(data)
    discursowriter.writerow(titulo)
    discursowriter.writerow(link)

#csv.close()
