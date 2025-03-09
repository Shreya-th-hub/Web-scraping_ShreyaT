import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "wikitable"})
rows = []
for row in table.find_all("tr")[1:]:  # Skip the header row
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    while len(cols) < len(headers):
        cols.append("") 
    
    rows.append(cols)
df = pd.DataFrame(rows, columns=headers)
df.to_csv("indian_military_aircraft.csv", index=False)

print(df.to_string(index=False))

print("Data saved as 'indian_military_aircraft.csv'")