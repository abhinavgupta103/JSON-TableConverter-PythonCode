import json 
import csv

f = open('rawJSON.json') 
data = json.load(f) f.close()

f=csv.writer(open('converted.csv','wb+'))

for item in data: 
    f.writerow([item['pk'], 
    item['model']] + item['fields'].values())