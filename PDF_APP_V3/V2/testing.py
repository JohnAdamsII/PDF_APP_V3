import os,re

s = os.path.dirname(os.path.abspath(__file__))
newstr = re.escape(s)
newstr = newstr[2:]
newstr2 = "C"+newstr
newstr = "C"+newstr+r"\\Export docx to PDF"


print (newstr)
print(newstr2)

#BASE_DIR = os.path.join( os.path.dirname( __file__ ), '..' )

#print(BASE_DIR)
