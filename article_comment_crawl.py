import requests
from requests import get
from bs4 import BeautifulSoup

req = requests.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=20191029')
html = req.text
req.close()
if req.ok:
    print('ok')
else:
    print('failed')

soup = BeautifulSoup(html,'html.parser')

rankings_list = soup.select(
    'div.ranking_headline'
)
print(ranking_list)


f = open("a.html",'w')
f.write(html)
f.close()
def download(url):
    file_name = url.split('/')[-1]
    with open(file_name,"wb") as file:
        response = get(url)
        file.write(response.content)
