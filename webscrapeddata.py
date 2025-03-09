
pip install beautifulsoup4
!pip install selenium

## Movie Data

import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}
url="https://www.imdb.com/chart/top/"
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')
movies = []
for item in soup.select('h3',class_='ipc-title__text'):
    movies.append( item.text)
movies_250=[]

for i in movies:
    try:
        var=int(i.split('.')[0])
        movies_250.append(i)
    except:
        continue
df1=pd.DataFrame(movies_250)
df1
df1.to_csv('Movies Data.csv',index=False)
print(df1)

## States Data

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", {"class": "wikitable"})

rows = table.find_all("tr")[2:]  

states_data = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 7:  
        state_name = cols[0].text.strip() 
        population = cols[4].text.strip().split('[')[0]  
        states_data.append({"State": state_name, "Population": population})

df = pd.DataFrame(states_data)

print(df.to_string(index=False))

df.to_csv("us_states_population.csv", index=False)
print("Wikipedia data saved as us_states_population.csv")

