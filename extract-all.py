import PyPDF2

FILE_PATH = './paper1.pdf'

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    # for page in reader.pages:
    page = reader.getPage(0)
    print(page.extractText())