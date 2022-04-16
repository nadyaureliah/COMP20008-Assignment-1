import pandas as pd
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description = "Output CSV file")
parser.add_argument('FilenameA',metavar='filenameA',type=str)
parser.add_argument('FilenameB',metavar='filenameB',type=str)
args=parser.parse_args()
filename_a=args.FilenameA
filename_b=args.FilenameB

df=pd.read_csv('owid-covid-data-2020-monthly.csv')

new_cases=df.groupby(['location'])[['new_cases']].sum(min_count=1)
new_deaths=df.groupby(['location'])[['new_deaths']].sum(min_count=1)

output=new_deaths.merge(new_cases,on=['location'])
output['case_fatality_rate']=output['new_deaths']/output['new_cases']

scatter_a=plt.scatter(output['new_cases'],output['case_fatality_rate'],alpha=0.5,s=25,edgecolor='black')
plt.xlabel('Confirmed New Cases')
plt.ylabel('Case Fatality Rate')
plt.grid(True)
plt.title('Case Fatality Rate vs Confirmed New Cases in 2020 by Location')
plt.annotate('Yemen',xy=(2099.0,0.290615))
plt.annotate('Mexico',xy=(1426090.0,0.08821813490))
plt.annotate('World',xy=(82735546.0,0.022055))
plt.savefig(filename_a)


scatter_b=plt.scatter(output['new_cases'],output['case_fatality_rate'],alpha=0.5,s=25,edgecolor='black')
plt.xlabel('Confirmed New Cases')
plt.ylabel('Case Fatality Rate')
plt.grid(True)
plt.title('Case Fatality Rate vs Confirmed New Cases in 2020 by Location (Log Scale)')
plt.annotate('Yemen',xy=(2099.0,0.290615))
plt.annotate('Fiji',xy=(31.0,0.06451612903))
plt.annotate('Mexico',xy=(1426090.0,0.08821813490))
plt.annotate('World',xy=(82735546.0,0.022055))
plt.xscale('log')
plt.savefig(filename_b)