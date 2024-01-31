import csv

class Item:
    # class level attributes
    all = []
    pay_rate = 0.8  # after 20% discount
    

    # Instance level attributes
    # __init__ can only be used to create instance attributes 
    def __init__(self, name: str, price: float, quantity = 0):
        
        # Validating Arguements
        assert price >= 0, f"Price {price} should be greater than or eual to 0"
        assert quantity >= 0, f"quantity {quantity} should be greater than or eual to 0"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


        # Actions to execute 
        Item.all.append(self)



    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# Use Class methods when you need to initiate hundereds of instances from a csv json or any other type of file  
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_int(num):

        if isinstance(num, float):
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False

    def __repr__(self):
        return f"({self.name}, {self.price}, {self.quantity})"
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

phone1 = Phone("jscPhonev10", 500, 5, 1)

Item.instantiate_from_csv()
print(Item.is_int(7.5))
print(Item.all)



# Creating instances of the Item class with specific values
# item1 = Item('Phone', 200, 5)
# item2 = Item('Laptop', 1000, 2)
# item3 = Item('HeadPhones', 250, 8)
# item4 = Item('Mouse', 150, 4)
# item5 = Item('Keyboard', 200, 10)



# print(f"Price Before Applying Discount: {item1.price}")
# item1.apply_discount()
# print(f"{item1.name} Price After Applying Discount: {item1.price}")


# item2.pay_rate = 0.7
# print(f"Price Before Applying Discount: {item2.price}")
# item2.apply_discount()
# print(f"{item2.name} Price After Applying Discount: {item2.price}")



















# print(Item.pay_rate)
# print(item1.pay_rate)
# at first instance will try to find attribute on class level
# if it can not find it then it will find it on class level
# basically instances can access class attributes the same way

# print(Item.__dict__) # this will show all the attributes for class level in the form of a dictionory
# print(item1.__dict__) # this will show all the attributes for instance level in the form of a dictionory

