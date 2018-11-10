#Merges all .pdf files in the current directory where this scipt is saved

from PyPDF2 import PdfFileMerger
import os,glob2,re

def  F_Merge(path):
    pdf_files = glob2.glob("*.pdf")
    if len(pdf_files) <= 1:
        print("Intially, No .pdf files in current directory or only one .pdf exists in directory")
    else:
        merger = PdfFileMerger()
        for files in pdf_files:
            merger.append(path+files)
        if not os.path.exists(path+'merged.pdf'):
            merger.write(path+'merged.pdf')
        merger.close()
        print('\n'.join(pdf_files)+"\nmerged to file named merged.pdf in current folder")


path = re.sub(r'\\',r'/',os.getcwd()[2:])+'/'
if __name__ == '__main__':
    F_Merge(path)

#path = re.sub(r'\\',r'/',os.getcwd()[2:])+'/'
#F_Merge(path)
