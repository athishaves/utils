from PyPDF2 import PdfFileWriter, PdfFileReader


# TODO : Pdf location
inputPdf = PdfFileReader(open(pdf_location, "rb"))

outputPdf = PdfFileWriter()


# Range from page a to b (exclusive)
for i in range (30, 39):
    outputPdf.addPage(inputPdf.getPage(i))

    # TODO : Result Pdf location
    with open(result_pdf_location, "wb") as outputStream:
        outputPdf.write(outputStream)