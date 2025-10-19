# 🐍 Python Functions — Examples from W3Schools

This file contains clear examples and explanations of Python functions for **beginners**.

---

## 1️⃣ Create and Call a Function
```python
def my_function():
    print("Hello from a function")
my_function()
```

## 2️⃣ Function with Parameters
```python
def greet(name):
    print("Hello, " + name)
greet("Aref")
```

## 3️⃣ Function with Multiple Parameters
```python
def full_name(first, last):
    print(first + " " + last)
full_name("Aref", "Rezvanpanah")
```

## 4️⃣ Arbitrary Arguments (*args)
```python
def fruits(*names):
    print("The first fruit is " + names[0])
fruits("Apple", "Banana", "Cherry")
```

## 5️⃣ Keyword Arguments
```python
def country(country_name):
    print("I am from " + country_name)
country(country_name="Afghanistan")
```

## 6️⃣ Arbitrary Keyword Arguments (**kwargs)
```python
def student_info(**info):
    print("His last name is " + info["lname"])
student_info(fname="Aref", lname="Rezvanpanah")
```

## 7️⃣ Default Parameter Value
```python
def country_default(country="Norway"):
    print("I am from " + country)
country_default("Sweden")
country_default()
```

## 8️⃣ Passing a List as an Argument
```python
def my_food(food):
    for item in food:
        print(item)
fruits = ["apple", "banana", "cherry"]
my_food(fruits)
```

## 9️⃣ Return Values
```python
def multiply(x):
    return 5 * x
print(multiply(3))
```

## 🔟 The pass Statement
```python
def empty_function():
    pass
```

## 🧩 Function Names
```python
def calculate_sum(a, b):
    return a + b
print(calculate_sum(4, 7))
```

## 💡 Why Use Functions?
```python
def area_of_rectangle(length, width):
    return length * width
print("Area:", area_of_rectangle(5, 10))
```

## 📎 Author
👩‍💻 **Created by:** Rezvan Panah  
📅 **Year:** 2025  
💬 **Language:** Python 3  
🎯 **Purpose:** Teaching conditional statements in Python in a clear and simple way.

---

## 💖 Support & Feedback
If this repository helped you, please consider:
- ⭐ **Starring** the repo  
- 🗨️ **Commenting** your thoughts  
- 📢 **Sharing** it with others learning Python  

Your feedback motivates more free educational content!

---
