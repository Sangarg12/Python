#!/usr/bin/env python
# coding: utf-8

# # Generators
# 
# Generators allow us to generate as we go along, instead of holding everything in memory and will be memory efficient.
# Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. This type of function is a generator in Python, allowing us to generate a sequence of values over time. The main difference in syntax will be the use of a "yield" statement.
# 
# In most aspects, a generator function will appear very similar to a normal function. The main difference is when a generator function is compiled they become an object that supports an iteration protocol. That means when they are called in your code they don't actually return a value and then exit. Instead, generator functions will automatically suspend and resume their execution and state around the last point of value generation. The main advantage here is that instead of having to compute an entire series of values up front, the generator computes one value and then suspends its activity awaiting the next instruction. This feature is known as state suspension.
# 
# # To start getting a better understanding of generators, let's go ahead and see how we can create some.
# 

# In[1]:


#Normal cube function

def cube(n):
    result = []
    for i in range(n):
        result.append(i**3)
    
    return result


# In[2]:


cube(10)


# In[3]:


#above we noticed that it return the full list of of cubes till we ask for so here result holds the whole list in 
#memory and return to us.Suppose if we call cube for 1 millin number then how much memory it will occupy so it won't be 
# memory efficient if we have huge number which occupy fore memory to store.


# In[10]:


#The same thing we can do with generator with yield keyword.Lets see

def cube(n):
    #result = []  ----- commented
    for i in range(n):
        #result.append(i**3) -- commented
#instead use yield here
        yield i**3
    # return result  ----- no need of returning anything


# In[11]:


cube(10)


# In[12]:


# it won't return any result because it is showing that is now generator so we need to iterate the numbers with generator function


# In[13]:


for i in cube(10):
    print(i)


# Great! Now since we have a generator function we don't have to keep track of every single cube we created.
# 
# Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time.

# In[15]:


#lets try to break it into steps how generator is working, how it is memory efficient.how it resume where it left off.


# In[16]:


#lets run cube function again

def cube(n):
    #result = []  ----- commented
    for i in range(n):
        #result.append(i**3) -- commented
#instead use yield here
        yield i**3
    # return result  ----- no need of returning anything


# In[17]:


cube(10)


# In[18]:


g= cube(10)


# In[19]:


g


# In[20]:


print(next(g))


# In[21]:


#it print first value

print(next(g))


# In[22]:


#it prints 1 which is after 0. so it means it resume value where it stops to iterate before.

print(next(g))


# In[29]:


print(next(g)) # lets run is multiple type to reach the last value so that we can understand in last how it behaves


# In[30]:


#Above one is last value of the iterations.lets see when we run this again what will be the output

print(next(g))


# In[31]:


#it shows "StopIteration" because we called off all the values and functions is exist now.


# Observe that a generator object is generated once, but its code is not run all at once. Only calls to next actually execute (part of) the code. Execution of the code in a generator stops once a yield statement has been reached, upon which it returns a value. The next call to next then causes execution to continue in the state in which the generator was left after the last yield. This is a fundamental difference with regular functions: those always start execution at the "top" and discard their state upon returning a value.
# 
# 
# Why we use generator insteaded of normal functon ? ans is :- Instead of creating a function which returns a list of values, one can write a generator which generates the values on the fly. This means that no list needs to be constructed, meaning that the resulting code is more memory efficient. In this way one can even describe data streams which would simply be too large to fit in memory.

# In[ ]:




