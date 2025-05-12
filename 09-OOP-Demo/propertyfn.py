# Exercise Name:
# 	09-OOP-Demo
# Description:
# 	Create a class and demonstrate how @property decorator is used

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.1416 * self._radius ** 2

    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            raise ValueError("Radius cannot be negative")


c = Circle(5)

print("Radius:", c.radius)
print("Area:", c.area)

c.radius = 10
print("Updated Area:", c.area)
