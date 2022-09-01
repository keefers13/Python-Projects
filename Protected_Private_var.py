class Protected_Private_Var:
    def __init__(self):
        self.__privateVar = 30
        self._protectedVar = 3

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
