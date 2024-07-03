# Error Handling in Python
# Exception Handling with try, except, else, and finally
# Custom exceptions

"""_summary_

Notes:
Error handling in Python it helps to handle unexpected situations and errors.

Try: contains code that might throw an exception
NB: If an exception is occurs the rest of the code in the try block is skipped, or ignored

2. Except: catches and handles exceptions
NB: You can specify different handlers to different exceptions types

3. Else: the code runs if no exception occurs
If no exception are raised in the try block it runs.

4. Finally: It runs whether an exception is raised/occurred or not
NB: Used for cleaning up actions 

"""
# Example 1: Handle exceptions with division by zero.
print("Example 1")

try:
    number = int(input('Enter a number: '))
    result = 20 / number
except ValueError:
    print("Invalid number! Please enter a valid number")
    
except ZeroDivisionError:
    print("Error! Division by zero is not allowed")
    
else:
    print(f"Result is {result}")
    
finally:
    print("Execution completed successfully")

print()
    
# Exercise 1: Write a function that converts a string to an integer and handle both ValueError
# if a the string cannot be converted to an integer and the TypeError if the input is not a string
# Use multiple except block to handle these exceptions.
print("Exercise 1 solution")  


# print("Exercise 1")
def string_to_integer():
    try:
        number = int(input("Enter string value: "))
    except ValueError as valueError:
        print("Invalid input! Please enter a valid number.")
        print(f"ValueError: {valueError}")
        
    except TypeError as typeError:
        print("Please enter a string")
        print(f"ValueError: {typeError}")
        
    else:
        print(f"Result is {number}")

string_to_integer()



print()
# Custom exception handling
# Example 2: Exception raised for error in the input, if funds are insufficient
print("Example 2")

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account."
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exceptions handling
try:
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
    
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
else:
    print(f"New balance is {new_balance}")
finally:
    print("Transaction completed")

  
# Note 
"""_summary_
    Defining a custom exception
    
    
    Class CustomError(Exception):
        
def __init__ (self,message):
        super().__init__(message)
         self.message = message
         
         ### Raising a custom Exception
         def check_value(value):
         if value is < 0 or value:
            raise CustomError("Value cannot be negative")
            return value

        
    # Handle exceptions with try, except, else, and finally
    try:
        result = check_value(-10)
        
    except CustomError as e:
        print(f"Custom error caught: {e.message}")
        
    """

print()
print("Exercise 2 Solution")

class InvalidAgeError(Exception):
    def _init_(self, age):
        self.age = age
        self.message = f"Invalid age {self.age}. Enter a valid age input."
        super()._init_(self.message)
        # Super()
        # calling
        # initializing parent class constructor
        

def check_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"you are {age} years old")

try:
    check_age()
except InvalidAgeError as e:
    print(e.message)
else:
    print("Valid age entered.")
finally:
    print("Age validation complete.")
