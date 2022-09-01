class Protected_Private_Var: # creating an object that uses both protected and provate variables
    def __init__(self):
        self.__privateVar = 30 # the private variable
        self._protectedVar = 3 # the protected variable

    def getPrivate(self):
        print(self.__privateVar) 
    
    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected_Private_Var()
obj.getPrivate()
obj.setPrivate(30 + 1)
obj.getPrivate()
obj._protectedVar = 4
print(obj._protectedVar)
