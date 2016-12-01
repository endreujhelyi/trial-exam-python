# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid:

    def __init__(self, size_a, size_b, size_c):
        self.a = size_a
        self.b = size_b
        self.c = size_c
        self.getSurface()
        self.getVolume()

    def getSurface(self):
        side_a = self.a * self.b
        side_b = self.a * self.c
        side_c = self.b * self.c
        return 2 * (side_a + side_b + side_c)

    def getVolume(self):
        return self.a * self.b * self.c
