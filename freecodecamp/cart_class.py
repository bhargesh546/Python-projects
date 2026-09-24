"""
  Another example is a shopping cart where we do the following:

  Add items to the cart
  
  Remove items from the cart
  
  Get the number of items in the cart
  
  Check what items are in the cart
  
  Check if a specific item is in the cart
  
  Return or display an item at a specific index in the cart
  
  While we might have a method that adds items to the cart and removes certain items from the cart, we can create special methods for all the other functionality:
  
  __len__() to get the length of the items in the cart
  
  __iter__() to loop through the items in the cart so we can see them
  
  __contains__() to check if a specific item is in the cart
  
  __getitem__() to return or display an item at a specific index in the cart
  
  Here's an example of a Cart class with these user-defined methods and special methods:
"""

class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)

"""
cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart
"""
