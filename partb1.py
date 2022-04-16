## Part B Task 1

import re
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description = "Output CSV file")
parser.add_argument('Filename',metavar='filename',type=str)
args=parser.parse_args()
output_filename=args.Filename

entries=sorted(os.listdir('cricket/'))[1:]
pattern=r'[A-Z]{4}\-\d{3}[A-Z]?(?![a-z])'
df=pd.DataFrame(columns=['filename','documentID'])

i=0
for file in entries:
    textfile=open('cricket/'+file)
    filetext=textfile.read()
    document_id=re.findall(pattern,filetext)[0]
    df.loc[i]=[file,document_id]
    textfile.close()
    i+=1

df=df.set_index('filename')
df.to_csv(output_filename)