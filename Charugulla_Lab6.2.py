# Shruti Ratna Charugulla
# Program Status: Complete
# This program to read all the records from the file
# created in the first program, display them and calculate the total and average purse.

def main():
    # Open a file 
    horses_file = open('race.txt', 'r')
    # Read the first line
    name = horses_file.readline()
    print('Today\'s Winnings at Belmont Park')
    print('-----------------------------------')
    # Initialize variables
    total = 0.0
    count = 0
    while name != '':
        # Read value from the file
        purse = float(horses_file.readline())
        count = count + 1
        # Compute the total purse
        total = total + purse
        name = name.rstrip('\n')
        print('Horse: ', name)
        print('Purse:  $ ', format(purse,',.2f'), sep= '')
        name = horses_file.readline()
    print('The total purse for the day is:  $', format(total, ',.2f'))
    print('The average purse for the day is:  $', format(total/count, ',.2f'))

    horses_file.close()
    
# Add try/except handling
try:
    main()
except IOError:
    print('This file race.txt does not exist.')
except ValueError:
    print('The value that you are trying to read is invalid.')
except:
    print('The file race.txt could not be read.')
finally:
    pass


