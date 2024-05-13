import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))

    password = generate_password(length)

    print("Generated Password:", password)
