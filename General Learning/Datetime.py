""" datetime.datetime.now() will make everything current %a will get the Day string, %d will get the day of the month as an INT, %B will get the Month in string, %Y will get the full year 'i.e. 2021'
%I will get you the hour in 12hr format, %M will get you the current minute, and %p will tell you if it's AM or PM %c will get you everything combined """


import datetime
x = datetime.datetime.now()
print(x.strftime("It is: " + "%a " + "the " + "%d " +"of " + "%B " + "the year is: " + "%Y " +
                 "the time is: "+"%I" + ":" + "%M" +" %p" + " so it is... " + "%c"))

#random is the module used, random.randrange (x, y) used the imported module to get a random range between two numbers 
import random
print(random.randrange(1, 100))

a = 12
b = 12.5
if b < a:
    print("b is greater than a")
    if a > 21:
        print("You can legally consume alcohol")
    else:
        print("You are not as old as b and you can not go to college parties.")
elif a == b:
    print('a and b are equal')
else:
    print ("a is not greater than b and it is not the same number")

"""i = 1
while i < 100:
    print(i)
    if i == 97:
        break
    if i == 7:
        continue
    i+= 6
else:
    print("This can no longer continue, or it will go past 100")
    """
mySentence = "loves the color"

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name) :
    lst = []
    for i in color_list:
       msg = "{} {} {}".format (name, mySentence, i)
       lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input("What is your name? ")
        if name  == '':
            print("You need to provide your name!")
        elif name == 'Sally':
            print('Sally, you may not use this software.')
            
        else:
            go = False
    lst = color_function (name)
    for i in lst :
        print(i)

mySentence1 = "May I interest you in..."
italianList = ('Chicken parm', 'Spaghetti and Meatballs', 'Spaghetti and Sauce', 'Italian Sausage and Peppers')
japaneseList = ('Hibachi Chicken', 'Hibachi Steak', 'Sushi', 'Tempura')
americanList = ('Fried Chicken and Waffles', 'Hamburger and Fries', 'Chicken \'n Dumplins')
mexicanList = ('Burritos', 'Nachos', 'Tamales', 'Enchilladas', 'Carne Asada')
def dinnerPlans():
    def get_name1():
    go = True
    while go:
        name = input("What is your name? ")
        if name  == '':
            print("You need to provide your name!")
        else:
            go = False
while name:
    print("{}, hello. What would you like for dinner tonight?".format(name))
    choice = input("Please type out which choice you'd like to make, with the first letter capitalized, between: Italian, Japanese, American, or Mexican: ")
    if choice = Italian:
        for i in italianList:
        print ("{} {} {}".format (name, mySentence1, i))
    elif choice = Japanese:
        for i in japaneseList:
        print("{}{}{}".format(name, mySentence1, i))
    elif choice = American:
        for i in americanList:
        print("{}{}{}".format(name, mySentence1, i))
    elif choice = Mexican:
        for i in mexicanList:
        print("{}{}{}".format(name, mySentence1, i))
    else:
        print("Oops, there may have been a mistake along the way here. Please make sure you put a capital letter at the start of your food choice. If you did, it was the developers fault and he will get it fixed soon")
    
    
        


