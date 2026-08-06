'''

def friend():
    print("My friend is kind")
    print("My friends name is Sarah.")
    print("My friends hair is red.")


friend()

'''

class Student():
    # properties/attributes 
    name = "Ben"
    age = 14 
    schoolclass = "9th"
    classteacher = "Ms. Alexa"

    # constructor
    def __init__(self):
        print("Making a new Student.")

    def show_details(self): 
        print("Details of student are: ")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.classteacher)
    
    def change_details(self): 
        self.age = int(input("Please enter your age:"))
        self.name = input("Please enter your name:")
        self.schoolclass = input("Please enter your schoolclass:")
        




# making object of student class 
Anika = Student()
Diya = Student()

Anika.change_details()
Diya.change_details()

Anika.show_details()
Diya.show_details()