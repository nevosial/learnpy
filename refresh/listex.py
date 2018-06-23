mylist = [1,2,3,4,6,7,8,9,10]
a = mylist
#print(mylist)
b= mylist * 2
c = [mylist]* 3
# print(b)
# print(c)
# print(len(mylist))
# print(mylist[2:8])


print(a)
a.append(11)
print(a)

a.insert(15, 65)
print(a)

print(a.pop())
print(a.pop(0))

a.sort()
print(a)
a.reverse()
print(a)

a.sort()
del a[7]
print(a)

print(a.index(9))
a.insert(10, True)
print(a)
a.sort()
print(a)
print("==")
b = a * 2
print(b)
print(b.count(True))
b.remove(True)
print(b)



'''
mylist = [1,2,3,4,6,7,8,9,10]
a = mylist
#print(mylist)
b= mylist * 2
c = [mylist]* 3
# print(b)
# print(c)
# print(len(mylist))
# print(mylist[2:8])


print(a)
a.append(11)
print(a)

a.insert(15, 65)
print(a)

print(a.pop())
print(a.pop(0))

a.sort()
print(a)
a.reverse()
print(a)

a.sort()
del a[7]
print(a)

print(a.index(9))
a.insert(10, True)
print(a)
a.sort()
print(a)
print("==")
b = a * 2
print(b)
print(b.count(True))
b.remove(True)
print(b)
'''
