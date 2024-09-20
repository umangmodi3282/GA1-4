# main.py of a1p2, INFO8601 Conestoga College - Professor Michael Yingbull
# Example usage of reverse_cipher function
# update this header as per the assignment when you revise the files in this directory

# a1p2-cipher.py

import sys
from simple_cipher import reverse_cipher

if __name__ == "__main__":
    # Ensure a plaintext argument is provided
    if len(sys.argv) != 2:
        print("Usage: python a1p2-cipher.py <plaintext>")
        sys.exit(1)

    # Get the plaintext from the command-line arguments
    plaintext = sys.argv[1]

    # Call the reverse_cipher function
    ciphertext = reverse_cipher(plaintext)

    # Print the reversed ciphertext
    print("Ciphertext:", ciphertext)