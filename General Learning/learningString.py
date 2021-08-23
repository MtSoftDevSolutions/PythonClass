#### LEARNING STRING METHODS
myGreeting = "Ciao Bella!"
myMultiLine = '''Hello Dear,
How was your day?
Mine was great, but slightly rainy.'''
print (myGreeting)
print (myMultiLine)
print(myGreeting[-5:-1])
MultiLineLength = len(myMultiLine)
print (MultiLineLength)
toStrip = "      hairy   "
stripped = toStrip.strip()
print ("In winter it is good to be", stripped, "as it provides plenty of warmth.")
commander = myGreeting.upper()
print (commander)

if "Michael" not in myMultiLine:
    print("No, Michael, you're not included this time.")
if "Dear" in myMultiLine:
    print("Yes, you were called a Dear.")
myConcat = "Sometimes I play around and say \'{}\' to my wife." + " " + "She usually gets serious and just responds \"{}\"."
print(myConcat.format(myGreeting, myMultiLine))

##### LEARNING OPERATORS

print (300 * 765)
num1 = 77000
num2 = 76999
print(num1 >= num2)
num3 = 55,555
print(50000 < num2 and 60000< num1)
print(num3 is num1)
print(num2 is not num3)
print(5 in num3)
print ("not" not in myMultiLine)
a=1
print (a << 2)

animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')
listofAnimals = list(animal)
print(listofAnimals)
