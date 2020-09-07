# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# SDanh,9.6.2020,Implemented Assignment 9 Main.py
# ------------------------------------------------------------------------ #
# TODO: Import Modules
import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IOC

strFileName = "EmployeeData.txt"
lst_of_Employees = []

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
myProcessor = PC.FileProcessor()
myIO = IOC.EmployeeIO()

# Load data from file into a list of employee objects when script starts
try:
    raw_data = myProcessor.read_data_from_file(strFileName)
    for entry in raw_data:
        print(entry[0] + " " + entry[1] + " " + entry[2].strip("\n"))
        intID = int(entry[0])
        strFirst_Name = entry[1]
        strLast_Name = entry[2].strip("\n")
        new_employee = DC.Employee(intID, strFirst_Name, strLast_Name)
        lst_of_Employees.append(new_employee)
except FileNotFoundError:
    print("YOUR FILE WAS NOT FOUND!!")

while True:
# Show user a menu of options
    myIO.print_menu_items()
# Get user's menu option choice
    intChoice = myIO.input_menu_options()
    # Show user current data in the list of employee objects
    if intChoice == '1':
        print("Print")
        myIO.print_current_list_items(lst_of_Employees)
        continue
    # Let user add data to the list of employee objects
    elif intChoice == '2':
        print("Adding")
        try:
            new_employee = myIO.input_employee_data()
            lst_of_Employees.append(new_employee)
        except UnboundLocalError:
            print("Cannot make Employee Entry!")
        continue
    # let user save current data to file
    elif intChoice == '3':
        print("Save")
        myProcessor.save_data_to_file(strFileName, lst_of_Employees)
        continue
    # Let user exit program
    elif intChoice == '4':
        print("Exit")
        break
    else:
        print("INPUT MUST BE [1-4]")

# Main Body of Script  ---------------------------------------------------- #
