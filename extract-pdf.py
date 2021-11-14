import PyPDF2
# with open("Chemistry_paper_1__SL.pdf", "rb") as f:
#     reader = PyPDF2.PdfFileReader(f)
#     page = reader.getPage(0)
#     print(page.extractText())
    
# a=page1.extractText()

file = open("paper1.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
print(reader.numPages)
page  = reader.getPage(0)
print(page.extractText())