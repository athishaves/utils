# COMMAND LINE :    python filename.py INPUT_PDF OUTPUT_PDF [ [ page_a page_b ] ..... ]

        
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


# Command Line arguments
args = sys.argv
print(str(args))


# Pdf location
inputPdf = PdfFileReader(open(args[1], "rb"))
outputPdf = PdfFileWriter()


def addPages (a, b):
	for i in range (a,b+1):
		outputPdf.addPage(inputPdf.getPage(i))
		
	    # Result Pdf location
		with open(args[2], "wb") as outputStream:
			outputPdf.write(outputStream)
			
			
for i in range (3,len(args),2):
	addPages(int(args[i]),int(args[i+1]))
