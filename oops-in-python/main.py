# Each variable has been instantiated from a class. Each Datatype is an object
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Initializing instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Tau", 100, 5) # creating instance of the class
print(item1.calculate_total_price()) # calling the method to calculate total price

item2 = Item("T-Shirt", 50, 10) # creating another instance of the class

# Displaying the type of each variable
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))