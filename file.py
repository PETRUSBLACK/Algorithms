class Animal:

    def __init__(self, _name, _color):
        self.name = _name
        self.color = _color

    def setName(self, _name):
        self.name = _name

    def getName(self):
        return f'{self.name} {self.color}'

    def speak(self):
        print('hissssss')

    def __str__(self):
        return f'{self.name} {self.color}'

class Dogs(Animal):

    def __init__(self, _name, _color):
        super().__init__(self, _name, _color)

    def getName(self):
        return super().getName()
    
    def setName(self, _name):
        return super().setName(_name)

    def speak(self):
        return super().speak()



class Birds(Animal):
    pass

if __name__ == "__main__":
    animal1 = Animal('bingo','red')
    animal2 = Animal('Bruno','Green')
    print(animal1.getName())
    print(animal1.speak())
    animal1.setName('Brown')
    print(animal1)

    # print(animal2)
    # print(animal2.speak())