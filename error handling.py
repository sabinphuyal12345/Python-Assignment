
#Error Handling 

# Division with error handling
def divide_numbers():
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Example usage
divide_numbers()

# Integer input validation
def get_integer_input():
    try:
        # Ask the user to input an integer
        user_input = int(input("Please enter an integer: "))
    except ValueError:
        # If the user doesn't enter a valid integer, handle the error
        print("Invalid input, please enter an integer.")
    else:
        # If the input is valid, print the integer
        print(f"You entered the integer: {user_input}")

# Example usage
get_integer_input()

# File Not Found error handling
def open_file():
    try:
        with open('unknown.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file 'unknown.txt' was not found.")

# Example usage
open_file()
