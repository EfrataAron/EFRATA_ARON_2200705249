# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""_summary_ 
    
    Dictionaries in python are collections of keys and values
    -Unordered
    -mutable and
    -indexed by keys
    
    """

# Example 1: Create a dictionary
# Create a dictionary for a student pursuing software engineering
# the key must be your name, age, technology interest and year of study. put
# your own details

print("Example 1 Solution")

student_dict = {
    "name": "Efrata Aron",
    "age": "30",
    "technology": "AI and ML",
    "course": "BSE",
    "Year": "Year3",
}

print(student_dict["name"])
print()

# Access values

# Modify Values:

# Exercise 1: Modify age and technology
print("Exercise 1 Solution")
student_dict["age"] = "42"
student_dict["technology"] = "Robotics"


print(student_dict["age"])
print(student_dict["technology"])

# Example2: adding keys and values
print()
print("Example 2")
student_dict["email"] = "efrataaron5@gmail.com"

print(student_dict)

# Exercise 2: Remove a key and value from student dictionary
print()
print("Exercise 2 Solution")
del student_dict["age"]
print(student_dict)

# Remove using pop() method
year = student_dict.pop("Year")
print("dictionary after removing Year", student_dict)
print("removed value", year)
print()


# Common Dictionary methods
"""_summary_
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value



"""
# Example 3: Use the get method to get the value
print("Example 3 ")
print(student_dict.get("technology"))

# Exercise 3: Use the update method to change value in age

student_dict.update({"age": "25"})
print(student_dict)
print()

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary
print("Exercise 4 Solution")
if "age" in student_dict:
    print(" age is present in the dictionary.", student_dict["age"])

else:
    print(" age is not present in the dictionary.")

print()

# keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""_summary_

keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """
print()

# Exercise 5: Use the update method to change the course and add a new
# key "WhatsApp_Number" to the dictionary
print("Exercise 5 Solution")
student_dict.update({"course": "BSC", "WhatsApp_Number": "0770636395"})
print("Student dictionary after change", student_dict)
print()
