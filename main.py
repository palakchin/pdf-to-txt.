# importing required modules
import PyPDF3

# creating a pdf file object
pdfFileObj=open('test.pdf','rb')

# creating a pdf reader object
pdfReader=PyPDF3.PdfFileReader(pdfFileObj)

# printing Information of pdf file
print(pdfReader.documentInfo)

# printing number of pages in pdf file
print(pdfReader.numPages)

# printing extracted text from pdf file
print(pdfReader.getPage(45).extractText())

# using for loop for extract text of specific number of pages from pdf file
str = ""
for i in range (1, 20):
    str += pdfReader.getPage(i).extractText()

# storing extracted text in Text File
with open('Text.txt', "w", encoding='utf-8') as f:
 f.write(str)
 





    
    