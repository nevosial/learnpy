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
