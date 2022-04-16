## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os
from nltk.tokenize import word_tokenize

input_keywords=sys.argv[1:]
keywords_str=""
for keys in input_keywords:
    keywords_str+=keys+" "

tokenized_keywords=nltk.word_tokenize(keywords_str.lower())
    
df=pd.read_csv('partb1.csv')

entries=sorted(os.listdir('cricket/'))[1:]

i=0
boolean=0
for file in entries:
    textfile=open('cricket/'+file)
    filetext=textfile.read()
    filetext=re.sub(r'[^\w\s]',' ',filetext)
    filetext=re.sub(r'\d+','',filetext)
    filetext=re.sub(r'\s+',' ',filetext)
    filetext=filetext.lower()
    tokenized_filetext=nltk.word_tokenize(filetext)
    for tokens in tokenized_keywords:
        if tokens in tokenized_filetext:
            boolean=1
        else:
            boolean=0
            break
    if boolean==1:
        print(df.loc[df['filename']==file]['documentID'].values[0])
    textfile.close()
    i+=1