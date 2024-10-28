import sys
import os

def encrypt(plaintext_path, ciphertext_path, key_path):
    # Read the plaintext and key
    with open(plaintext_path, 'rb') as plaintext_file, open(key_path, 'rb') as key_file:
        plaintext = plaintext_file.read()
        key = key_file.read()

    # Ensure the key is long enough
    if len(key) < len(plaintext):
        raise ValueError("Key must be at least as long as the plaintext.")

    # Encrypt using XOR
    ciphertext = bytearray([b ^ k for b, k in zip(plaintext, key)])

    # Save the ciphertext
    with open(ciphertext_path, 'wb') as ciphertext_file:
        ciphertext_file.write(ciphertext)

    print(f"Encrypted {plaintext_path} to {ciphertext_path} using {key_path}")

def decrypt(ciphertext_path, decrypted_path, key_path):
    # Read the ciphertext and key
    with open(ciphertext_path, 'rb') as ciphertext_file, open(key_path, 'rb') as key_file:
        ciphertext = ciphertext_file.read()
        key = key_file.read()

    # Decrypt using XOR
    decrypted = bytearray([c ^ k for c, k in zip(ciphertext, key)])

    # Save the decrypted text
    with open(decrypted_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"Decrypted {ciphertext_path} to {decrypted_path} using {key_path}")

# Check if enough arguments are provided
if len(sys.argv) != 5:
    print("Usage:")
    print("  To encrypt: python a2-jsmith1234avera4567.py --encrypt <plaintext_path> <ciphertext_path> <key_path>")
    print("  To decrypt: python a2-jsmith1234avera4567.py --decrypt <ciphertext_path> <decrypted_path> <key_path>")
    sys.exit(1)

# Extract command-line arguments
mode = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]
key_path = sys.argv[4]

# Run the appropriate function based on the mode
if mode == '--encrypt':
    encrypt(input_path, output_path, key_path)
elif mode == '--decrypt':
    decrypt(input_path, output_path, key_path)
else:
    print("Invalid mode. Use --encrypt or --decrypt.")