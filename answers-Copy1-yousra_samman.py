#!/usr/bin/env python
# coding: utf-8

# Data Science Fundamentals: Python |
# [Table of Contents](../index.ipynb)
# - - - 
# <!--NAVIGATION-->
# Module 1. [Basic Python Syntax](./01_mod_python_syntax.ipynb) | [Variables and Objects](./02_python_variables_objects.ipynb) | [Operators](./03_python_operators.ipynb) | **[Exercises](./04_mod_practice.ipynb)**

# # Module 1: Practice Exercises

# In[1]:


# Jupyter Notebook Mod 01: Practice Assignment!
# Here are the compiled problems we did during our introduction to Jupyter Notebooks. Take the time to go through each of these practice problems that we went through during class, and COMMENT the code explaining what each line does. 

# BE SURE TO DO #6-10 As well!

# Submit a link to your GitHub repository.

# Submit your COMMENTED version of this file as your assignment. 


# 1. Accept the user's first and last name and print them in reverse order with a space between them

# In[2]:


# 1. Accept the user's first and last name and print them in reverse order with a space between them


# In[3]:


x = 'samman'
y = 'yousra'
n = ' '
print(x + n + y)


# 2. Accept an integer (n) and compute the value of n+nn+nnn

# In[4]:


# 2. Accept an integer (n) input from the user and compute the value of n+nn+nnn. For example if n=4 then n + nn + nnn = 4 + 44 + 444 = 492


# In[5]:


n = 600
nn = 10
nnn = 5
print(n+nn+nnn)


# 3. Ask the user "What country are you from?" then print the following statement: "I have heard that [input] is a beautiful country!"

# In[7]:


# 3. Ask the user "What country are you from?" then print the following statement: "I have heard that [input] is a beautiful country!"


# In[8]:


x = ' "What country are you from?" '
y = ' "I have heard that Algeria is a beautiful country!"'
print(x + y)


# 4. Write a for loop that multiplies the number 4 by all the integers from 0 to 10 and prints the following for each: "4 multiplied by [i] is [x]" 

# In[9]:


# 4. What is the output of the following Python code 
    # x = 10
    # y = 50
    # if (x ** 2 > 100 and y < 100):
    # print(x, y)


# In[11]:


x = 10 # x is a pointer for 10
y = 50 # y is a pointer from 50
if (x ** 2 > 100 and y < 100): # if x^2 is greater than 100 and y is less than 100 print both x and y after running the code
    print(x, y)


# 5. Print a multiplication table that matches the following. Use two nested for loops to achieve this.

# <img src="files/table.png">

# In[13]:


# 5. What is the output of the following addition (+) operator, and why does this code chunk execute this way?
    # a = [10, 20]
    # b = a
    # b += [30, 40]
    # print(a)
    # print(b)


# In[14]:


a = [10, 20] # a is a pointer for 10 and 20
b = a # b is a pointer for a, or is the same as a
b += [30, 40] #b += is the same as b=b+30 and 40
print(a)
print(b)


# 6. Is a String Immutable in Python?

# In[ ]:


# 6. What is the output of the following code and what arithmetic operators is being used here? print(2%6)


# In[15]:


print(2%6) #modulus (integer remainder after division of a by b)


# 7. What is the output of x AND explain why that is the output for:
x = 36 / 4 * (3 +  2) * 4 + 2
# In[ ]:


# 7. What is the output of the following code and what arithmetic operators are used here? print(2 * 3 ** 3 * 4)


# In[16]:


print(2 * 3 ** 3 * 4) #multiplication (product of a and b)


# In[ ]:


# 8. What is a text editor?


# In[ ]:


# 8. ANSWER: saves your files w/o formatting


# In[ ]:


# 9. What is python?


# In[ ]:


# 9. ANSWER: object-oriented programming language that is easy to read


# In[ ]:


# 10. What is jupyter notebook, what type of python environment is it, and what alternatives are there to jupyter notebook?


# In[ ]:


# 10. ANSWER: jupyter notebook a web-based interactive computing platform
              # IPython Kernel is the type of environment
              # Eclipse is an alt


# <!--NAVIGATION-->
# Module 1. [Basic Python Syntax](./01_mod_python_syntax.ipynb) | [Variables and Objects](./02_python_variables_objects.ipynb) | [Operators](./03_python_operators.ipynb) | **[Practice](./04_mod_practice.ipynb)**
# <br>
# [top](#)

# - - -
# 
# Copyright © 2020 Qualex Consulting Services Incorporated.
