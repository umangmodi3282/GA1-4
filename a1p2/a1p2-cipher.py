
import sys
from simple_cipher import reverse_caesar_cipher

if __name__ == "__main__":
    # Ensure a plaintext argument is provided
    if len(sys.argv) != 4:
        print("Usage: python a1p2-cipher.py <hello Umang modi > <8983777> <8983776>")
        sys.exit(1)

    # Get the plaintext and student numbers from the command-line arguments
    plaintext = sys.argv[1]
    student_number1 = int(sys.argv[2])  # First student number as an integer
    student_number2 = int(sys.argv[3])  # Second student number as an integer

    # Call the reverse_caesar_cipher function
    ciphertext = reverse_caesar_cipher(plaintext, student_number1, student_number2)

    # Print the resulting ciphertext
    print("Ciphertext:", ciphertext)
