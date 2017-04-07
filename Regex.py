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
    try:
        fh = open('lines.txt')
        for line in fh: print(line , end='')
    except IOError as e:
        print('Could not open file:' , e)

if __name__ == "__main__": main()

#Exceptions can also be raised using the raise.
