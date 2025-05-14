class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5

    def feed(self):
        self.hunger = max(0, self.hunger - 2)
        print(f"{self.name} has been fed!")

    def play(self):
        if self.energy > 0:
            self.happiness = min(10, self.happiness + 2)
            self.energy = max(0, self.energy - 1)
            print(f"{self.name} is playing and having fun!")
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self):
        self.energy = min(10, self.energy + 3)
        print(f"{self.name} is resting...")

    def status(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}\n")
