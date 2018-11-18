# Shruti Ratna Charugulla
# Program Status: Complete
# This program reads a string from the user containing a date in the form mm/dd/yyyy.
# And it prints the date in the format March 12, 2018.


def main():

    # Get the date from the user in the format mm/dd/yyyy
    date = input('Enter a date in the format mm/dd/yyyy: ')
    # Split the date
    date_list = date.split('/')
    # Determine the name of the month accordingly and print the date
    if date_list == '01':
        print('January', date_list[1], ',', date_list[2])
    elif date_list[0] == '02':
        print('February', date_list[1], ',', date_list[2])
    elif date_list[0] == '03':
        print('March', date_list[1], ',', date_list[2])
    elif date_list[0] == '04':
        print('April', date_list[1], ',', date_list[2])
    elif date_list[0] == '05':
        print('May', date_list[1], ',', date_list[2])
    elif date_list[0] == '06':
        print('June', date_list[1], ',', date_list[2])
    elif date_list[0] == '07':
        print('July', date_list[1], ',', date_list[2])
    elif date_list[0] == '08':
        print('August', date_list[1], ',', date_list[2])
    elif date_list[0] == '09':
        print('September', date_list[1], ',', date_list[2])
    elif date_list[0] == '10':
        print('October', date_list[1], ',', date_list[2])
    elif date_list[0] == '11':
        print('November', date_list[1], ',', date_list[2])
    elif date_list[0] == '12':
        print('December', date_list[1], ',', date_list[2])

# Call the main function
main()

