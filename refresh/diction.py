# Dictionaries in 3.6

rollbook = {"nev":27 ,"dan":47, "nik":50, "dav":50}

print(rollbook.keys())
print(rollbook.values())
print(rollbook.items())

print("Nev number: ",rollbook.get("nev"))
print(rollbook)
print(" # belongs to ", rollbook.get("rock", "VIP"))

l = ["my", "name", "is", "duder", "duder"]
b = {0}
for w in l:
    #print(w)
    b.add(w)  #add to a Set
print(b)

score = int(input("Enter score: "))
if score >= 90:
    print("A")
elif score >= 75 and score <= 90:
    print("B")
elif score >= 60 and score <= 75:
    print("C")
else:
    print("Did not qualify.")
