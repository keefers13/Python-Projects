
#this is the parent class, denoting an employee of a university
class faculty:
    name = "No Name Provided"
    email = ''
    password = '1234abcd'
    subject = ''
    account_number = 0

#this is a child class, inheriting the parent class attributes and adding attributes sepcific to tenured faculty
class tenured(faculty):
    PhD_type = ''
    years_tenured = 0


#this is a child class, inheriting the parent class attributes and adding attributes sepcific to adjunct faculty

class adjunct(faculty):
    highest_degree_earned = ''
    years_employed = 0
