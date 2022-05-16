class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # instance method
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"


red_car = Car("Red", 30000)
blur_car = Car("Blue", 10000)

# print(red_car)
# print(blur_car)

for car in (blur_car, red_car):
    print(f"The {car.color} car has {car.mileage} miles")
