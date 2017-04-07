def main():
    if name == 'nev':
        print('Good choice')
    elif name == 'max':
        print('Can do better')
    elif name == 'Vic':
        print('Can do better')
    else:
        print('Try again')

#Python does not have a switch case.
#Strategy to use multiple choices in python using Dictionaries aka switch case :-)
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'bison'
    )
    name = 'three'
    print(choices.get(name, 'default'))
    #will print default if input is not in the dict.

#conditional expression.
    x, y = 0, 1
    if x > y:
        print('x is bigger than y')
    else:
        print('x is less than y')

        str =  ' this is true' if x > y else 'this is not true'
    print(str)

# the for loop in Python




if __name__== '__main__':main()
