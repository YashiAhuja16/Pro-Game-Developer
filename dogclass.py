class Dog():
    name = "Night"
    breed = "Dalmation" 

    def _init__(self):
        print("Making a new Dog:")
    
    def show_details(self): 
        print("Details of dog are:")
        print(self.name)
        print(self.breed)

    def change_details(self):
        self.name = input("Please enter the dog's name:")
        self.breed = input("Please enter the dog's breed:")
    
    def bark(self):
        print("Woof Woof!")

Fluffy = Dog()
Cuddles= Dog()

Fluffy.change_details()
Cuddles.change_details()

Fluffy.show_details()
Cuddles.show_details()

Fluffy.bark()
Cuddles.bark() 
