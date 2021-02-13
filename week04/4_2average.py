# Asks user to enter numbers until they enter 0, and the output is a list of the entered numbers and their average
# Author: Andrew Scott

# An empty list that will contain whatever numbers are entered by the user
numbers = []

# A variable that will store the number entered by the user
number = int(input("Enter number (enter 0 to quit): "))

# A loop that adds the user's number to the previously created list, and conyinues to ask users to enter numbers 
# which will be added to the list util the user enters 0 to end the loop
while number != 0:
    numbers.append(number)

    number = int(input("Enter another number (enter 0 to quit): "))

# A loop that will print each number that was added to the list
for value in numbers:
    print (value)

# Calculates the average number of the user's numbers by adding them all then dividing the sum by the amount of numbers entered
average = float(sum(numbers)) / len(numbers)
print("The average is {}".format(average))