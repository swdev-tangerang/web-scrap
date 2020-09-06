import requests
from bs4 import BeautifulSoup

url = "https://www.detik.com/terpopuler"
response = requests.get(url, params={'tag_from': 'wp_cb_mostPopular_more'})
# print(response)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
populer_area = soup.find(attrs={'class': 'grid-row list-content'})
# titles = populer_area.findAll(attrs={'class': 'media__title'})
images = populer_area.findAll(attrs={'class': 'media__image'})
print("Pencetakkan images type hasil findAll:")
print(type(images))
for image in images:
    tag_a = image.find("a")
    tag_img = tag_a.find("img")
    print(tag_img['title'])
