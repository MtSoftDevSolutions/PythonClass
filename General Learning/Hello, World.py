Groceries = ['milk', 'eggs', 'bread', 'soda', 'sweets']
myGroceryList = list(Groceries)
for i in Groceries:
    print(i)
Groceries.append("vegetables")
for i in Groceries:
    print(i)
copier = Groceries.copy()

list1 = ['a', 'b', 'c', 'd', 'e', 'f'] 
list2 = [1, 2, 3, 4, 5, 6]
list3 = list1 + list2
print(list3)
list1.reverse()
print('Reversed List:', list1)
tupThis = ('horse', 'carriage', 'ox', 'plow', 'dog', 'sled')
print(tupThis)
for i in tupThis:
    print(i)
tupNum = tupThis.count('ox')
print(tupNum)
mySet = {'tennis', 'swimming', 'bbq', 'basketball', 'baseball'}
print(mySet)
mySet.add('stadiums')
print(mySet)
mySet.remove('bbq')
print(mySet)
mySet1 = set(('tennis', 'bbq', 'lemons', 'cherry pie', 'apple pie'))
diffSummer = mySet.difference(mySet1)
print(diffSummer)

audiDict = {
    "brand": "Audi",
    "model": "A8",
    "year": 2017
    }
print(audiDict)
print(audiDict["brand"])
x = audiDict.get("model")
print(x)
audiDict["year"] = 1994
audiDict["color"] = "royal blue"
print(audiDict)

famPort = {
    "wife" : {
        "name" : "Jessica",
        "year married" : 2017
        },
    "daughter" : {
        "name" : "Mailee",
        "birth year" : 2008
        },
    "Cat1" : {
        "name": "Romeo",
        "adoption date" : 2021
        },
    "Cat2" : {
        "name": "Merrick",
        "adoption date": 2021
        }
    }
