import urllib
import lxml.html
import csv
import unicodedata
discurso = []

connection = urllib.urlopen('http://www2.planalto.gov.br/acompanhe-o-planalto/discursos/discursos-da-presidenta/discurso-da-presidenta-da-republica-dilma-rousseff-durante-sancao-da-lei-que-altera-o-simples-nacional-brasilia-df')
dom = lxml.html.fromstring(connection.read())

for d in dom.xpath('//div[@id="content-core"]/div/p/text()'):
    print d


#carregar o csv ou texto com todos os links
#objeto = csv.reader(open('links.csv', 'rU'))


#for link in objeto:
    #print link[0]