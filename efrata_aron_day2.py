#EFRATA ARON
# 2200705249
#Day 2 


""" _summary_

Control Structures
 Conditional statements (if, elif, else)
 Loops (for, while)
 Comprehensions (list, dictionary
comprehensions)

"""

# if, elif, else

#Example 1
print("Example 1")
Age = 70 

if Age < 18: 
    print('You are an adult')
elif Age > 65:
    print('you are senior citizen')
    
else:
    print('You are a Youth')
    
    
    
  # Example 2 
print("Example 2") 
# 90, above above is Excellent, Equal 80 and above is Very good, if 70, good
# otherwise , not good. 


grade = 50

if grade >=90:
    print('Excellent')
elif grade >= 80:
    print('very good')
elif grade >= 70:
    print('Good')

else: 
    print('Not good')

""" 
 Exercise:  Scenario: Write a python script to determine the price 
 of a movie based on age. Condition children under 13 get discount for price 
 =shs1000
 Teenagers between 13 and 18 get discount for price = shs 500
 Adults 18 and above pay full price = shs 2000
 Otherwise, senior citizens pay full price = shs 5000
   
    """
    
    #Exercise 1 solution
print()   
print("Exercise Solution____") 

age = int(input("whats your age"))
fullprice= 2000
if age <13:
    discount= 1000
    Price= fullprice-discount
    print("Children pay " , Price)
   
    
elif 13 < age < 18:
     discount= 1000
     Price= fullprice-discount
     print("Teenagers pay " , Price)
     
elif 65 > age > 18:
     discount= 1000
     Price= fullprice-discount
     print("Adults pay " , Price)
         
else:
     print("senior citizens pay shs 5000")
    
    
# Loops (for, while)

"""_summary_
    for loop iterates over a sequence (list, tuple, dictionary, set, string)
    the while loop repeaats as long as a condition is true 
   
    """
    
#Example 3
print()   
print("Example 3")   
cars = ['Tesla', 'Audi', 'BMW', 'Jeep', 'RangeRover']
  
    
for car in cars:
        print(car)
print()    
# Example 4  count 1 to 10
print("Example 4")
 
count = 1
while count <= 10:
     print("Count 1 to 10:", count)
     count += 1
    

#Exercise 2

"""_summary_
    
    Create your own list of favorite colors using for loop
    2.  Create a reverse of the input 12345 to be 54321 using while loop
    """
print()
print("Exercise 2 solution_______________________________________________________________")
    
    #exercise solution
colors=["red", "black", "lavender", "turquoise"]
for color in colors:
    
    print(color) 
print()
 
print("reversecolors")   
reversed_colors=colors[::-1]

for color in reversed_colors:
    print(color)
print()    

    #using while loop to reverse
    
counter = 5
while counter >=1:
    
     print("Count 5 to 1:", counter)
     counter -= 1
    
    
    
    
         
    
