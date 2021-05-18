'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class Exercise:
    def __init__(self, name, frequency, area):
        self.name = name
        self.frequency = frequency
        self.area = area

    def __str__(self):
        return f"I go to the {self.area} to {self.name} {self.frequency}."

class Training(Exercise):
    def __init__(self, name, frequency, area, machine):
        super().__init__(name, frequency, area)
        self.machine = machine

    def __str__(self):
        return f"I go to the {self.area} to {self.name} {self.frequency}, I especially love the {self.machine} machine."

class Cardio(Training):
    def __init__(self, name, frequency, area, machine):
        self.name = name
        self.frequency = frequency
        self.area = area
        self.machine = machine

    def __str__(self):
        return f"I do {self.name} on the {self.machine} {self.frequency} at the {self.area}."


running = Exercise("run", "daily", "track")
print(running)

training = Training("train", "weekly", "gym", "smith")
print(training)

cardio = Cardio("cardio", "monthly", "gym", "treadmill")
print(cardio)