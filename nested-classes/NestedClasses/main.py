class Dog:
    class Gate:
        def __init__(self, age, size):
            self.age = age
            self.size = size

        def get_details(self):
            if self.age <= 1 and self.age >= 10:
                return 'cage'
            elif self.size <= 5:
                return 'playground_small'
            else:
                return 'playground_big'

    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.size = None
        self.dogs = []

    def add_dog(self, dog_id, name, age, size):
        self.id = dog_id
        self.name = name
        self.age = age
        self.size = size
        dog_gate = self.Gate(age, size)
        self.dogs.append([dog_id, name, age, size, dog_gate])

    def list_dogs(self, gate):
        return [gate. () for dog in self.dogs[gate]]


dog = Dog()

dog.add_dog(1, "Buck", 3, 6)
for dog_playground in ("cage", "playground_small", "playground_big"):
    for dog_item in dog.list_dogs(dog_playground):
        print(dog_item)
