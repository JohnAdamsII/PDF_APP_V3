import glob, os, time, zipfile
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

parent_folder_path = os.getcwd()                          #get the path of where script is saved
parent_folder_files= os.listdir(parent_folder_path)       #get a list of all files in path


def get_files_list(extension):                            #given an extension returns a list of all those files in working-dir
    files_list = glob.glob("*."+str(extension))
    if (len(files_list) == 0):
        print("No files with "+str(extension)+" extension exist")
        #return None
    else:
        return files_list

def extension_to_PDF(filename):                         #given a filename as str, changes its extension to PDF
    sObject = slice(filename.rindex("."))
    new_filename = filename[sObject]+".pdf"
    return new_filename


def Converter(filename):
    im = Image.open(filename)
    if im.mode == "RGBA":
        im = im.convert("RGB")
    filename = extension_to_PDF(filename)
    if not os.path.exists(filename):
        im.save(filename,"PDF",resolution=100.0)
    

def cwd_PDF_deleter():                          #deletes PDFS in working dir
    PDF_files = glob.glob("*.pdf")
    if(len(PDF_files) == 0):
        print("No PDF files exists in folder")
        return None
    else:
        for item in PDF_files:
            if item == 'merged.pdf':
                continue
            os.remove(item)

def file_deleter(extension):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(str(extension))]:
                path = os.path.join(dirpath, filename)
                os.remove(path)

def mass_converter():
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in [f for f in filenames if f.endswith(".jpg")]:
                path = os.path.join(dirpath, filename)
                Converter(path)
        
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in [f for f in filenames if f.endswith(".PNG")]:
                path = os.path.join(dirpath, filename)
                Converter(path)

        for dirpath, dirnames, filenames in os.walk("."):
            for filename in [f for f in filenames if f.endswith(".jpeg")]:
                path = os.path.join(dirpath, filename)
                Converter(path)

    


def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
 
    for path in input_paths:
        pdf_merger.append(path)
 
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):                                    
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format(output_filename))

def convert_all():
    jpg_files = get_files_list("jpg")
    png_files = get_files_list("png")
    jpeg_files = get_files_list("jpeg")

    l = []
    l.extend(jpg_files)
    l.extend(png_files)
    l.extend(jpeg_files)
    

    if len(l) > 0:
        for i in range(len(l)):
            if l[i] is None:
                continue
            Converter(str(l[i]))
    else:
        return "no items to convert"

def unzipper():
    zips = glob.glob("*.zip")
    for items in zips:
        zip_ref = zipfile.ZipFile(items, 'r')
        zip_ref.extractall(os.getcwd())
        zip_ref.close()

    

if __name__ == '__main__':
    #convert_all()
    #mass_converter()
    #file_deleter(".pdf")
    #unzipper()






    



    """     pdf_files = get_files_list("pdf")

    merger('merged.pdf',pdf_files) 

    time.sleep(2)
      
    PDF_deleter() 

    pdf_splitter('merged.pdf') """
   