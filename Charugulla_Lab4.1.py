# Shruti Charugulla
# Program Status: Complete
# This program uses a while loop to displays and compares the budgeted amount
# with spent amount in the month.

# Create a named constant to input total budget for the month
BUDGET = float(input('Enter amount budgeted for the month: '))

# Create variable to control the loop
total = 1
expenses = 0

# Calculate the expenses in the month
# Print Budgeted amount and Spent amount
while total > 0:
    total = float(input('Enter an amount spent(0 to quit): '))
    expenses += total
print("Budgeted: $", BUDGET)
print("Spent: $", expenses)

# Create variables by comparing the expenses with the budget
over_budget = expenses - BUDGET
under_budget = BUDGET - expenses

# Determine and print the budget accordingly.
if expenses > BUDGET:
    print("You are $", format(over_budget, '.2f'),"over budget. PLAN BETTER NEXT TIME!")
elif expenses < BUDGET:
    print("You are $", format(under_budget, '.2f'),"under budget.")
elif expenses == BUDGET:
    print("You have met your budget exactly.")
