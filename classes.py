import random

class Dog:  
    info = "sweet ball of fun"

    def __init__(self, name):
        print("woof Wooff!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my lucky number is {self.lucky_number}")

dog1 = Dog("Freyja")
dog2 = Dog("Gustave")
dog1.bark()
dog2.bark()

class Office:

    def __init__(self, name):
       
        print("Quiet")
        self.name = name
#testign git


class Desk(Office):

    height = "max"
    lenght = 120

    def change_height(self):
        self.height = "low"
        print(self.height)
    
    def __init__(self, name):
        print("desk is in the office")

desk1 = Desk("name")
print(desk1)


