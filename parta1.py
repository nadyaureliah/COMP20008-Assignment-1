import pandas as pd
import argparse

parser = argparse.ArgumentParser(description = "Output CSV file")
parser.add_argument('Filename',metavar='filename',type=str)
args=parser.parse_args()
output_filename=args.Filename

df=pd.read_csv('owid-covid-data.csv')

df['date']=pd.to_datetime(df['date'],format="%Y-%m-%d",errors='coerce')
df['month']=df['date'].dt.strftime('%m')
df['year']=df['date'].dt.strftime('%Y')

year_loc=df.loc[df['year']=="2020"]

final_total_cases=year_loc.groupby(['location','month'])[['total_cases']].max()
final_new_cases=year_loc.groupby(['location','month'])[['new_cases']].sum(min_count=1)
final_total_deaths=year_loc.groupby(['location','month'])[['total_deaths']].max()
final_new_deaths=year_loc.groupby(['location','month'])[['new_deaths']].sum(min_count=1)

output=final_total_cases.merge(final_new_cases, on=['location','month'])
output=output.merge(final_total_deaths,on=['location','month'])
output=output.merge(final_new_deaths,on=['location','month'])

output['case_fatality_rate']=output['new_deaths']/output['new_cases']
output=output.reindex(columns=['case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths'])
output=output.sort_values(by=['location','month'],ascending=True)
print(output.head())
output.to_csv(output_filename)