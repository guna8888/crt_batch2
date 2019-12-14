#!/usr/bin/env python
# coding: utf-8

# # python
# ## pyhton
# - point1
#      **subpoint
# 
# - point2
# - point3
# 
# 

# 

# In[5]:


# pyhton is very usefull
# output function
print('ahellow worlf')
print('welcome to the programmingd')
a=input('enter your name')
print(a)


# 

# In[6]:


a=10
b=10
a+b


# # datatypes
# ## int
# ## float
# ## boolean
# ## complex
# ## string

# In[11]:


a=complex(5+1j)
b=complex(4+2J)
a+b
print(a+b)


# In[14]:


a = 1234
b=len(str(a))
print(b)


# # operators
# ## arthimectic operators
# ### +,/,%,-,*,//,**
# 

# In[15]:


a=5
b=7
print(a+b)
print(a-b)
print(a%b)
print(a*b)
print(a//b)
print(a**b)


# # logical operators
# ## and,or

# In[17]:


a=5
b=6
print(a>2 and b<3)


# # relational operators
# ## <,>,=,<=,>=,==,!=

# In[19]:


a=5
b=9
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a=b)
print(a!=b)


# In[20]:


a="python"
print('p' in a)
print('y' in a)
print('z' in a)


# # conditional statements
# ## if, if else,elif
# 

# In[24]:


a=int(input("enter the number"))
if a>10:
    print('big number')
else:
    print('small number')



# In[29]:


# to check the elif condition
a=int(input('enter the number '))
if a>0:
    print('+ve')
elif a<0:
    print('-ve')
else :
    print('zero')


# In[36]:


# to check weather the given year is leap year or not
year=int(input("Enter year to be checked:"))

if(year%4==0 and year%100!=0 or year%400==0):
    print('The year is a leap year!')
else:
    print("The year isn't a leap year")








# In[ ]:





# In[ ]:





# In[ ]:




