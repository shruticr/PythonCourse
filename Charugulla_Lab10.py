# Shruti Ratna Charugulla
# Program Status: Complete
# Design a class named Employee that holds the employee details: name, ID number, department and job title.
# This program gets information from the user and passes it as parameters to the initializer method. It creates
# 3 instances of the class. And it displays the information of the three individuals.


# import class from employee.py
from employee import Employee

def main():

    # Create an empty list
    employee_list = []

    # Assign a variable for number of entries
    numEntries = 4

    # Create a for loop for the user to enter the details of 3 employees
    for count in range(1, numEntries):
        emp_name = input('Enter employee name: ')
        emp_ID = input('Enter employee ID: ')
        emp_dept = input('Enter department: ')
        emp_title = input('Enter position: ')
        print()

        # Create Employee objects for the attributes
        detail = Employee(emp_name, emp_ID, emp_dept, emp_title)

        # Add the employee details to the list
        employee_list.append(detail)

    # Create a for loop to print the entered employee details from the list
    for count in range(0, numEntries-1):
        print()
        print('Employee ', str(count+1), ': ')
        print(employee_list[count])

# Call the main function
main()



