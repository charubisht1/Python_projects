# Class for personal information
class Personal_info:
    # Define __init__ function that creates below attributes
    def __init__(self, name, address, age, p_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__p_number = p_number

    # Create mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__name = address

    def set_age(self, age):
        self.__age = age

    def set_p_number(self, p_number):
        self.__p_number = p_number

    # Create accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_p_number(self):
        return self.__p_number

    # Create __str__ function to print in a specific format
    def __str__(self):
        return 'Name :' + self.__name + '\n' + 'Address :' + self.__address + '\n' + 'Age :' + self.__age + \
               '\n' + 'Phone number: ' + self.__p_number
