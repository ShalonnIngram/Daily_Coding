'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, color):
        self.name = name
        self.color = color


venus = Planet("Venus", "red")
print(venus.name, venus.color)
