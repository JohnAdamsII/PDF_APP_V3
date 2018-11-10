# Converts files  to PDF and merges

from PIL import Image
import os,glob2,re
from PDF_Merge_Script import F_Merge
#from docx_2_PDF import Docx_to_PDF

def Converter(filename):
    im = Image.open(filename)
    if im.mode == "RGBA":
        im = im.convert("RGB")
    if filename[-4:-1] == "jpe":
        new_filename = filename[:-4]+'pdf'
        if not os.path.exists(new_filename):
            im.save(new_filename,"PDF",resolution=100.0)
    else:
        new_filename = filename[:-3]+'pdf'
        if not os.path.exists(new_filename):
            im.save(new_filename,"PDF",resolution=100.0)

PNG_files = glob2.glob("*.PNG")
JPEG_files = glob2.glob("*.jpeg")
JPG_files = glob2.glob("*.JPG")
Docx_files = glob2.glob("*.docx")

if len(PNG_files) > 0:
    for item in PNG_files:
        Converter(re.sub(r'\\',r'/',os.getcwd()[2:])+'/'+''.join(item))

if len(JPEG_files) > 0:
    for items in JPEG_files:
        Converter(re.sub(r'\\',r'/',os.getcwd()[2:])+'/'+''.join(items))

if len(JPG_files) > 0:
    for items in JPG_files:
        Converter(re.sub(r'\\',r'/',os.getcwd()[2:])+'/'+''.join(items))


number = -1
if len(Docx_files) > 0:
    for items in Docx_files:
        number += 1
while(number >= 0):                        #THIS IS DUMB BUT IT WORKS(FIX L8ER)
    number -= 1
    Docx_to_PDF(Docx_files[number])

PDF_files = glob2.glob("*.pdf")
print(PDF_files)

F_Merge( re.sub(r'\\',r'/',os.getcwd()[2:])+'/')



#message = input("Do you want to merge the PDF files in current folder? (y/n) ")
# if message == 'y' or message =='Y' or message == 'yes' or message == 'Yes':












#message = input("Would you like to merge all .pdf files in current folder? (Y/N) ")
#if message == 'Y':
#filename_PNG = re.sub(r'\\',r'/',os.getcwd()[2:])+'/'+''.join(glob2.glob("*.PNG")) #Got to be a better way
#filename_JPEG = re.sub(r'\\',r'/',os.getcwd()[2:])+'/'+''.join(glob2.glob("*.jpeg"))
