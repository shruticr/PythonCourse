#Shruti Ratna Charugulla
# Program Status: Complete
# This program uses a loop to ask the user for the horses’ names and amount won for the day



def main():
    # Get the number of breeds
    horses_race = int(input('How many breeds of horses do you want in the text file: '))
    # Open a file to write
    output = open('race.txt', 'w')
    
    # Create a for loop to enter the horses names and amounts won
    for count in range(1, horses_race + 1):
        horse_name = input('Horse name #' + str(count) + ': ')
        amounts_won = input('How much did the horse #' + str(count) + 'win: ')
        output.write(horse_name + '\n')
        output.write(amounts_won + '\n')

    output.close()

# add try/except handling
try:
    main()
except IOError:
    print('The file race.txt could not be created.')
except ValueError:
    print('The given value is not valid.')
finally:
    pass
