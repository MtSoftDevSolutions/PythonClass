class middleName:
    def __init__(self) :
        self._protectedVar = "Hunter"


obj = middleName ( )
obj._protectedVar = "Lauren"
print (obj._protectedVar)

class Middle:
    def __init__(self):
        self.__privateVar = "Lauren"

    def getPrivate(self):
        print(self.__privateVar)

    def getmiddleName(self):
        self._protectedVar = "Hunter"
        print(self._protectedVar)

obj = Middle()
obj.getPrivate()
obj.getmiddleName()
