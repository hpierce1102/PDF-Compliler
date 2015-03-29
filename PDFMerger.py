#!/usr/bin/env python3

import PyPDF2

def mergePDFs (files, output):
	mergedPDF = PyPDF2.PdfFileMerger()

	for path in files:
		#print(path)
		mergedPDF.append(path)

	outputLocation = open(output, "wb")
	mergedPDF.write(output)

paths = list()
paths.append("/home/hayden/PDF/A13_book_report.pdf")
paths.append("/home/hayden/PDF/A13_book_report.pdf")
paths.append("/home/hayden/PDF/A13_book_report.pdf")

mergePDFs(paths, "/home/hayden/PDF/compiled2.pdf")