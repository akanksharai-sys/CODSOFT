 # Password Generator Application
import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    # Base characters: letters
    characters = string.ascii_letters
    
    # Add digits if enabled
    if use_digits:
        characters += string.digits
    
    # Add special characters if enabled
    if use_special:
        characters += string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input, using default length 12.")
        length = 12
    
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_digits, use_special)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()