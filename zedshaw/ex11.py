#User inputs
# end allows cursor to be on same line.

print("===Employee Enrollment form===")
print("Enter your First name: ", end='')
fname = input()
print("Enter your Last name: ",end='')
lname = input()
print("Enter your age: ",end='')
age = input()
print("Enter your gender(M/F): ",end='')
gender = input()

print(f"""
====Your details====
Name: {fname} {lname}
Age: {age}
Gender: {gender}
""")

print("==============")
