class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} says {sound}"

class JackRussel(Dog):
    def speak(self,sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass




# miles = Dog("Miles", 4, "Jack Russel Terries")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# Jim = Dog("Jim", 5, "Bulldog")

miles = JackRussel("Miles",4)
budldy = Dachshund("Buddy",9)
jack = Bulldog("Jack",3)
jim = Bulldog("Jim",5)

miles.species
budldy.name
print(jack)
jim.speak("Woof")

print(miles.speak())

