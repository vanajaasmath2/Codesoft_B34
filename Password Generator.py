import random
import string

def generate_password(length):
    # Define the characters you want to include
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    # Ask the user for desired password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
