def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 56, 7))
print(add(1, 2, 3, 4, 8, 7, 6, 1, 2, 3, 4, 5, 6, 7, 8, 6, 5))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)  # Nissan
print(my_car.model) # None
