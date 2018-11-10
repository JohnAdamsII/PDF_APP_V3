import os,glob2

PDF_files = glob2.glob("*.pdf")
print(PDF_files)

Num_of_files = 0

for files in PDF_files:
    Num_of_files += 1

index_var = Num_of_files-1

print(Num_of_files)
print(index_var)

while(index_var >= 0):
    if PDF_files[index_var] == 'merged.pdf':
         index_var -= 1
         continue
    else:
         os.remove(PDF_files[index_var])
         if index_var < 0:
             break
         else:
             index_var -= 1

# new_PDF_files = glob2.glob("*.pdf")
# print(new_PDF_files)
# print(len(new_PDF_files))


if __name__ == '__main__':
    pass
