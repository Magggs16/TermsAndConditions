
import PyPDF2

bTos = open("TOS.pdf","rb") #rb for read binary mode
flagWords = open("Flags.txt","r") #open flags file 
pdfTos = PyPDF2.PdfFileReader(bTos)
print("Number of pages: ")
print(pdfTos.numPages)

#get the page and extract text
print("Text by sentence :\n")
pageObj = pdfTos.getPage(1)

page = pageObj.extractText().replace('\n',' ').replace('  ',' ')

pageSentences = ""


#****TO DO
#put all letters in an array and check if two spaces
#follow eachother replace one space as an '\n'
#then put each sentence in an array
sentenceCnt = 0
for t in page:
    if t == '.' :
        t = t.replace(".",".\n\n")
        sentenceCnt+=1
    pageSentences+=t
print(pageSentences)

#make page sentences array
sentences = ["" for x in range(sentenceCnt)]
pageSentences = ""
i = 0 
for t in page:
        if t == '.' :
            sentences[i] = pageSentences
            pageSentences = ""
            i = i+1
        pageSentences+=t


      
for i in range(0,sentenceCnt):
    for word in flagWords:
        #get word in flag text file
        for w in sentences[i].split():
            if word == w.lower():
                print(word)
                print("+++++++++++++++++++++++++++++++")
            


     
# closing the pdf file object 
bTos.close() 
flagWords.close()
