# simple_cipher.py
# INFO86801 Conestoga College, Professor Michael Yingbull
# update this header as per the assignment when you revise the files in this directory

import re

def reverse_cipher(plaintext):
    """
    Accepts a plaintext string and returns the reversed string as the ciphertext.
    """
    # Reverse the plaintext using slicing
    ciphertext = plaintext[::-1]
    return ciphertext


def reverse_caesar_cipher(plaintext: str, student_number1: int, student_number2: int):
    """
    Encrypts the given plaintext by reversing the string and applying a Caesar cipher shift
    calculated based on the sum of digits from the highest student number.

    Parameters:
    plaintext (str): The text to be encrypted.
    student_number1 (int): First student's number.
    student_number2 (int): Second student's number.

    Returns:
    str: The encrypted string.
    """
    # Step 1: Preprocessing - Remove spaces, punctuation, and convert to uppercase
    clean_text = re.sub(r'[^A-Za-z]', '', plaintext).upper()
    
    # Step 2: Reverse the string
    reversed_text = clean_text[::-1]
    
    # Step 3: Determine the higher student number
    highest_student_number = max(student_number1, student_number2)
    
    # Step 4: Calculate shift based on the sum of digits of the higher student number, modulo 26
    digit_sum = sum(int(digit) for digit in str(highest_student_number))
    shift_value = digit_sum % 26
    
    # Step 5: Apply Caesar shift to each character
    def caesar_shift(char, shift):
        # Shift a single character by 'shift' positions, wrapping around from 'Z' to 'A'
        shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        return shifted

    encrypted_text = ''.join(caesar_shift(char, shift_value) for char in reversed_text)

    return encrypted_text
