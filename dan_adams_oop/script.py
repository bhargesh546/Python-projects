class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof Woof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number



owner1 = Owner("Danny", "122 Springfield Drive", "647-888-4785")
owner2 = Owner("Sally", "130 Springfield Drive", "647-999-4274")

dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(f"{dog1.owner.name} is the owner of a {dog1.breed} called {dog1.name}")

dog2 = Dog("Freya", "Greyhound", owner2)
print(f"{dog2.owner.name} is the owner of a {dog2.breed} called {dog2.name}")
