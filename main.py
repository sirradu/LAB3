from num2t4ru import num2text
from docxtpl import DocxTemplate
import csv
from docx2pdf import convert
def callsms():
    array = []

    with open('data.csv') as file:
        reader = csv.reader(file)

        for row in reader:
            array.append(row)

    call = -20
    sms = 0

    for i in range(1, 10):
        if '915783624' in array[i][1]:
            call += float(array[i][3])
            sms += float(array[i][4])
    return("%.0f" % (call*2+sms*2))


def internet():
    list = []

    with open('nfcap.csv') as data:
        reader = csv.reader(data)
        for i in reader:
            list.append(i)

    ibyte = 0
    cost = 0

    for i in range(len(list)):
        if '192.168.250.27' in list[i]:
            ibyte += float(list[i][12])


    ibyte = ibyte / (2 ** 20)
    cost = ibyte * 1
    return("%.0f" % cost)

units = ((u'рубль', u'рубля', u'рублей'), 'm')
callsms_price = int(callsms())
internet_price = int(internet())
full_price = callsms_price+internet_price
ndc = "%.0f" % (full_price*0.2)
doc = DocxTemplate("empty.docx")
context ={
    'mobilecon' : callsms_price,
    'internetcon' : internet_price,
    'fullprice' : full_price,
    'ndc' : ndc,
    'word_price' : (num2text(full_price, units))
}
doc.render(context)
doc.save("invoice.docx")
convert("invoice.docx")

