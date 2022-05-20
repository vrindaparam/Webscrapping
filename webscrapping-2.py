from bs4 import BeautifulSoup 
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions'
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.text,"html.parser")
print(soup)

rows = soup.find_all('tr')
cols = [t.text.rstrip() for t in rows[0].find_all('th')]
diz = {c:[] for c in cols}
print(diz)


for r in rows[1:]:
    diz[cols[0]].append(r.find('th').text.
                 replace('xa0', '').rstrip())
    row_other = r.find_all('td')
    for idx,c in enumerate(row_other):
        cell_text = c.text.replace('xa0', '').rstrip()
        diz[cols[idx+1]].append(cell_text)


df = pd.DataFrame(diz)
df.head()
df.to_csv('tableghg.csv')

