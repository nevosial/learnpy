#Strings

s = "neville"
width = 10
fillchar = '*'

print(id(s))

#Center adjust the string in given width
print(s.center(width))

#Left adjust the string in given width
print(s.ljust(width))

#right adjust the string in given width
print(s.rjust(width))

#Center adjust the string in given width and fill the remaining space.
print(s.center(width, fillchar))

#Left adjust the string in given width and fill the remaining space
print(s.ljust(width, fillchar))

#right adjust the string in given width and fill the remaining space
print(s.rjust(width, fillchar))


#Count occurences
print(s.count('l'))

#uppercase
print(s.upper())

#lowercase
print(s.lower())

print(len(s))

#find first occurence in item
print(s.find('l'))

#split the string
print(s.split('i'))
