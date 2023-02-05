# # Exercise 1
# # import class Personal_info
# import Personal_info
# # Create 3 instances of the class as per the requirement (will use mutator method)
# my_info = Personal_info.Personal_info("Charu", "Sweden", "25", "9711488546")
# friend_info = Personal_info.Personal_info("Anuj", "India", "26", "9711359117")
# family_info = Personal_info.Personal_info("Manik", "India", "53", "9971139542")
#
# # Create list to store Personal_info class objects
# my_list = [my_info, friend_info, family_info]
#
# print(100*'*')
# print("The program prints personal information for myself, friends and family respectively.")
# print(100*'*')
#
# # Create loop to iterate through the list
# for i in my_list:
#     # call class methods to print Personal info details (will use accessor method)
#     print(i)
#
#     print(35*'-')

# Exercise 2
#
# ask user how many pets that should be entered
#  enter data about each pet
#  create object for each pet entered
#  the data about each pet should be stored as the object’s attributes
# o use i.e. set-methods in the class
#  store each pet-object created in a “list”
#  let the user have an option to choose if
# o all pet’s should be listed or
# o just all pets of a certain type
#  use a loop to go through, iterate, the list and display the requested data
# according to the option chosen by user, all or just specific type of pets.

# Import class Pets
import Pets

print(" This program asks you to enter you pet details and gives you")
print("an option to view all pets together or only a certain type. ")
print(25 * '-')

# Ask user how many pets that should be entered
n = int(input("Enter number of pets :"))
# My_list stores each pet-object created
my_list = []
for i in range(0, n):
    print(" Enter input for Pet ", i + 1)
    a = input("Enter your pet's name :")
    b = input("Enter your pet type: ")
    c = input("Enter your pet's age: ")
    print(30 * '-')
    # Create a new name for every pet object entered
    new_obj = '{:_<4}'.format('pet') + str(i)
    # Store the data about each pet as the object’s attributes
    new_obj = Pets.Pets(a, b, c)
    # Append list with each iteration (contain class objects)
    my_list.append(new_obj)

print("Thankyou for your input!")

# function for finding unique pet type values
# create empty list to pet type
pet_list = []


def pet_unique(pet_list):
    for i in my_list:
        # calling class method to get pet type
        pet = i.get_animal_type()
        pet_list.append(pet)
    # select unique values from pet_list    remove list
    unique_val = set(pet_list)
    # returning unique pet type
    return unique_val


print("Printing pet details now")

# Options chosen by user, all or just specific type of pets
result = input("Write 'all' to see all the pets. To view all pets of a certain type press 's' : ")

# Printing the pet details
# print for all pets
if result == "all":
    for i in my_list:
        # call __str__ function from Pet class
        print(i)
# print for specific pet type
elif result == "s":
    print(" Choose pet category from below: ")
    # calling function pet_unique for user to choose a specific type of pet
    print(pet_unique(pet_list))
    my_pet = input("Enter your pet: ")
    for i in my_list:
        # Print if pet type is same as user input
        if i.get_animal_type() == my_pet:
            print(i)
