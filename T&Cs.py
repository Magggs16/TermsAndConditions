import PyPDF2

bTos = open("TOS.pdf","rb") #rb for read binary mode
pdfTos = PyPDF2.PdfFileReader(bTos)
print("Number of pages: ")
print(pdfTos.numPages)

#get the page and extract text
print("Text by sentence :\n")
pageObj = pdfTos.getPage(0)

page = pageObj.extractText().replace('\n',' ')
pageSentences = ""
for t in page:
    if t == '.' :
        t = t.replace(".",".\n")
    pageSentences+=t
print(pageSentences)
     
# closing the pdf file object 
bTos.close() 
