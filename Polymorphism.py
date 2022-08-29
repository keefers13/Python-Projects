#creating a parent class, then a child class that inherits from it


#this is the parent class, denoting an employee of a university
class faculty:
    name = "No Name Provided"
    email = ''
    password = '1234abcd'
    subject = ''
    account_number = 0

    def welcomeMessage(self):
        print("Welcome to our faculty!")
        

#this is a child class, inheriting the parent class attributes and adding attributes sepcific to tenured faculty
class tenured(faculty):
    PhD_type = ''
    years_tenured = 0

    def welcomeMessage(self):
        entry_name = input("Enter your last name: \n>>>")
        print("Welcome, Dr. {}!".format(entry_name))

#this is a child class, inheriting the parent class attributes and adding attributes sepcific to adjunct faculty

class adjunct(faculty):
    highest_degree_earned = ''
    years_employed = 0

    def welcomeMessage(self):
        entry_name = input("Enter your last name: \n>>>")
        print("Welcome, Professor {}!".format(entry_name))


if __name__ == "__main__":
    employee = faculty()
    employee.welcomeMessage()

    doctor = tenured()
    doctor.welcomeMessage()

    professor = adjunct()
    professor.welcomeMessage()
    


