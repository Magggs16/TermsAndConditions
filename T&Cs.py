
import PyPDF2

bTos = open("TOS.pdf","rb") #rb for read binary mode
flagWords = open("Flags.txt","r")
pdfTos = PyPDF2.PdfFileReader(bTos)
#print("Number of pages: ")
#print(pdfTos.numPages)

#create dictionary outside of for loop to be able to collect ALL of the flag sentences
flagDictionary ={}

#fill keys in dictionary
for word in flagWords:
        flagSentence = []
        flagDictionary.update({word.strip():flagSentence})
flagWords.close()

#only traverse through 10 pages to minimize output ideally
#program would traverse through all pages for the user
for j in range(0,10):
    #get the page and extract text
    pageObj = pdfTos.getPage(j)
    page = pageObj.extractText().replace('\n',' ').replace('  ',' ')
    #create a string to form sentence
    pageSentences = ""
    #keep track of how many sentences there are
    sentenceCnt = 0
    for t in page:
        if t == '.' :
            t = t.replace(".",".\n\n")
            sentenceCnt+=1
        pageSentences+=t
        
    #make page sentences array
    sentences = []
    pageSentences = ""
    i = 0 
    for t in page:
            if t == '.' :
                sentences.append(pageSentences)
                pageSentences = ""
                i = i+1
            pageSentences+=t
            
    #compares word in sentence to word in flag words if the word is true store
    #the key word and sentence in a dictionary
    #create a dictionary to store flag words with specific sentence
    flagWords = open("Flags.txt","r")
    for word in flagWords:
        for i in range(0,sentenceCnt):
            #get word in flag text file
            for w in sentences[i].split(): 
                if word.strip() == w.strip('. ,').lower():
                    flagDictionary[word.strip()].append(sentences[i])   
    flagWords.close()
print(flagDictionary)
# closing the files
bTos.close()
flagWords.close()

#create html output with dictionary
htmlOutput = ''
for key in flagDictionary:
        htmlOutput+="<div cellspacing=\"0\" style=\"padding-right: 5px;width:800;height:20; border:1px solid rgb(160, 160, 160); background-color:rgb(160, 160, 160);\"><font face=\"helvetica neue, helvetica, arial,verdana, sans-serif\"><span style=\"font-size:13px;\"><span style=\"color: white\"><strong>"+key.upper()+"</strong></span></span></span></font></table>"
        for sent in flagDictionary[key]:
                htmlOutput+="<div border = \"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"width:700px; padding-bottom:10px; padding-left:0px;\"><ul style=\"list-style-position:inside; text-indent: -.4em;\">"+sent+"</ul></div>"
#write to an html template to create a more aesthetic output
template = ''
with open('ToSOutput.html', 'r') as file:
    template = file.read()
    file.close()

template = template.replace(r'{key}',htmlOutput)

with open('out.html', 'w') as file:
    file.write(template)
    file.close()

