# Shruti Ratna Charugulla
# Program Status: Complete
# This program reads the file’s contents and determines the following:
# The number of uppercase letters in the file
# The number of lowercase letters in the file
# The number of digits in the file
# The number of whitespace characters in the file

def main():
    
    # Initialize the counts
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    whitespace_count = 0
    # Open the file in read mode
    infile = open('text.txt', 'r')
    # Read the contents in the file
    lines = infile.read()

    # Create a for loop to read the characters in the lines 
    # and calculate the number of different counts
    for ch in lines:
        if ch.isupper():
            uppercase_count += 1
        elif ch.islower():
            lowercase_count +=1
        elif ch.isdigit():
            digit_count += 1
        elif ch.isspace():
            whitespace_count += 1
    
    # Print the counts
    print('Uppercase letters: ', uppercase_count)
    print('Lowercase letters: ', lowercase_count)
    print('Digits: ', digit_count)
    print('Spaces: ', whitespace_count)

# Call the function
main()

