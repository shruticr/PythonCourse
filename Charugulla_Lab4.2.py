# Shruti Charugulla
# Program Status: Complete
# This program uses a loop to display a table
# showing the years 1 through 25 and the rise in water level
# for every year.

# Print the table headings
print('Year\t\tRise (in millimeters)')
print('-------------------------------------')

# Print the years 1 through 25 and the corresponding
# rise in water level by 1.8 every year.
LEVEL = 0

for number in range(1, 26):
    LEVEL += 1.8
    print(number, '\t','\t', format(LEVEL,'.2f'))
