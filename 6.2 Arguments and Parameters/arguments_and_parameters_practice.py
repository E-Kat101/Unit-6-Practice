"""
1. Given the code below, answer the following questions:
    How many arguments are sent to the num_chairs function? What are they?
    Two arguments are sent to the num_chairs functions. They are the value 4 and the value 5.
    
    What are the names of the parameter variables? What values are they assigned from running the code below?
    The names of the parameter variables are tables and chairs_per_table. From running the code below, the number of tables gets assigned a value of 4, and the number of chairs per tables gets assigned a value of 5.
    
    What is the output?
    The output is: You will need 20 chairs.
    
    What happens when you remove an argument? when you add one?
    When you remove an argument, an error will occur saying the function num_chairs() is missing 1 required positional argument, which is the value for chairs_per_table. When you add an argument, an error will occur saying that num_chairs only takes two positional arguments, yet three were given. In both scenarios, the code will not run.
"""

def num_chairs(tables, chairs_per_table):
    chairs = tables * chairs_per_table
    print(f"You will need {chairs} chairs.")


num_chairs(4, 5)


# 2. Create a function that takes one integer argument and simply prints it out. Call this function print_integer.
def print_integer(n):
    print(n)

if __name__ == "__main__":
    print_integer(5)

    
# 3. Create a function that takes two integer arguments and prints out their difference. You can use math.abs() for absolute value.
def subtract(a, b):
    difference = abs(b - a)

    print(difference)

subtract(-5, 4)


# 4. List the two things wrong with the following code and how to fix it.

# function subtract(a):
# That is not the proper way to define a function
# There is only one parameter, but two arguments
#     print(a - b)
   

# subtract(5, 7)

def subtract(a, b):
    print(a - b)

subtract(5, 7)


# 5. How would you call the following function? Give two examples.
def activate_thrusters(percent_power):
    pass

activate_thrusters(80)
# or
if __name__ == "__main__":
    activate_thrusters(80)

    
# 6. What is wrong with how the code below calls a function that takes a name and how many apples that person will eat? Give an example of the correct way to do it.
# person_apples

# The code does not involve the two arguments in the brackets that have to come after the function. The first argument should be a string that is a name, and the second argument should be the integer value of how many apples the person will eat.
# Also, it is best practice to use the if __name__ == "__main__": statement to call functions.
if __name__ == "__main__":
    person_apples("George", 23)
