import PyPDF2

# recipe book pdf
# prints contents of page two
def read_pdf():
    file = 'path'
    with open(file, 'r+b') as f:
        reader = PyPDF2.PdfFileReader(f)
        print(reader.numPages)
        print(reader.getDocumentInfo())
        pageObj = reader.getPage(2)
        print("\n" + pageObj.extractText())


# every pages text is printed
def read_entire_pdf():
    file = 'path'
    with open(file, 'r+b') as f:
        reader = PyPDF2.PdfFileReader(f)
        # print(reader.numPages)
        # print(reader.getDocumentInfo())

        for page in range(0, reader.numPages):
            pageObj = reader.getPage(page)
            print("\n" + pageObj.extractText())


if __name__ == "__main__":
    read_entire_pdf()
