#Sets in 3.6

p = {True, 3, 'nev', 4, 6, 7}
q = {False, True, 1,2,'vic', 'zoe',6, 7, 'nev'}

# union will return new set with all elements
r = p.union(q)
print(r)

# intersection will return only the common elements found in both
s = p.intersection(q)
print(s)

# difference will return only the uncommon elements found in both
t = p.difference(q)
print(t)

#issubset will return if subset of another
print(f"Is {p} subset of {q} :",p.issubset(q))

#adding item to the Set
p.add("False")
print(p)

#remove will take out an item from the Set.
p.remove("nev")
print(p)

#pop will remove arbitary element from the Set.
p.pop()
print(p)

# clear the Set with clear()
p.clear()
print(p, q)
