import random
import string

#password generation
def generate_password(length: int = 16):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

#Displays password in terminal
password = generate_password()
print(f"Generated Password: {password}")
