import pandas as pd
df = pd.read_excel (r'test.xlsx')
x=[]

for i in range (0, len(df)):
    x.append(df.iloc[i]['Domain'])

print (x)
print(type(df))
print (df)
print (len(df))


import pandas as pd
a_list = [1,2]
b_list = [3,4]

d = {'Domain': domain_list, 'Status': result_list}
df = pd.DataFrame(data=d)
print (df)


import pandas
from openpyxl import load_workbook

book = load_workbook('Masterfile.xlsx')
writer = pandas.ExcelWriter('Masterfile.xlsx', engine='openpyxl') 
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df.to_excel(writer, "Main", cols=['Diff1', 'Diff2'])

writer.save()