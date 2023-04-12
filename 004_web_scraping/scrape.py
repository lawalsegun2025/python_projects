import requests 
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find('a').get("href")
        hn.append(href)
    return hn

print(create_custom_hn(links, votes))

#href = item.find('a').get("href")