from Pet import Pet


class Dog(Pet):
    def __init__(self, name, type, tricks, owner):
        super().__init__(name, type, tricks)
        self.owner = owner

    def noise(self):
        print("Woof woof woof")
        return self

    def sleep(self):
        # print(f"Shhh {} is sleeping")
        super().sleep()
        return self

    def printInfo(self):
        print(self.owner)
