#!/usr/bin/python3

class Daycare:

    def __init__(self, animals):
        self.animals = animals

    @property
    def animals(self):
        return self.__animals
    @animals.setter
    def animals(self, animals):
        if not isinstance(animals, list):
            raise TypeError("animals must be a list")
        if not all(type(animal) is Animal for animal in animals):
            raise ValueError("animals must be list of Animals")
        elif len(animals) == 0:
            raise ValueError("list should not be empty")
        else:
            self.__animals = animals

    def __str__(self):
        border = "========================="
        row = "Animal #{}: {}\n"
        string = border + '\n'
        for i, v in enumerate(self.animals):
            string += row.format(i, v)
        string += border
        return string

class Animal:

    __VALID_SPECIES = ("dog", "cat", "bird")

    def __init__(self, name, species):
        self.name = name
        self.species = species

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        if not isinstance(name, str):
            raise TypeError("name should be string")
        if name == "":
            raise ValueError("name should not be empty")

    @property
    def species(self):
        return self.__species
    @species.setter
    def species(self, species):
        self.__species = species

        if species not in self.__VALID_SPECIES:
            raise ValueError("animal not supported")

def main():

    a = "Name: {}, Species: {}"
    dog = Animal("A", "dog")
    print (a.format(dog.name, dog.species))
    cat = Animal("b", "cat")
    print (a.format(cat.name, cat.species))
    bird = Animal("d", "bird")
    print (a.format(bird.name, bird.species))

    res = dog + cat + bird
    res2 = dog + bird
    res3 = res + res2
    print(res3)

if __name__ == "__main__":
    main()
