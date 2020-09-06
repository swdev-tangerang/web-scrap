import requests
import bs4

url = "http://jadwalsholat.pkpu.or.id/monthly.php?id=308"
contents = requests.get(url)
response = bs4.BeautifulSoup(contents.text, "html.parser")
data_highlight = response.find_all("tr", "table_highlight")
data = data_highlight[0]
print(data)
i = 0
sholat = {}
for d in data:
    print(d)
    if i == 1:
        sholat["subuh"] = d.get_text()
    elif i == 2:
        sholat["zuhur"] = d.get_text()
    elif i == 3:
        sholat["ashar"] = d.get_text()
    elif i == 4:
        sholat["maghrib"] = d.get_text()
    elif i == 5:
        sholat["isya"] = d.get_text()
    i += 1
print(sholat)
