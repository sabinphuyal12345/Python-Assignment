#Classes

#Recatngle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")  # Output: 15
print(f"Perimeter: {rect.perimeter()}")  # Output: 16

#student class

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40

# Example usage:
student = Student("John Doe", 101, 85)
student.display_details()
print(f"Passed: {student.is_passed()}")  # Output: True

student2 = Student("Jane Smith", 102, 35)
student2.display_details()
print(f"Passed: {student2.is_passed()}")  # Output: False

#Circle Class 

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage:
circle = Circle(5)
print(f"Area: {circle.area():.2f}")           # Output: 78.54
print(f"Circumference: {circle.circumference():.2f}")  # Output: 31.42

#Class Bank Balance

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

# Example usage:
account = BankAccount("12345678", "John Doe", 500)
account.display_balance()  # Output: Current Balance: 500

account.deposit(200)  # Deposited: 200
account.display_balance()  # Output: Current Balance: 700

account.withdraw(300)  # Withdrawn: 300
account.display_balance()  # Output: Current Balance: 400

account.withdraw(500)  # Output: Insufficient balance.

#Class Book

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount):
        if 0 <= discount <= 100:
            self.price -= self.price * (discount / 100)
            print(f"Discount applied: {discount}%")
        else:
            print("Discount should be between 0 and 100.")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

# Example usage:
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 20.00)
book.display_details()
# Output:
# Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Price: $20.00

book.apply_discount(10)  # Discount applied: 10%
book.display_details()
# Output:
# Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Price: $18.00

#Class calculator

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

# Example usage:
calc = Calculator()

print(calc.add(5, 3))        # Output: 8
print(calc.subtract(5, 3))   # Output: 2
print(calc.multiply(5, 3))   # Output: 15
print(calc.divide(5, 3))     # Output: 1.666...
print(calc.divide(5, 0))     # Output: Error: Division by zero is not allowed.

#Class Person

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am a {self.gender}.")

class Employee(Person):
    def __init__(self, name, age, gender, job_title):
        super().__init__(name, age, gender)  # Call the constructor of the Person class
        self.job_title = job_title

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, I am a {self.gender}, and I work as a {self.job_title}.")

# Example usage:
person = Person("Alice", 30, "female")
person.introduce()
# Output: Hello, my name is Alice, I am 30 years old, and I am a female.

employee = Employee("Bob", 40, "male", "Software Engineer")
employee.introduce()
# Output: Hello, my name is Bob, I am 40 years old, I am a male, and I work as a Software Engineer.
