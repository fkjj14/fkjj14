class Dog:
    name='unknown'
    def __init__(self, breed, speed):
        self.is_walked=False
        self.breed = breed
        self.speed = speed
    
    def walk(self):
        print(f'dog {self.name} walks')
        self.is_walked=True


class DogSpike(Dog):
     name='Spike'
class DogMike(Dog):
    name='Mike'

my_dog=DogSpike('bulldog', 12)
friends_dog=DogMike('pitbull', 20)
print(f'my dog name is {my_dog.name} ')
print(f'my dog speed is {my_dog.name} km/h')
print(f'my')
