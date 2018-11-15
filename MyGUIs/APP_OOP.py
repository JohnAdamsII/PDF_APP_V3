import os, zipfile, time, threading
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

class File():

    """ File class used to retrieve file paths, unzip, and delete files"""

    # class attributes 
    root_dir = os.getcwd()
    Allowed_Extensions = [".jpeg", ".jpg", ".PNG", ".png",
                          ".pdf", ".PDF", ".JPEG", ".JPG", ".docx", ".DOCX",".zip",".ZIP"]
    files_list = []

    def __init__(self, directory=root_dir):
        """ class constructor """
        self.directory = directory
        self.files_list = []


    def getfiles(self, extension, recursive=False):
        """ given a LIST of extensions gets all files of those extensions in current working dir
            or all files of given extensions including subdirectories if recursive is set to true, 
                    Example: pass [".pdf"] to get pdf files       """
        
        #raise ValueError("Unsupported extension, please try again")

        if (recursive == True):
                for item in extension:
                    for dirpath, dirnames, filenames in os.walk(self.root_dir):
                        for filename in [f for f in filenames if f.endswith(item)]:
                            path = os.path.join(dirpath, filename)
                            self.files_list.append(path)
                return self.files_list

        else:
            for item in extension:
                for file in os.listdir(self.directory):
                    if file.endswith(item):
                        self.files_list.append(os.path.join(self.directory, file))
            return self.files_list

    def get_all_files(self):
        """ returns a list of all files and sub-directories from root directory, ignores git repos """

        All_Files_List = []

        for path, subdirs, files in os.walk(self.root_dir):
            for name in files:
                if ".git" not in path:
                    All_Files_List.append(os.path.join(path, name))
        return All_Files_List

    def getdir(self,name = None, path= None):
        """ returns a list of all files in a directory, given a path to directory, or directory name """

        if(path == None and name != None):
            path = self.getdirpath(name)     
           
        
        if(os.path.exists(path)):
            files_list = []
            [ files_list.append(os.path.join(path,x)) for x in os.listdir(path) ]
            return files_list
        
        else:
            raise FileNotFoundError("File not found, please check name or path")

    def getdirpath(self,name):
        """ returns path of directory give name """
        
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
                if dirpath[-len(name):] == name:
                    path = dirpath 
        return path

    def getfilepath(self,name):
        """ returns a file's path as a string, given it's name, 
        if more than one file of that name exists returns the one in highest directory """
        
        list_of_paths = []
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            if name in filenames:
                list_of_paths.append(os.path.join(dirpath,name))   
    
        return list_of_paths[0] 


    def unzip(self):
        """  unzips all files in current working dir and extracts there """

        zip_files_list = self.getfiles(".zip")

        for items in zip_files_list:
            zip_ref = zipfile.ZipFile(items, 'r')
            zip_ref.extractall(os.getcwd())
            zip_ref.close()

        return self

    def delete(self, extension, recursive=False):
        """ takes a LIST of extensions and deletes all files with that extension in current directory
        DANGEROUS when recursive == True deletes all files with given extension in all directories within root directory 
        Also, ignores any files with "merged.pdf" in them         """

        if (recursive == True):
            print("\nThe following files have been deleted: \n")
            to_be_deleted = self.getfiles(extension, recursive=True)
            to_be_deleted = [x for x in to_be_deleted if "merged.pdf" not in x]
            [[os.remove(x),print(x)] for x in to_be_deleted]

        else:
            print("\nThe following files have been deleted: \n")
            to_be_deleted = self.getfiles(extension)
            to_be_deleted = [x for x in to_be_deleted if "merged.pdf" not in x]
            [[os.remove(x),print(x)] for x in to_be_deleted]

        return self


class PDF(File,list):

    """class to convert, merge, and split PDF'S, subclass of File"""

    def __init__(self, directory = os.getcwd()):
        self.directory = directory

    def convert(self,l):
        """ takes in a list of files converts to PDF """
        
        for file in l:
            im = Image.open(file)
            if im.mode == "RGBA":
                im = im.convert("RGB")
            filename = self.extension_to_PDF(file)
            if not os.path.exists(filename):
                im.save(filename,"PDF",resolution=100.0)
                print(str(file)+" converted to PDF")

        return self

    def merge(self,input_paths,output_path="merged.pdf"):
        """ takes in a list of pdf file paths and merges to output file merged.pdf 
        in current working directory   """
        
        pdf_merger = PdfFileMerger()
 
        for path in input_paths:
            pdf_merger.append(path)
 
        with open(output_path, 'wb') as fileobj:
            pdf_merger.write(fileobj)
            pdf_merger.close()

        print("\nThe following files have been merged to file merged.pdf\n")
        [print(x) for x in input_paths]
        return self

    def split(self,path):
        """ given a path to a muti page PDF document, splits it into 
            single page PDF documents in current working directory """

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
        
        return self

    def extension_to_PDF(self,filename):
        """ Given a filename, changes it extension to PDF for convert method """                                                             
        sObject = slice(filename.rindex("."))
        new_filename = filename[sObject]+".pdf"
        return new_filename

    def word_to_PDF(self):
        pass
  
    


def main():
    """ TESTS """ 
    #my_dir = r"C:\Users\sk8rb_000\Desktop\test_folder\test_images"
    #myfile = [r"C:\Users\sk8rb_000\Desktop\test_folder\welding.jpg"]

    fileobj = File().getfiles(["jpeg"])

    time.sleep(2) 

    pdf_obj = PDF().convert(fileobj)

    """ time.sleep(2)
    
    mypdf_obj = PDF().getfiles([".pdf"])
    
    new_pdf_obj = PDF().merge(mypdf_obj)

    time.sleep(2) """
    
   
    #new_pdf_obj = PDF().split(mypdf_obj[0])
    #myfileobj = File().getfilepath("Mac.PNG")
    #myfileobj = File().getfilepath("PDF_GUI.pyw")
    #myfileobj = File().delete([".pdf",".PNG",".jpg",".jpeg"],recursive=True)
    # #myfileobj = File().unzip()
    
       
    


if __name__ == '__main__':
    main()











