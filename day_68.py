
# Request Module in python


import requests
response=requests.get("https://www.youtube.com")
print(response.text)


# bs4 module
import requests
from bs4 import BeautifulSoup
url="https://www.youtube.com"
r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)