import requests
import re
import json

url = 'https://monomax.by/map'
r = requests.get(url)
str = r.text
iter = re.finditer('\.Placemark\(\s*\[\d+\.\d+, {,2}\d+\.\d+\],\s*\{([^}]*)}\s*\)', str)
data = []
for i in iter:
    buffer = re.findall('\d+\.\d+', i[0])
    lat = float(buffer[0])
    lon = float(buffer[1])
    address = re.search('balloonContentHeader: .*\'', i[0])[0][23:-1]
    phone = re.search('balloonContentBody: .*\'', i[0])[0][30:-1]
    data_buffer = {
        "address": address,
        "latlon": [lat, lon],
        "name": "Мономах",
        "phones": phone
    }
    data.append(data_buffer)
with open("monomax.json", "w") as write_file:
    json.dump(data, write_file)