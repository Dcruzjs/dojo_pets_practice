class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    # implement the following methods:
    # sleep() - increases the pets energy by 25

    def sleep(self):
        print("sleeping from Pet")
        if self.energy < 75:
            self.energy += 25
        return self
    # eat(self) - increases the pet's energy by 5 & health by 10

    def eat(self):
        if self.energy < 95:
            self.energy += 5
        if self.health < 90:
            self.health += 10
        return self
    # play(self) - increases the pet's health by 5

    def play(self):
        if self.health < 95:
            self.health += 5
    # noise(self) - prints out the pet's sound

    def noise(self):
        pass
