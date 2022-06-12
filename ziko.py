import re
import ijson
import json
from urllib.request import urlopen

f = 'https://www.ziko.pl/wp-admin/admin-ajax.php?action=get_pharmacies'
objects = ijson.items(urlopen(f),'')
values = list(next(objects).values())
data = []
for i in values:
    phone_str = ''
    try:
        index = int(i['hours'].rindex('tel. '))
        phone_str = re.sub('\r\n', '', i['hours'][index:])
        phone_str = phone_str[5:]
    except:
        phone_str = 'None'
    buffer = {
        "address": i['address'],
        "latlon": [i['lat'], i['lng']],
        "name": i['title'],
        "phones": phone_str,
        "working_hours": re.sub('<br>', ' ', i['mp_pharmacy_hours'])
    }
    data.append(buffer)
with open("ziko.json", "w") as write_file:
    json.dump(data, write_file)