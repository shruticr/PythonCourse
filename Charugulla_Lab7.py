# Shruti Ratna Charugulla
# Program Status: Complete
# This program program allows the user to enter the rainfall statistics for 12 months into a list.
# The program calculates the total rainfall for the year, the average rainfall for the year and the
# months with the highest and lowest rainfall.


def main():

    # Create a list of months in an year.
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    # Create an empty list
    rainfall_amounts = []
    # Initialize the accumulator
    total = 0

    # Get the rainfall amounts for all the 12 months.
    for month in months:
        rain = int(input('Enter the rainfall for ' + month + ': '))
        # Create an input validation
        while rain < 0:
            print('Please enter a valid positive number.')
            rain = int(input('Enter the rainfall for ' + month + ': '))
            continue
        # Append the rainfall amounts to the empty list
        rainfall_amounts.append(rain)
        # Calculate the total rainfall
        total += rain

    print('Total Rainfall: ', total)
    # Calculate the average rainfall
    print('Average Rainfall: ', format(total /len(months), ',.2f'))

    # Find the index of the lowest rainfall amount and get the month name at the same index
    max_index = rainfall_amounts.index(max(rainfall_amounts))
    print('Highest Rainfall: ', months[max_index])
    # Find the index of the lowest rainfall amount and get the month name at the same index
    min_index = rainfall_amounts.index(min(rainfall_amounts))
    print('Lowest Rainfall: ', months[min_index])

# Call the function and add the try/except handling
try:
    main()
except ValueError:
    print('Please enter a valid integer')
    




