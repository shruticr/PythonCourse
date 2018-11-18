# Shruti Charugulla
# Program Status: Complete
# This program calculates the discount amount and the total amount
# when user enters the quantity of packages purchased

# Create named constant for the original price
ORIGINAL_PRICE = 99

# Get the user's number of packages
userQuantity = int(input('Enter the number of packages purchased: '))

# Calculate the discount amount for each quantity range
discount10to19 = ORIGINAL_PRICE * userQuantity * 0.1
discount20to49 = ORIGINAL_PRICE * userQuantity * 0.2
discount50to99 = ORIGINAL_PRICE * userQuantity * 0.3
discountAbove100 = ORIGINAL_PRICE * userQuantity * 0.4

# Create named constants and Calculate the total amount for each quantity range
TOTAL_10 = (ORIGINAL_PRICE * userQuantity) - discount10to19
TOTAL_20 = (ORIGINAL_PRICE * userQuantity) - discount20to49
TOTAL_30 = (ORIGINAL_PRICE * userQuantity) - discount50to99
TOTAL_40 =(ORIGINAL_PRICE * userQuantity) - discountAbove100

# Determine and print both the discount amount and total amount
if userQuantity >= 10 and userQuantity <= 19:
    print('Discount Amount: $', format(discount10to19, ".2f"))
    print('Total Amount: $', format(TOTAL_10, ".2f"))
elif userQuantity >= 20 and userQuantity <= 49:
    print('Discount Amount: $', format(discount20to49, ".2f"))
    print('Total Amount: $', format(TOTAL_20, ".2f"))
elif userQuantity >= 50 and userQuantity <= 99:
    print('Discount Amount: $', format(discount50to99, ".2f"))
    print('Total Amount: $', format(TOTAL_30, ".2f"))
elif userQuantity >= 100:
    print('Discount Amount: $', format(discountAbove100, ".2f"))
    print('Total Amount: $', format(TOTAL_40, ".2f"))
else:
    print('Please enter a valid positive integer')
