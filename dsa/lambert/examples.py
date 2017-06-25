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
    
    
#Function with variable number of arguments
#Here args is the list that is passed to the function.
#sometimes called as unpacker.
def multi(*args):
    result = 0;
    for i in args:
        result = result + i;
    return result;

#print(multi(1, 2, 3))
