from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://www.britannica.com/topic/list-of-the-smallest-countries-by-area'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)
soup.find('table')
table = soup.find('table')
print(table)
world_titles = soup.find_all('th')
world_titles
world_table_titles = [title.text for title in world_titles]
print (world_table_titles)
df = pd.DataFrame(columns = world_table_titles)
df
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text for data in row_data]
    length = len(df)
    df.loc[length]= individual_row_data
df
df.to_csv (r'C:\SmallestCountries.csv', index = False)