class superheroNames: #This first class exists to set up the protected 
    def __init__(self):
        self._protectedVar = "Unknown" #Unknown is a place holder
obj = superheroNames()
obj._protectedVar = "Wolverine" #Unkown now becomes Wolverine and is printed as such
print(obj._protectedVar)

class superheroNames:
    def __init__(self):
        self.__privateVar = "Bub"
    def getPrivate (self):
        print(self.__privateVar) #Prints out Bub, again, bub is somewhat of a place holder existing for Logan
    def setPrivate(self, private):
        self.__privateVar = private
obj = superheroNames() #Calls the class superheroNames
obj.getPrivate() #Will print out Bub
obj.setPrivate("Logan") #Sets the private variable from Bub to Logan
obj.getPrivate() #Prints out Logan
