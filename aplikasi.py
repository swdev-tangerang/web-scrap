import requests
import bs4

url = "http://jadwalsholat.pkpu.or.id/monthly.php?id=308"
contents = requests.get(url)
print(contents)
print(contents.text)
