#input and argv
from sys import argv
script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("Can you quickly answer the following questions.")

print(f"{user_name}, Do you like apples?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"""
{user_name} said {likes} for apples
and lives in {lives}.
""")
