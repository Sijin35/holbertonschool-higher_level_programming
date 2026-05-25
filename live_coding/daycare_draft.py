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
    
    def __add__(self, new_name):
        return Daycare([self, new_name])
    
    def __str__(self):
        self.species = species
        if species in self.__VALID_SPECIES == "dog":
            d = "Woof Woof, my name is {self.name}"
            return d
        elif species in self.__VALID_SPECIES == "cat":
            c = "Meow Meow, my name is {self.name}"
            return c
        elif species in self.__VALID_SPECIES == "bird":
            b = "Tweet Tweet, my name is {self.name}"
            return b
        else:
            err = "Uhh Huh"
            return err
   
class Neighborhood:
    
    __c = 0
    def __init__(self):
        if type(self).__c != 0:
            raise BaseException("Neighbourhodd can not be more than 1")
        else:
            type(self).__c += 1
        
        self.daycare_list = daycare_list

        @property
        def daycare_list(self):
            return self.__daycare_list
        @daycare_list.setter
        def daycare_list(self, daycare_list):
            self.__daycare_list = daycare_list

        def __del__(self):
            print("Neighborhood destroyed")
            __c -= 1

class RSPCA:
    
    def __init__(self, Animal=[]):
        self.animals_saved = []

    @property
    def animals_saved(self):
        return self.__animals_saved
    @animals_saved.setter
    def animals_saved(self, animals):
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
    print(res)
    res3 = res + res2
    print(res3)
    
    hood = Neighbourhood(res, res2)
    print(hood)
if __name__ == "__main__":
    main()
