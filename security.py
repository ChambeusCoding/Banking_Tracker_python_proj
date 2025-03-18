import hashlib
import re
import json
from cryptography.fernet import Fernet
import base64

# Method to encrypt the password using SHA-256 hashing
def encrypt_password(password):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    # Hash the password
    sha256.update(password.encode('utf-8'))
    # Return the hexadecimal representation of the hashed password
    return sha256.hexdigest()

# Method to check password strength
def is_password_strong(password):
    # Password strength criteria: at least 8 characters, contains letters and numbers
    return len(password) >= 8 and bool(re.search(r'[a-zA-Z]', password)) and bool(re.search(r'\d', password))

# Method to simulate storing user's encrypted passwords (for example, in a database)
def get_correct_encrypted_password():
    return encrypt_password("PointBreak47!x")

# Method to generate a symmetric encryption key (Fernet key)
def generate_key(password):
    # Encrypt the password into a key using SHA-256
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    # Convert the hash to 32 bytes base64 encoded, this will be used for encryption
    key = base64.urlsafe_b64encode(sha256.digest())
    return key

# Method to encrypt the JSON data and save to a file
def encrypt_and_save_json(data, password, file_name):
    # Generate encryption key based on the password
    key = generate_key(password)
    fernet = Fernet(key)
    
    # Convert data to JSON string
    json_data = json.dumps(data)

    # Encrypt the JSON string
    encrypted_data = fernet.encrypt(json_data.encode())

    # Save the encrypted data to a file
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)
    print("Data encrypted and saved to file.")

# Method to decrypt the JSON data from a file
def decrypt_json(file_name, password):
    # Generate encryption key based on the password
    key = generate_key(password)
    fernet = Fernet(key)

    # Read the encrypted data from the file
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data).decode()

    # Convert the decrypted string back to a JSON object
    data = json.loads(decrypted_data)
    return data

# Main function to run the user authentication and encryption/decryption flow
def main():
    # Number of allowed attempts
    max_attempts = 3
    attempts_left = max_attempts

    # Correct encrypted password (in real scenarios, this would come from a database)
    correct_encrypted_password = get_correct_encrypted_password()

    # Ask for the password input from the user
    while attempts_left > 0:
        input_password = input("Password: ")

        # Check if the password is strong
        if not is_password_strong(input_password):
            print("Password is weak. It must contain at least 8 characters, including letters and numbers.")
            continue  # Skip this iteration and ask for a new password

        # Encrypt the input password and compare it with the correct encrypted password
        if encrypt_password(input_password) == correct_encrypted_password:
            print("Accessing WOPR...")
            print("Greetings Professor Falken, Shall we play a game? ")

            # Example JSON data
            data = {
                "income": [
                    {"amount": 2000, "date": "2025-03-01", "source": "Salary"}
                ],
                "expenses": [
                    {"amount": 500, "date": "2025-03-05", "category": "Rent", "description": "Monthly rent payment"}
                ]
            }

            # Encrypt and save the data to a file
            encrypt_and_save_json(data, input_password, 'encrypted_data.json')

            # Decrypt the data from the file
            decrypted_data = decrypt_json('encrypted_data.json', input_password)
            print("Decrypted Data:", decrypted_data)

            break  # Exit the loop if password is correct
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Incorrect password. You have {attempts_left} attempts left.")
            else:
                print("Incorrect password. No attempts left.")
                # Optionally, you can exit or lock the user out at this point

if __name__ == "__main__":
    main()
