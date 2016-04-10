#encoding:utf-8
import csv
import urllib
import lxml.html
import unicodedata
import os

objeto = csv.reader(open('links.csv', 'rU'), dialect=csv.excel_tab)

for link in objeto:
    connection = urllib.urlopen(link[0])
    dom = lxml.html.fromstring(connection.read())
    discurso = []
    #for d in dom.xpath('//div[@id="content-core"]/div/p/text()'):
    for d in dom.xpath('//div[@id="parent-fieldname-text"]/div/p/text()'):
        discurso.append(d)
    d1 = " ".join(discurso)
    data = dom.xpath('//span[@class="documentPublished"]/text()[normalize-space()]')
    data1 = [date.strip() for date in data]
    #print data1[0], d1
    make_string = "-".join(data1)
    make_string= make_string.replace("/", "-")
    file = open(make_string + '.txt', 'w')
    #file = file.write(d1)
    file = file.write(unicodedata.normalize('NFKD', d1).encode('ascii', 'ignore'))
    #file.close()

    #filename = make_string+'.txt'
    #location = '/Users/guilhermefelitti/Desktop/discursos/'
    #for filename in os.listdir(location):
        #nome = os.path.join(location, filename)
    #with open(nome) as file_object:
        #write(d1)