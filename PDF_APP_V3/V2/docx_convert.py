import os,re
from win32com import client

#folder = "C:\\Export_to_pdf"
#test = os.path.dirname(os.path.abspath(__file__))

s = os.path.dirname(os.path.abspath(__file__))
newstr = re.escape(s)
newstr = newstr[2:]
newstr2 = "C"+newstr
newstr = "C"+newstr+r"\\docx files 2B converted to PDF"


#folder = "C:\\Users\\sk8rb_000\\Desktop\\docx_convert\\Export_to_pdf"
folder = newstr
file_type = 'docx'
#out_folder = folder + "\\PDF_converted_from_docx"
out_folder = newstr2

os.chdir(folder)

if not os.path.exists(out_folder):
    print('Creating output folder...')
    os.makedirs(out_folder)
    print(out_folder, 'created.')
else:
    print(out_folder, 'already exists.\n')

for files in os.listdir("."):
    if files.endswith(".docx"):
        print(files)

print ('\n\n')

try:
    word = client.DispatchEx("Word.Application") # Using DispatchEx for an entirely new Word instance
    word.Visible = True # Added this in here so you can see what I'm talking about with the movement of the dispatch and Quit lines.
    for files in os.listdir("."):
        if files.endswith(".docx"):
            out_name = files.replace(file_type, r"pdf")
            in_file = os.path.abspath(folder + "\\" + files)
            out_file = os.path.abspath(out_folder + "\\" + out_name)
            doc = word.Documents.Open(in_file)
            print ('Exporting', out_file)
            doc.SaveAs(out_file, FileFormat=17)
            doc.Close()

    word.Quit()

except (Exception, e):
    print (e)
