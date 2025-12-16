# Get the first number from the user
# We use float() to handle non-integer numbers (like 5.5)
num1 = float(input("Enter the first number: "))

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Perform the calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 # Standard division (results in a float)

# Print the results to match the required output format
print("\nAddition:", int(addition)) # Use int() to print as a whole number (15)
print("Subtraction:", int(subtraction)) # Use int() to print as a whole number (-5)
print("Multiplication:", int(multiplication)) # Use int() to print as a whole number (50)
print("Division:", division)