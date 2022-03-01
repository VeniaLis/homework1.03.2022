import requests
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
quates = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_ ='tags')



my_list = []
my_list2 = []

for q in quates:
   my_list.append(q.text)
for a in authors:
    my_list2.append(a.text)

my_dict = dict(zip(my_list,my_list2))
print(my_dict, end= '')


for q in range(0, len(quates)):
    print(quates[q].text + '\n' + authors[q].text)
    my_tags = tags[q].find_all('a', class_='tag')
    for my_tags in my_tags:
        print(my_tags.text)
    print('\n')