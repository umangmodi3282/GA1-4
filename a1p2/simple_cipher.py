# simple_cipher.py
# INFO86801 Conestoga College, Profesisor Michael Yingbull
# update this header as per the assignment when you revise the files in this directory
def reverse_cipher(plaintext):
    """
    Accepts a plaintext string and returns the reversed string as the ciphertext.
    """
    # Reverse the plaintext using slicing
    ciphertext = plaintext[::-1]
    return ciphertext