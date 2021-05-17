import requests
import re
import pandas as pd
from openpyxl import load_workbook

result_list = []

url = "https://domenebi.ge/domain/search?domain="


def status_checker(domains):
    global result_list
    global url
    for i in range(0, len(domains)):
        request = requests.get(url + domains[i])
        web_text = str(request.content)
        result = re.search('<div class="panel-body domain-is-(.*?)">', web_text).group(1)
        result_list.append(result)


domain_list = []

df = pd.read_excel(r'Domains.xlsx')
for i in range(0, len(df)):
    domain_list.append(df.iloc[i]['Domain'])
status_checker(domain_list)

dict_for_df = {'Domain': domain_list, 'Status': result_list}
df = pd.DataFrame(data=dict_for_df)
print(df)

df.to_excel('Result.xlsx')
print("hid")
