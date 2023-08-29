from PyPDF2 import PdfReader

li = [21,25,26,44,79]
for i in li:
    rpath = "./renshen/"+str(i) + ".pdf"
    wpath = "./retxtData2/"+str(i) + ".txt"
    #rpath = fixEOF(rpath)
    reader = PdfReader(rpath)
    for page in reader.pages:
        text = page.extract_text()
        txtfile = open(wpath,"a",encoding = "UTF-8")
        txtfile.write(text)
        txtfile.close()