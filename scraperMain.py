import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

query = "Physical Therapists in Singapore"
search = query.replace(' ', '+')
results = 10
url = (f"https://www.google.com/search?q={search}&num={results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
soup_title = BeautifulSoup(requests_results.text,"html.parser")
links = soup_link.find_all("a")
heading_object=soup_title.find_all( 'h3' )
filePath = Path('scraperOutput.csv')
dataArray = []

for link in links:
  for info in heading_object:
    newLine = []
    get_title = info.getText()
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        newLine.append(get_title)
        newLine.append(link.get('href').split("?q=")[1].split("&sa=U")[0])
        dataArray.append(newLine)
        
df = pd.DataFrame(dataArray)
df.to_csv(filePath)
        