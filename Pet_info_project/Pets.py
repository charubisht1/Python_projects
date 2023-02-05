# Class for pets
class Pets:
    # Define __init__ function that creates below attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Create mutator methods
    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Create accessor methods

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def __str__(self):
        return 'Name : ' + self.__name + '\n' + 'Pet type : ' + self.__animal_type + '\n' + 'Pet age: ' + self.__age


