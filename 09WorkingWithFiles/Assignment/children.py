import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("../data/childDetails.json", "r")
children = json.load(f)
longest = 0
longestname= ""
shortest = 1000
shortestname = ""
for relatives in children:
    if len(relatives["name"]) > longest:
        longestname = relatives["name"]
        longest = len(relatives["name"])
    elif len(relatives["name"]) < shortest:
        shortest = len(relatives["name"])
        shortestname = relatives["name"]
print(shortestname)
print(longestname)

highest = ""
highestincome = 0
lowest = ""
lowestincome = 1000000000000000000
income = 0
for child in children:
    income = 0
    for incomes in child["guardians"]:
        income = incomes["salary"] + income
    if income > highestincome:
        highestincome = income
        highest = child["name"]
    if income < lowestincome:
        lowestincome = income
        lowest = child["name"]
print(highest,"     ", lowest)

parentsalary = 0
totalchildren = 0
highestchild = ""
highest = 0
for child in children:
    parentsalary = 0
    totalchildren = 1
    for sibling in child["siblings"]:
        totalchildren = totalchildren + 1
    for incomes in child["guardians"]:
        parentsalary = incomes["salary"] + parentsalary
    if parentsalary/totalchildren > highest:
        highest = parentsalary/totalchildren
        highestchild = child["name"]
print(highestchild)
parentsalary = 0
totalchildren = 0
highestchild = ""
highest = 100000000000
for child in children:
    parentsalary = 0
    totalchildren = 1
    for sibling in child["siblings"]:
        totalchildren = totalchildren + 1
    for incomes in child["guardians"]:
        parentsalary = incomes["salary"] + parentsalary
    if parentsalary/totalchildren < highest:
        highest = parentsalary/totalchildren
        highestchild = child["name"]
print(highestchild)
    
    