import sys

# Error handling for command line arguments
if len(sys.argv) != 2:
    print("Usage: python a1p1-umodi3777.py <umodi3777>")
    sys.exit(1)

# Extract user ID from command line
user_id = sys.argv[1]

# Function to convert user ID to a number by summing Unicode values
def calculate_dividend(user_id):
    return sum(ord(char) for char in user_id)

# Function to get divisor from the last two digits of a student number
def calculate_divisor(student_number):
    last_two_digits = int(str(student_number)[-2:])
    # Handle case where the last two digits are 00
    return last_two_digits if last_two_digits != 0 else 1

student_number = 8983777

# Calculate the dividend and divisor
dividend = calculate_dividend(user_id)
divisor = calculate_divisor(student_number)

# Perform the modulo operation
try:
    result = dividend % divisor
    print(f"Dividend (sum of Unicode values): {dividend}")
    print(f"Divisor (last two digits of student number): {divisor}")
    print(f"Result of {dividend} modulo {divisor} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
