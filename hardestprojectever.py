thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
x = thisdict["brand"]
thisdict = {
        "brand": "Mustang",
        "year": "1964",
        }
thisdict["year"] = 2018
for x in thisdict:
    print(x)
    for x in thisdict:
        print(thisdict[x])
for x in thisdict.values():
    print(x)
for x, y in thisdict.items():
    print(x,y)
    print(len(thisdict))
    thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
