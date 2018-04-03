class AnimalShelter(object):

    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalAge = 0

    """ enqueues """
    def enqueue(self, animalName, animalType):
        """ adds animals to the shelter """
        self.animalAge += 1
        newAnimal = Node(animalName, animalType)
        newAnimal.timestamp = self.animalAge
        if animalType == 'cat':

            if not self.headCat:
                self.headCat = newAnimal

        if self.tailCat:
            self.tailCat.pointer = newAnimal
            self.tailCat = newAnimal

        elif animalType == 'dog':

            if not self.headDog:
                self.headDog = newAnimal

        if self.tailDog:
            self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    """ Dequeues """
    def dequeuePrefDog(self):
        """ removes dogs """
        if self.headDog:
            newAnimal = self.headDog
            self.headDog = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            return 'No Dogs!'

    def dequeuePrefCat(self):
        """ removes cats """
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            return 'No Cats!'

    def dequeueNoPref(self):
        """ removes no pref """
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif self.headDog and not self.headCat:
            return self.dequeueDog()
        elif self.headDog and self.headCat:
            if self.headDog.timestamp < self.headCat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            return ('No Animals!')

    def _print(self):
        print('Cats:')
        cats = self.headCat
    while cats:
        print(cats.animalName, cats.animalType)
        cats = cats.pointer
        print('Dogs:')
        dogs = self.headDog
    while dogs:
        print(dogs.animalName, dogs.animalType)
        dogs = dogs.pointer


if __name__ == '__main__':
