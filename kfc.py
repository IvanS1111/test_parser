import ijson
import json
from urllib.request import urlopen

f = 'https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true'
objects = ijson.items(urlopen(f), 'searchResults.item')
data = []
for i in objects:
    address = ''
    start_Weekday = ''
    end_Weekday = ''
    start_Weekend = ''
    end_Weekend = ''
    Weekday = ''
    Weekend = ''
    latlon = []
    try:
        address = i['storePublic']['contacts']['streetAddress']['ru']
    except:
        address = 'None'
    try:
        start_Weekday = str(i['storePublic']['openingHours']['regularDaily'][0]['timeFrom'])
        end_Weekday = i['storePublic']['openingHours']['regularDaily'][0]['timeTill']
        start_Weekend = i['storePublic']['openingHours']['regularDaily'][5]['timeFrom']
        end_Weekend = i['storePublic']['openingHours']['regularDaily'][5]['timeTill']
        Weekday = 'пн-пт ' + start_Weekday + ' до ' + end_Weekday
        Weekend = 'сб-вс ' + start_Weekend + ' до ' + end_Weekend
    except:
        Weekday = 'closed'
        Weekend = 'closed'
    try:
        latlon = [float(i['storePublic']['contacts']['coordinates']['geometry']['coordinates'][0]),
                       float(i['storePublic']['contacts']['coordinates']['geometry']['coordinates'][1])]
    except:
        latlon = ["None", "None"]
    buffer = {
            "address": address,
            "latlon": latlon,
            "name": i['storePublic']['title']['ru'],
            "phones": [i['storePublic']['contacts']['phone']['number']],
            "working_hours": [Weekday, Weekend]
        }
    data.append(buffer)
with open("kfc.json", "w") as write_file:
    json.dump(data, write_file)


