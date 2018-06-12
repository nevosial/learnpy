#Multiple lines spacess
#escape characters, tabbed spaces.

x =10
print(f"my net worth is {x} million right now.")
print("The table weighs",x,"pounds.")
s = "value="+str(x)+" pounds."
print(s)

p = "value="+repr(x)+" pounds."
print(p)

print("I\'m the man of the earth")
print("Here is the man of the earth.")
print("""There are many of them and in ascending order:
\t 1. Adam
\t 2. Elijah
\t 3. Abel
""")

print("""
Escape sequences:
Backslash \\
Single quote `
Double quote \"
Linefeed \\n
Carriage return \\r
Vertical tab \\v
Horizantal tab \\t
""")
