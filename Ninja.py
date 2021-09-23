class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, fN="Daniel", lN="Cruz", treats="KitKar 4.4", pet_food="Apple Crackers", Pet="pet"):
        self.first_name: fN
        self.last_name: lN
        self.treats: treats
        self.pet_food: pet_food
        self.pet: Pet

    # implement the following methods:

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    # feed(self) - feeds the ninja's pet invoking the pet eat(self) method
    def feed(self):
        self.pet.eat()
        return self

    # bathe(self) - cleans the ninja's pet invoking the pet noise(self) method
    def bathe(self):
        self.pet.noise()
        return self

    def printInfo(self):
        print(self)
        print(f"{self.pet_food}")
        print(f"{self.first_name}")
