'''
- Write a script with three classes that model everyday objects. OK
- Each class should have an __init__ method that sets at least three attributes OK
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string. OK
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
class Electronics:
    def __init__(self, type, usage, size):
        self.type = type
        self.usage = usage
        self.size = size

    def __str__(self):
        return f"I use my {self.type} for {self.usage}, I love that it is {self.size}."


class Coffee:
    def __init__(self, flavored, roasted, temperature):
        self.flavored = flavored
        self.roasted = roasted
        self.temperature = temperature

    def __str__(self):
        return f"I love {self.flavored} coffee! It is {self.roasted} roasted & tastes so good when its {self. temperature}."



class Shoes:
    def __init__(self, brand, color, activity):
        self.brand = brand
        self.color = color
        self.activity = activity

    def __str__(self):
        return f"My go to shoes for {self.activity} are my {self.color} {self.brand} shoes!"

    def __add__(self, other):
        workout = self.activity + other.activity
        return workout

laptop = Electronics("laptop", "work", "large")
ipad = Electronics("ipad", "fun", "small")
phone = Electronics("phone", "everything", "small")


vanilla = Coffee("vanilla", "slow", "hot")
caramel = Coffee("caramel", "slow", "cold")
mocha = Coffee("mocha", "medium", "cold")


running = Shoes("nike", "black", "running")
training = Shoes("reebok", "grey", "training")
walking = Shoes("adidas", "pink", "walking")

print(running)
