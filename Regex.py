# re module is the Python regular expression module.

import re

#Searching method
re.search()
# Search and replace method
re.sub()
# Pre compile the regex
re.compile()

#ignore cases
re.IGNORECASE

# Exception Handling in Python
def main():
    #example of a IO error
    try:
        fh = open('lines.txt')
        for line in fh: print(line , end='')
    except IOError as e:
        print('Could not open file:' , e)

    #example for a ValueError
    try:
        print('Enter a numerical value')
        numb = int(input())
        if numb % 2 == 0:
            print("Number is an even number")
        else:
            print('Number is an odd number')


    except ValueError as e:
        print('Please enter an integer value. System error :{}'.format(e))

if __name__ == "__main__": main()

#Exceptions can also be raised using the raise
