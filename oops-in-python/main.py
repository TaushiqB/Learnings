# Each variable has been instantiated from a class. Each Datatype is an object
class Item:
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item() # creating instance of the class
item1.name = "Tau"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price()) # calling the method to calculate total price

item2 = Item() # creating another instance of the class
item2.name = "T-Shirt"
item2.price = 50
item2.quantity = 10

# Displaying the type of each variable
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))