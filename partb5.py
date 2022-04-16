## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
import math
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ps=PorterStemmer()
vectorizer=TfidfVectorizer()

input_keywords=sys.argv[1:]
keywords_str=""
for keys in input_keywords:
    keywords_str+=keys+" "

tokenized_keywords=nltk.word_tokenize(keywords_str.lower())
stemmed_keywords=[ps.stem(word) for word in tokenized_keywords]
    
df=pd.read_csv('partb1.csv')

entries=sorted(os.listdir('cricket/'))[1:]

filename_lst=[]
documentID_lst=[]
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
    stemmed_filetext=[ps.stem(word) for word in tokenized_filetext]
    for stem in stemmed_keywords:
        if stem in stemmed_filetext:
            boolean=1
        else:
            boolean=0
            break
    if boolean==1:
        filename_lst.append(file)
        documentID_lst.append(df.loc[df['filename']==file]['documentID'].values[0])
    textfile.close()
    i+=1


text_lst=[]
for file in filename_lst:
    textfile=open('cricket/'+file)
    filetext=textfile.read()
    filetext=re.sub(r'[^\w\s]',' ',filetext)
    filetext=re.sub(r'\d+','',filetext)
    filetext=re.sub(r'\s+',' ',filetext)
    filetext=filetext.lower()
    tokenized_filetext=nltk.word_tokenize(filetext)
    stemmed_filetext=[ps.stem(word) for word in tokenized_filetext]
    text_lst.append(' '.join(stemmed_filetext))

output={'documentID':[],'score':[]}
tfidf=vectorizer.fit_transform(text_lst)
vector=vectorizer.transform([' '.join(stemmed_keywords)])
cos_similar=cosine_similarity(tfidf,vector)
for n in range(len(documentID_lst)):
    output['documentID'].append(documentID_lst[n])
    output['score'].append(round(cos_similar[n][0],4))
df=pd.DataFrame.from_dict(output)
df=df.sort_values(by='score',ascending=False)
df=df.set_index("documentID")
print(df)