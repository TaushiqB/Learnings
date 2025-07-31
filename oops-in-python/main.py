# Each variable has been instantiated from a class. Each Datatype is an object
class Item:
    pass

item1 = Item() # creating instance of the class
item1.name = "Tau"
item1.price = 100
item1.quantity = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))