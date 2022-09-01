
from abc import ABC, abstractmethod #importing in abstractmethod from abc module
class nomenclature(ABC):
    def fName(self, first_name):
        print("Your first name is: ", first_name)
    @abstractmethod
    def lName_guess(self, first_name):
        pass
    
class lName(nomenclature): # defining the lName_guess that was in the parect class nomenclature
    def lName_guess(self, first_name):
        if first_name == 'Keith':
            print('If your name is {}, then your last name must be Moore. '.format(first_name))
        else:
            print('Your name must not be as cool 🤷🏼‍♂️')
            
obj = lName()
obj.fName("Keith")
obj.lName_guess("Keith")
