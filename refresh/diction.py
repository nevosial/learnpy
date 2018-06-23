# Dictionaries in 3.6

rollbook = {"nev":27 ,"dan":47, "nik":50, "dav":50}

print(rollbook.keys())
print(rollbook.values())
print(rollbook.items())

print("Nev number: ",rollbook.get("nev"))
print(rollbook)
print(" # belongs to ", rollbook.get(47))
