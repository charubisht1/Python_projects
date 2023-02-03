# Importing class Team and required packages
from Team import Team
from datetime import date
from itertools import count
import sys
class create_menu:

    def __init__(self):
        pass
    def run():
        # Create number sequence from 0 and goes like 0, 1, 2...
        t_id = (count(start=0, step=1))
        # Define empty dictionary and list to store team data
        team_dict = {}
        team_temp = []
        # Provide menu to the user
        print("CHOOSE FROM THE MENU")
        print(" ")
        print("TO CREATE A TEAM : 0 \nTO READ TEAM DETAILS : 1 \nTO UPDATE TEAM RECORDS : 2")
        print("TO DELETE TEAM RECORD : 3 \nTO SEE NUMBER OF EXISTING TEAMS AND PERCENTAGE OF TEAMS WHICH PAID THE FEES : 4 ")
        print("TO CANCEL A TEAM PARTICIPTAION : 5 \nTO SAVE YOUR INFORMATION TO A TEXT FILE : 6")
        print("TO RETRIEVE INFORMATION FROM THE TEXT FILE : 7 \nTO EXIT THE PROGRAM : 8")
        print(" ")
        print(" ")

        while True:
            # print("Choose from menu options 0: Create, 1: Read, 2: Update, 3: Delete")
            # print("4: Info about existing team and percentage of teams which paid fees, 5: Cancel participation")
            # print("6: Save, 7: Load data from text file, 8: Exit")
            # print(" ")

            # Take user input for menu option
            menu_op = int(input("You are at the main menu. Choose your option : "))
            # TO CREATE A TEAM
            if menu_op == 0:
                print(" ")
                print(" LETS CREATE A TEAM! ")
                # User does not require to enter id, registration date, cancellation date
                # Taking user input for remaining parameters
                for i in t_id:
                    t_date = date.today()
                    t_name = input("Enter name :")
                    t_type = input("Enter team type girls/boys: ")
                    fee_paid = bool(int(input("Is your fee paid? 1 for yes 0 for no :")))
                    fee_amount = int(input("Enter your fee amount: "))
                    cancellation_date = "null"
                    # Creating instance of class Team
                    team_instance = Team(i, t_date, t_name, t_type, fee_paid, fee_amount, cancellation_date)
                    # Storing team details to an empty list, appending list for each iteration
                    team_temp.append(team_instance)

                    # Prompt user if they want to return to the main menu or continue creating team
                    prog_leave = int(input("Press 1 to return to the main menu. To continue creating team press 0 : "))
                    if prog_leave == 1:
                        for j in range(len(team_temp)):
                            # Transfering team details from list to the empty dictionary.
                            # Each element of list is a value in a dictionary.
                            team_dict[j] = team_temp[j]
                        break
                    else:
                        continue

            # TO READ TEAM DETAILS
            elif menu_op == 1:
                print(" ")
                print("READING TEAM DETAILS")
                print("To print details of all teams, PRESS 1 \nTo print details of individual teams, PRESS 2")
                print("To print details of teams by category, PRESS 3")
                read_teams = int(input("Please provide your input : "))
                print('-' * 45)
                if read_teams == 1:
                    # Reading all items from the dictionary
                    for key, value in team_dict.items():
                        print(value)
                        print('-' * 45)
                    print(" ")
                    print(" ")
                # Reading items from the dictionary using key
                elif read_teams == 2:
                    print(" ")
                    for key, value in team_dict.items():
                        print(key)
                    read_id = int(input("From above, enter which id you want to read:"))
                    print('-' * 45)
                    print(team_dict[read_id])
                    print('-' * 45)
                    print(" ")
                    print(" ")

                # Use get_t_type method of class Team to compare team type to user input
                # if values are equal print team details
                elif read_teams == 3:
                    print(" ")
                    category_type = input(" Print girls team or boys team:")
                    print('-' * 45)
                    for key, value in team_dict.items():
                        if value.get_t_type() == category_type:
                            print(key, value)
                            print('-' * 45)
                    print(" ")
                    print(" ")

            # TO UPDATE TEAM RECORDS
            elif menu_op == 2:
                print(" ")
                print("Listing the records! Print record that you you want to update : ")
                for key, value in team_dict.items():
                    print(value)
                    print(" ")
                update_val = int(input("Enter id you want to update:"))
                print("Enter values to update : ")
                print('-' * 45)
                t_name_new = input("Enter name : ")
                t_type_new = input("Enter team type girls/boys : ")
                fee_paid_new = bool(int(input("Is your fee paid? 1 for yes, 0 for no : ")))
                fee_amount_new = int(input("Enter your fee amount : "))
                # Referencing mutator methods of class Team to update new values
                team_dict[update_val].set_name(t_name_new)
                team_dict[update_val].set_t_type(t_type_new)
                team_dict[update_val].set_fee_paid(fee_paid_new)
                team_dict[update_val].set_fee_amount(fee_amount_new)
                print("Your data has been updated! Here are your updated values : ")
                print(" ")
                print(team_dict[update_val])
                print('-' * 45)

            # TO DELETE TEAM RECORDS
            elif menu_op == 3:
                print(" ")
                print("Listing the records! Print record that you you want to delete")
                for key, value in team_dict.items():
                    print(key)
                print(" ")
                print(" ")
                pick_id = int(input("Enter the id you want to delete : "))
                team_dict.pop(pick_id, 'OOPS! Entry not found')
                print(" Team Deleted Successfully! ")
                print(" ")

            # TO SEE HOW MANY TEAMS EXIST IN THE MOMENT
            # TO SEE PERCENTAGE OF TEAMS WHICH PAID THE FEES
            elif menu_op == 4:
                print(" ")
                total_team = len(team_dict)
                counter = 0
                for key, value in team_dict.items():
                    if value.get_fee_paid() == 1:
                        counter = counter + 1
                team_fee_paid_per = (counter / total_team) * 100
                print("Total number of teams at the moment is :", total_team)
                print('-' * 45)
                # formatting output in '50.00%' format
                print("Percentage of teams that have paid the fee is ", '{:.2f}%'.format(team_fee_paid_per))

                print(" ")
                print(" ")

            # TO CANCEL PARTICIPATION
            elif menu_op == 5:
                print(" ")
                print("Listing team records! Pick the record you want to cancel participation for :")
                for key, value in team_dict.items():
                    print(key)
                id_cancel = int(input("Enter which id you want to cancel :"))
                team_cancel = input("Are you sure you want to cancel? press 'y' for yes and 'n' for no : ")
                if team_cancel == 'y':
                    print(" ")
                    print("Your team is cancelled.")
                    print(" ")

                    # Using mutator method of class Team to update cancellation date
                    # from default value "null" to current date
                    team_dict[id_cancel].set_cancellation_date(date.today())

            # TO SAVE INFORMATION TO A TEXT FILE
            elif menu_op == 6:
                print("Saving data to text file")
                # Opening file in append mode
                team_info = open('team_info.txt', 'a')
                for key, value in team_dict.items():
                    # Writing the text file from the dictionary
                    team_info.write(str(value) + '\n')
                # Closing file
                team_info.close()

            # TO RETRIEVE INFORMATION FROM THE TEXT FILE
            elif menu_op == 7:
                print("Loading the data....")
                print(" ")
                print(" ")
                # Opening file in read mode
                team_info = open('team_info.txt', 'r')
                print(team_info.read())
                print('-' * 45)
                # Closing file
                team_info.close()
                print(" ")
                print(" ")

            # TO EXIT THE PROGRAM
            elif menu_op == 8:
                print(" ")
                sys.exit(" You have chosen to exit! Bye! ")

