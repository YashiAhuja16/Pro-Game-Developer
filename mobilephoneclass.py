class MobilePhone():

    def __init__(self,model,battery ):
        self.model = model 
        self.battery = battery 
        print("Making a new Mobile Phone:")


    def show_details(self):
        print("Details of phone are:")
        print(self.model)
        print(self.battery)

    def use_phone(self):
        self.battery -= 5
        print("You used the phone. Battery is now:")
        print(self.battery)


MyPhone = MobilePhone("iPhone", 100)

MyPhone.show_details()

MyPhone.use_phone()

MyPhone.show_details() 