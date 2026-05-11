# Polymorphism means having multiple(poly) forms(morph)

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print("Motorcycle is starting")

    def stop(self):
        print("Motorcycle is stopping")

# creating list of vehicles
vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018)
]

# Loop through list of vehicles and inspect
for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
    # if isinstance(vehicle, Vehicle):
    #     print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    #     vehicle.start()
    #     vehicle.stop()
    # else:
    #     raise Exception("Object is not a valid vehicle")