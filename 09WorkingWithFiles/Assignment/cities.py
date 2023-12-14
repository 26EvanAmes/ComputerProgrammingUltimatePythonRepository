import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()
for city in cities:
    if city["state"] == "Kansas":
        print(city["city"])

maxlength = 0
maxlengthcity = ""
for city in cities:
    if len(city["city"]) > maxlength:
        maxlength = len(city["city"])
        maxlengthcity = city["city"]
print(maxlengthcity)

south = 100000000
southcity = ""
north = -20000000
northcity = ""
east = -20000000
eastcity = ""
west = 100000000
westcity = ""
for city in cities:
    if north < city["latitude"]:
        north = city["latitude"]
        northcity = city["city"]
    if south > city["latitude"]:
        south = city["latitude"]
        southcity = city["city"]
    if east < city["longitude"]:
        east = city["longitude"]
        eastcity = city["city"]
    if west > city["longitude"]:
        west = city["longitude"]
        westcity = city["city"]
print("N =>",northcity,"S =>", southcity,"E =>", eastcity,"W =>", westcity)


grow = 0
growcity = ""
shrink = 0
shrinkcity = ""
for city in cities:
    rate = city["growth_from_2000_to_2013"].split("%")
    rate = rate[0]
    if rate != "":
        rate = int(float(rate))
        if grow > rate:
            grow = rate
            growcity = city["city"]
        if shrink < rate:
            shrink = rate
            shrinkcity = city["city"]
print("Growing the most =>", growcity, "Shrinking the most =>", shrinkcity)

