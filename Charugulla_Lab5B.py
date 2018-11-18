# Shruti Ratna Charugulla
# Program Status: Complete
# This program will determine the distance the object
# falls in a specific time period.
# The conversion formula is: d = 1/2*g*t^2

import distance

def main():
    print('Time \t Falling Distance')
    print('..........................')
    for time in range(1, 11):
        distance_b = distance.falling_distance(time)
        print(time, '\t\t', format(distance_b, '.2f'))

main()
