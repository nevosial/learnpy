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

# the while loop in Python
names = ['Dan', 'Vic', 'Kew', 'Stan']
i = 0
while(i < len(names)):
    print(i)
    i += 1

# fibonaci numbers using while
    a, b = 0, 1
    while b < 50:
        #print(b, end=' ')
        print(b)
        a, b = b, a + b


# the for loop in Python
names = [1,2, 3, 4]
    for d in names:
        print(d)

# using the enumerator to get the index for our array/lists
    s = 'my name is Eric'
    for i, c in enumerate(s):
        print(i, c)
        if c == 'E' : print(' The index for E is {}'.format(i))

# using continue, break and else
    s = 'this is a string'
    for c in s:
        if c == 's' : continue
        print(c, end='')

    s = 'this is a string'
    for c in s:
        if c == 's' : break
        print(c, end='')


    s = 'this is a string'
    for c in s:
        print(c, end='')
    else:
        print('Else is used when the iterator has nothing more to iterate.')


# using continue statement
def main():
    s = 'Dan'
    p1 = 'abc123'
    while True:
        print('Please enter your name:')
        name = str(input());
        if name != s:
            continue
        print('Enter your code:')
        code = input()
        if code == p1:
            break;
        else:
            print('Please enter the correct name/code combination !')
    print('Hi {} Welcome to the vault...'.format(name))


if __name__== '__main__':main()
