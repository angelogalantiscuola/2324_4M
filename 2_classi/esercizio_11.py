class Bike:
    def __init__(self, speed, marcia):
        self.speed = speed
        self.marcia = marcia

    def speedUp(self):
        self.speed += 1

    def speedDown(self):
        self.speed -= 1

    def setMarcia(self, nuova_marcia):
        self.marcia = nuova_marcia

    def __str__(self):
        return f"Bike(speed={self.speed}, marcia={self.marcia})"


class FatBike(Bike):
    def __init__(self, speed, marcia, spessore_pneumatico):
        super().__init__(speed, marcia)
        self.spessore_pneumatico = spessore_pneumatico

    def getSpessorePneumatico(self):
        return self.spessore_pneumatico

    def __str__(self):
        return f"FatBike(speed={self.speed}, marcia={self.marcia}, spessore_pneumatico={self.spessore_pneumatico})"


class MountainBike(Bike):
    def __init__(self, speed, marcia, ammortizzatori):
        super().__init__(speed, marcia)
        self.ammortizzatori = ammortizzatori

    def getAmmortizzatori(self):
        return self.ammortizzatori

    def __str__(self):
        return f"MountainBike(speed={self.speed}, marcia={self.marcia}, ammortizzatori={self.ammortizzatori})"
    

# Create a Bike object
bike = Bike(10, 2)
print(bike) # Bike(speed=10, marcia=2)
# Create a FatBike object
fatBike = FatBike(10, 2, 4)
print(fatBike) # FatBike(speed=10, marcia=2, spessore_pneumatico=4)
# Create a MountainBike object
mountainBike = MountainBike(10, 2, True)
print(mountainBike) # MountainBike(speed=10, marcia=2, ammortizzatori=True)
print(fatBike.getSpessorePneumatico())
fatBike.speedUp()
fatBike.speedUp()
print(fatBike) # FatBike(speed=12, marcia=2, spessore_pneumatico=4)
fatBike.setMarcia(3)
print(fatBike) # FatBike(speed=12, marcia=2, spessore_pneumatico=4)

