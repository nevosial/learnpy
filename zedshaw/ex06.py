# Variables and Strings

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I said: \"{x}\"")
print(f"I also said:'{y}'")

hilarious = False
joke_eval = "Isn't that joke funny?! {}"
print(joke_eval.format(hilarious))

w = "left side"
e = "right side"
print(w+e)
