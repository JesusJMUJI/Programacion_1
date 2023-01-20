class House:  # heigh, width, numberOfWalls
    def __init__(self, _height, _area, _numberOfWalls):
        self.height = _height
        self.area = _area
        self.numberOfWalls = _numberOfWalls

    def __str__(self):
        return "House with height: {0}, width: {1}, numberOfWalls: {2}".format(self.height, self.area, self.numberOfWalls)

    def Expand(self, heightIncrement, areaIncrement):
        self.height += heightIncrement
        self.area += areaIncrement

    def GetPrice(self):
        volume = self.area * self.height
        cost = volume * self.numberOfWalls
        return cost

    def __add__(self, other):
        newHouse = House(self.height, self.area, self.numberOfWalls)

        newHouse.Expand(other.height, other.area)

        newHouse.numberOfWalls += other.numberOfWalls

        return newHouse

    def __sub__(self, other):
        newHouse = House(self.height, self.area, self.numberOfWalls)

        newHouse.Expand(-other.height, -other.area)

        newHouse.numberOfWalls += other.numberOfWalls

        return newHouse

    def __eq__(self, other):
        return self.height == other.height and self.area == other.area

    def __ne__(self, other):
        return self.height != other.height or self.area != other.area

    def __gt__(self, other):
        return self.GetPrice() > other.GetPrice()


# construction site

apartment = House(5, 12, 4)

villa = House(20, 120, 50)

apartment.Expand(30, 200)

print(apartment)
print(villa)

print('My house is worth {0}'.format(villa.GetPrice()))

bungaloo = apartment + villa
print(bungaloo)
print(bungaloo.GetPrice())
print(bungaloo - apartment)

print('My hosue is bugger {0}'.format(apartment > villa))
villa.Expand(1000, 1000)
print('My hosue is bugger {0}'.format(apartment < villa))
