
import random
import string

# Simple function to generate a password
def generate_password(length):
    characters = string.ascii_letters + string.digits  # Letters (upper and lower) + numbers
    password = ''.join(random.choice(characters) for i in range(length))  # Randomly select characters
    return password

# Ask user for the password length
password_length = int(input("Enter the length of the password: "))

# Generate and display the password
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
