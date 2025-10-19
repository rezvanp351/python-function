# -------------------------------
# Python Functions

#Funtion Names and Why Use Functions
# def 2names():       # ❌ cannot start with a number
# def MyFunction():   # ❌ avoid capital letters for normal functions
# def user-name():    # ❌ cannot use hyphens
#--------------------------------
#use this role in function names:
# def my_function():  # ✅ use lowercase letters and underscores
# def calculate_sum(): # ✅ descriptive names
#

# -------------------------------

# 1. Creating and Calling a Function
def my_function():
    print("Hello from a function")
my_function()

# 2. Function with Parameters
def greet(name):
    print("Hello, " + name)
greet("Aref")
greet("Rezvan")

# 3. Function with Multiple Parameters
def full_name(first, last):
    print(first + " " + last)
full_name("Aref", "Rezvanpanah")

# 4. Arbitrary Arguments (*args)
def fruits(*names):
    print("The first fruit is " + names[0])
fruits("Apple", "Banana", "Cherry")

# 5. Keyword Arguments
def country(country_name):
    print("I am from " + country_name)
country(country_name="Afghanistan")

# 6. Arbitrary Keyword Arguments (**kwargs)
def student_info(**info):
    print("His last name is " + info["lname"])
student_info(fname="Aref", lname="Rezvanpanah")

# 7. Default Parameter Value
def country_default(country="Norway"):
    print("I am from " + country)
country_default("Sweden")
country_default()
country_default("Afghanistan")

# 8. Passing a List as an Argument
def my_food(food):
    for item in food:
        print(item)
fruits = ["apple", "banana", "cherry"]
my_food(fruits)

# 9. Return Values
def multiply(x):
    return 5 * x
print(multiply(3))
print(multiply(5))
print(multiply(9))

# 10. The pass Statement
def empty_function():
    pass

# 11. Function Names
def calculate_sum(a, b):
    return a + b
print(calculate_sum(4, 7))

# 12. Why Use Functions?
def area_of_rectangle(length, width):
    return length * width
print("Area:", area_of_rectangle(5, 10))
