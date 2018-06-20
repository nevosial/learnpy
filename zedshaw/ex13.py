#Unpacker and argv
from sys import argv



#unpack the args
script, first, second, third, fourth = argv

fourth = input("Enter your arg")

print("The script is called ",script)
print("The first arg is ", first)
print("The second arg is ", second)
print("The third arg is ", third)
print("This is from user: ",fourth)
