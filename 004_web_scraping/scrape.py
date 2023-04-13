import requests 
from bs4 import BeautifulSoup
import pprint

base_url = "https://news.ycombinator.com/news?p="
pages = 5

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k["votes"], reverse=True)

for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    url = f"{base_url}{i}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')



    
    def create_custom_hn(links, subline):
        hn = []
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].find('a').get("href", None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(" points", ""))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes':points})
        return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))

