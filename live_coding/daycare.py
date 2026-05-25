#!/usr/bin/python3

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
        if not isinstance(name, str):
            raise TypeError("name should be string")
        if name == "":
            raise ValueError("name should not be empty")
        self.__name = name

    @property
    def species(self):
        return self.__species
    
    @species.setter
    def species(self, species):
        if species not in self.__VALID_SPECIES:
            raise ValueError("animal not supported")
        self.__species = species

    def __str__(self):
       # return f"Name: {self.name}, Species: {self.species}"
        if self.species == "dog":
            return f"Woof Woof, my name is {self.name} the {self.species}"
        elif self.species == "cat":
            return f"Meow Meow, my name is {self.name} the {self.species}"
        elif self.species == "bird":
            return f"Tweet Tweet, my name is {self.name} the {self.species}"
        else:
            return "Uhh Huh"

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
        if not all(isinstance(animal, Animal) for animal in animals):
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

class Neighborhood:
    
    __c = 0
    def __init__(self, daycare_list):
        if Neighborhood.__c != 0:
            raise BaseException("Neighbourhodd can not be more than 1")
        
        Neighborhood.__c += 1
        self.daycare_list = daycare_list

    @property
    def daycare_list(self):
        return self.__daycare_list
    @daycare_list.setter
    def daycare_list(self, daycare_list):
        self.__daycare_list = daycare_list

    def __str__(self):
        return f"There are {len(self.daycare_list)} daycare/s currently"

    def __del__(self):
         print("Neighborhood destroyed")
         Neighborhood.__c -= 1


class RSPCA:
    
    def __init__(self, animals):
        self.animals_saved = animals

    @property
    def animals_saved(self):
        return self.__animals_saved

    @animals_saved.setter
    def animals_saved(self, animals):
        if not isinstance(animals, list):
            raise TypeError("animals must be a list")
        if not all(isinstance(animal, Animal) for animal in animals):
            raise ValueError("animals must be list of Animals")
        elif len(animals) == 0:
            raise ValueError("list should not be empty")
        else:
            self.__animals_saved = animals

    def __str__(self):
        print("Animals saved")
        border = "========================="
        row = "Animal #{}: {}\n"
        string = border + '\n'
        for i, v in enumerate(self.animals_saved):
            string += row.format(i, v)
        string += border
        return string

def main():

    dog = Animal("Bark", "dog")
   # print(dog)
    cat = Animal("Nyan", "cat")
   # print(cat)
    bird = Animal("X", "bird")
   # print(bird)
    
    print()
    print("=================================")
    print()
    
    res = Daycare([dog, cat, bird])
    res2 = Daycare([dog, bird])
    print(res)
    print(res2)
    
    print()
    print("=================================")
    print()

    n = Neighborhood([res, res2])
    print(n)
    del n

    print()
    print("=================================")
    print()

    r = RSPCA([dog, cat, bird])
    print(r)

if __name__ == "__main__":
    main()
