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
            h = True
            while h:
                print("{}, hello. What would you like for dinner tonight?".format(name))
                choice = input("Please type out which choice you'd like to make, with the first letter capitalized, between: Italian, Japanese, American, or Mexican: ")
                if choice == "Italian":
                    for i in italianList:
                        print ("{} {} {}".format (name, mySentence1, i))
                    break
                elif choice == "Japanese":
                    for i in japaneseList:
                        print("{} {} {}".format(name, mySentence1, i))
                    break
                elif choice == "American":
                    for i in americanList:
                        print("{} {} {}".format(name, mySentence1, i))
                    break
                elif choice == "Mexican":
                    for i in mexicanList:
                        print("{} {} {}".format(name, mySentence1, i))
                    break
                else:
                    print("Oops, there may have been a mistake along the way here. Please make sure you put a capital letter at the start of your food choice. If you did, it was the developers fault and he will get it fixed soon")
                    

                
    get_name1()
dinnerPlans()
