# Tricks

squares = []
for x in range(1,11):
    squares.append(x*x)

print(squares)


sq = [ x*x for x in range(1,11)]
print(sq)

# Cubes of odd numbers
odd_cubes = [ x*x*x for x in range(1,11) if x%2!=0]
print(odd_cubes)

# save in a list, all vowels in a word.
vow = [ch.upper() for ch in "babablacksheephaveyouanywool" if ch in 'aieou']
print(vow)
