#return factorial for loop in a function

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
print(factorial(5))

#Check Number is prime or not

def is_prime(n):
    if n <= 1:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to √n
        if n % i == 0:
            return False  # If divisible, it's not prime
    return True  # Otherwise, it's prime

# Example usage:
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False

#Find Maximum Among List

def find_max(lst):
    if not lst:  # Check if the list is empty
        return None  # Return None for an empty list
    max_value = lst[0]  # Assume the first element is the maximum
    for num in lst:
        if num > max_value:  # Update max_value if a larger number is found
            max_value = num
    return max_value

# Example usage:
print(find_max([1, 3, 7, 0]))  # Output: 7
print(find_max([]))            # Output: None


#Check Palindrome

def palindrome_check(string):
    string = string.lower()  # Convert to lowercase for case-insensitivity
    return string == string[::-1]  # Compare the string with its reverse

# Example usage:
print(palindrome_check("radar"))  # Output: True
print(palindrome_check("hello"))  # Output: False
print(palindrome_check("Madam"))  # Output: True


#Sum of squares of natural numbers 

def sum_of_squares(n):
    if n < 1:
        return "Input must be a natural number (n ≥ 1)."
    return sum(i**2 for i in range(1, n + 1))

# Example usage:
print(sum_of_squares(5))  # Output: 55


#Sum of squares 

def sum_of_squares(n):
    if n < 1:
        return "Input must be a natural number (n ≥ 1)."
    return sum(i**2 for i in range(1, n + 1))

# Example usage:
print(sum_of_squares(3))  # Output: 14