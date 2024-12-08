import random

# Function to generate keys
def generate_keys(prime):
    g = random.randint(2, prime - 1)  # Choose a random generator
    x = random.randint(2, prime - 2)  # Private key
    h = pow(g, x, prime)  # Public key component
    return (prime, g, h), x

# Function to encrypt a message
def encrypt(public_key, message):
    prime, g, h = public_key
    k = random.randint(2, prime - 2)  # Random ephemeral key
    c1 = pow(g, k, prime)
    c2 = (message * pow(h, k, prime)) % prime
    return c1, c2

# Function to decrypt a message
def decrypt(private_key, prime, ciphertext):
    c1, c2 = ciphertext
    s = pow(c1, private_key, prime)  # Shared secret
    s_inv = pow(s, -1, prime)  # Modular inverse of shared secret
    message = (c2 * s_inv) % prime
    return message

# Example usage
def main():

    # Predefined prime number
    prime = 23

    # Step 1: Key generation
    public_key, private_key = generate_keys(prime)
    print(f"\nPublic Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Step 2: Encrypt a predefined message
    message = 7  # Example message
    ciphertext = encrypt(public_key, message)
    print(f"\nEncrypted Message (c1, c2): {ciphertext}")

    # Step 3: Decrypt the message
    decrypted_message = decrypt(private_key, prime, ciphertext)
    print(f"\nDecrypted Message: {decrypted_message}")

    # Verification
    if message == decrypted_message:
        print("Decryption successful!")
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    main()
