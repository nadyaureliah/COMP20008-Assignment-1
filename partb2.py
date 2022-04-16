# Part B Task 2
import re
import os
import sys

textfile=open(sys.argv[1])
filetext=textfile.read()

filetext=re.sub(r'[^\w\s]',' ',filetext)
filetext=re.sub(r'\d+','',filetext)
filetext=re.sub(r'\s+',' ',filetext)
filetext=filetext.lower()

textfile.close()
print(filetext)