'''
:mod: shipmnt -- Process pdfs
========================================
..module:: text extraction
  :platform: Unix
  :synopsis: Classify a string as english or Hinglish
..moduleauthor:: Tushar Dhyani

Requirements::
	1. You will need to install PyPDF2 and tabula
		- Install PyPDF2: pip3 install PyPDF2
		- Install tabula: pip3 install tabula-py
	
'''
try:
	import argparse
	import PyPDF2
	import tabula
	import pandas as pd
	import os
	import sys
except ModuleNotFoundError as e:
	print(e,'''found, please install PyPDF2 and tabula
Requirements::
	1. You will need to install PyPDF2, pandas and tabula
		- Install PyPDF2: pip3 install PyPDF2
		- Install tabula: pip3 install tabula-py''')
	exit()




def extractText(root = './AICST/MF/HAWB',toFolder='./textFiles', verbose='False'):	
	print('Extracting text!')
	files=os.listdir(root)
	if not os.path.exists(toFolder):
		os.system('mkdir '+toFolder)
	for pdf in files:
		txt=''
		# Read all the files
		pdfFile = PyPDF2.PdfFileReader(os.path.join(root, pdf))
		# iterate through all pages:
		num = pdfFile.numPages
		for no in range(num):
			txt+=pdfFile.getPage(no).extractText()

		with open(os.path.join(toFolder,str(pdf.split('.')[0]))+'.txt','w') as f:
			f.write(txt)
		if verbose=='True':
			print(f'{pdf} done!')


def extractCsv(root = './AICST/MF/HAWB',toFolder='./csv', verbose='False'):
	print('Extracting CSV!')
	files=os.listdir(root)
	if not os.path.exists(toFolder):
		os.system('mkdir '+toFolder)
	root = './AICST/MF/HAWB'
	files=os.listdir(root)
	# paths = [os.path.join(root,i) for i in files]
	for pdf in files:
		txt=''
		try:
		    # Read all the files
			pdfFile = tabula.convert_into(os.path.join(root, pdf), os.path.join(toFolder,str(pdf.split('.')[0]+'.csv')))
			if verbose=='True':
				print(f'{pdf} done!')
		except:
			print(f'Error in {pdf}. Skipping...')


def main():
	'''
	PDF miner to extract text and csv tables from the pdfs.

	'''
	parser=argparse.ArgumentParser(description='''
		PDF mining
		''')
	parser.add_argument('-t','--text',action='store_true' ,help='Use this flag to extract text into txt folder')
	parser.add_argument('-c','--csv',action='store_true', help='Use this flag to convert pdf to csv into csv folder ')
	parser.add_argument('-v','--verbose',action='store_true', help='Use this flag enable verbosity. Default value is True')
	args = parser.parse_args()
	textextact=str(args.text)
	csvextract=str(args.csv)
	vb=str(args.verbose)
	# print(textextact, csvextract, vb)
	if textextact=='True':
		extractText(verbose=vb)
	elif csvextract=='True':
		extractCsv(verbose=vb)
	else :
		print('Please mention atleast one flag. Refer --help for more.')
	
if __name__ == '__main__':
	main()