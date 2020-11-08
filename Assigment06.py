# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a Python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# RAyeni,11.4.2020,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            list_of_rows.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows, 'Success'
        except:
            print()


    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to dictionary, then adds dictionary to list """

        # add task and priority to dictionary and assign to row
        row = {"Task": task.strip().capitalize(), "Priority": priority.strip().capitalize()}
        # append dict to list_of_rows
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Receives task and lists of tasks (dicts).  Removes task from list.
            Returns updated list.
        """
        status = ""  # Returns confirmation of success or failure in removing task
        i = 0  # list index
        # for loop to check if task exists.  If exists, delete it. Else, notify user.
        for row in list_of_rows:
            if list_of_rows[i]["Task"] == task:
                del list_of_rows[i]
                status = 'Success'
            else:
                status = "Failed: please check spelling or if task exist."
            i += 1
        return list_of_rows, status

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Function receives name of file and list of tasks (dicts).
            Writes list elements to file.  Returns list and message.
        """
        # opens file strFileName
        objFile = open(strFileName, "w")
        # for each row/dict in the table, write the values to the file
        for row in lstTable:
            objFile.write(row.get("Task") + "," + row.get("Priority") + "\n")
        objFile.close()  # close the file
        return list_of_rows, 'Data saved'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Ask user for task and its priority.
            Returns task and priority to main part of script
        """
        task = input("Enter Task: ")
        priority = input("Enter Priority (High, Medium, Low): ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Ask user for task to remove.
            Returns task to main part of script.
        """
        task = input("Enter Task to Remove: ")
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # Call input function, capture return in variables for task and priority
        strTask, strPriority = IO.input_new_task_and_priority()
        # Call function to add data to list, capture return in vars for table and status
        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        # Call function request input to continue
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # Call functions to receive task to remove, remove task, and receive input to continue
        strTask = IO.input_task_to_remove()
        lstTable, strStatus = Processor.remove_data_from_list(strTask.strip().capitalize(), lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # Call functions to write data to file, and receive input to continue.
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:  # Notify user Save operation was canceled.
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # Call functions to read data from file, and receive input to continue
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break   # and Exit
