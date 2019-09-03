# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:  # if the number divided by two and has no remainder... return true
        return True
    else:  # else return false
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if (num % 2 == 0):
    print('Even')
else:
    print('Odd')
