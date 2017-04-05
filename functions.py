
def myFun():
    print ("Welcome to my function")

myFun()

def cube(x):
    return(x*x*x)

#cube(3)

#print(cube(3))

def power(a, b):
    return pow(a, b)

#print(power(2, 3))

#Function with default args
def pwr(num , x=1):
    result = 1;
    for i in range(x):
        result = result * num;
    return result;

#print(pwr(2, 4))
#print (pwr(x=4, num = 2))

#Function with variable number of arguments
#Here args is the list that is passed to the function.
def multi(*args):
    result = 0;
    for i in args:
        result = result + i;
    return result;

print(multi(1, 2, 3))
