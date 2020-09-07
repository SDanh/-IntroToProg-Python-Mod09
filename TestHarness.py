# ------------------------------------------------------------------------ #
# Title: TestHarness
# Description: Test Harness for Assignment 09

# ChangeLog (Who,When,What):
# SDanh,9.5.2020,File Created. Implemented Person & Employee tests.
# SDanh,9.6.2020,File Created. Implemented File Processor & IO tests.
# ------------------------------------------------------------------------ #

import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IOC

#------Person Class Test------
print("===PERSON CLASS===")
#creates Person object and prints contents
person1 = DC.Person('John', 'Smith')
print(person1)
print(person1.first_name)
print(person1.last_name)
print(person1.to_string())

#------Employee Class Test------
print("===EMPLOYEE CLASS===")
#creates Employee objects and prints contents
person2A = DC.Employee(123,'Jane','Doe')
print(person2A.employee_id)
print(person2A.first_name)
print(person2A.last_name)
print(person2A.to_string())

person2B = DC.Employee(456,'Jim','Joe')
print(person2B.employee_id)
print(person2B.first_name)
print(person2B.last_name)
print(person2B.to_string())

print("\n")

#------FileProcessor Class Test------
print("===FILE PROCESSOR===")

#Test Data File
test_data_file_name = "TestData.txt"

#Uses previously created Employee objects and adds to list
test_list = []
test_list2 = []
test_list.append(person2A)
test_list.append(person2B)
print(test_list2)

#uses list to read and write to test file.
processor = PC.FileProcessor()
processor.save_data_to_file(test_data_file_name, test_list)

test_list2 = processor.read_data_from_file(test_data_file_name)
print(test_list2)
for entry in test_list2:
    print(str(entry[0]) + " " + str(entry[1]) + " " + str(entry[2].strip("\n")))

print("\n")

#------EmployeeIO Class Test------
print("===EMPLOYEE IO===")
testIO = IOC.EmployeeIO()

#prints menu items
testIO.print_menu_items()

#prints menu options
print(testIO.input_menu_options())

#test for printing list of items using function
test_list3 = []
person3 = DC.Employee(111,'AAA','BBB')
person4 = DC.Employee(222,'CCC','DDD')
test_list3.append(person3)
test_list3.append(person4)
testIO.print_current_list_items(test_list3)

#test for creating new employee objects using function
person5 = testIO.input_employee_data()
print(person5.employee_id)
print(person5.first_name)
print(person5.last_name)
print(person5.to_string())

