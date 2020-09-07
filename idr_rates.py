import requests

# url = "http://www.floatrates.com/daily/idr.json"
# json_data = requests.get(url)
contoh_json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.782242630006e-05, 'date': 'Sun, 6 Sep 2020 14:00:01 GMT', 'inverseRate': 14744.385516021}, 'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.7275394705128e-05, 'date': 'Sun, 6 Sep 2020 14:00:01 GMT', 'inverseRate': 17459.504297584}}
# print(contoh_json_data)
for data_json in contoh_json_data.values():
    print(data_json['code'])
    print(data_json['name'])
    print(data_json['date'])
    print(data_json['inverseRate'])
