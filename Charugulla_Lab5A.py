# Shruti Ratna Charugulla
# Program Status: Complete
# This program asks to input 5 test scores in the range 1 - 100 and calculates the average
# displaying the letter grade.


# this function inputs the 5 test scores
def main():
# Initialize a variable to store numeric average
    numeric_average = 0.0
# Loop from 1 to 5 to accept user input of 5 numeric scores, each of which is in the range 1-100
    for i in range(1,6):
        numeric_score = input('Enter score #' + str(i) + ' in range 1-100:')
        if float(numeric_score) < 0.0 or float(numeric_score) > 100.0:
            numeric_score = input('Error: Re-enter score #' + str(i) + ' in range 1-100:')
        numeric_average += float(numeric_score)
# Calculate average
    numeric_average = numeric_average/5
# Pass average to the function determine_grade to figure out the appropriate letter grade.
    determine_grade(numeric_average)

# This function takes in the average of all the scores and displays an appropriate letter grade.
def determine_grade(numeric_average):
    if numeric_average >= 90 and numeric_average <= 100:
        print('Your average is: ', format(numeric_average, '.2f'), ' which is an A')
    if numeric_average >= 80 and numeric_average <= 89:
        print('Your average is: ', format(numeric_average, '.2f'), ' which is a B')
    if numeric_average >= 70 and numeric_average <= 79:
        print('Your average is: ', format(numeric_average, '.2f'), ' which is a C')
    if numeric_average >= 60 and numeric_average <= 69:
        print('Your average is: ', format(numeric_average,'.2f'), ' which is a D')
    if numeric_average >= 0 and numeric_average <= 59:
        print('Your average is: ', format(numeric_average,'.2f'), ' which is a F')

# Call the main function
main()
