#!/usr/bin/env python
# coding: utf-8

# Dictionaries
# 
# We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.
# 
# This section will serve as a brief introduction to dictionaries and consist of:
# 
# 1.) Constructing a Dictionary
# 2.) Accessing objects from a dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods
# 
# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.
# 
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.
# Constructing a Dictionary
# 
# Let's see how we can construct dictionaries to get a better understanding of how they work!
# 

# In[1]:


# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}


# In[2]:


my_dict


# In[3]:


#calling
my_dict['key1']


# In[4]:


#Its important to note that dictionaries are very flexible in the data types they can hold. For example:

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# In[5]:


my_dict


# In[6]:


# Let's call items from the dictionary

my_dict['key3']


# In[7]:


#calling specific value

my_dict['key3'][1]


# In[9]:


#making effect on items.Lets do in uppper case

my_dict['key3'][2].upper()


# In[10]:


my_dict['key3'].append('itme3')


# In[11]:


my_dict


# In[12]:


my_dict['key3']


# In[13]:


my_dict['key1']


# In[14]:


my_dict['key1'] = my_dict['key1']-123


# In[15]:


my_dict


# In[16]:


my_dict['key1']


# In[17]:


#We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:

d ={}


# In[18]:


d


# In[19]:


d['apple_price'] = 40


# In[20]:


d


# In[21]:


#ANOTHER ONE

d['orange_price'] = 25


# In[22]:


d


# #Nesting with Dictionaries
# 
# Hopefully you're starting to see how powerful Python is with its flexibility of nesting objects and calling methods on them. Let's see a dictionary nested inside a dictionary:
# 

# In[24]:


# Dictionary nested inside a dictionary nested inside a dictionary

d= {'key1':{'nest_key':{'subnest_key':'value'}}}


# In[25]:


d


# In[27]:


#Wow! That's a quite the inception of dictionaries! Let's see how we can grab that value:

d['key1']['nest_key']['subnest_key']


# A few Dictionary Methods
# 
# There are a few methods we can call on a dictionary. Let's get a quick introduction to a few of them:
# 

# In[28]:


# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}


# In[30]:


# Method to return a list of all keys 

d.keys()


# In[31]:


# Method to grab all values

d.values()


# In[32]:


# Method to return tuples of all items  (we'll learn about tuples soon)

d.items()


# Hopefully you now have a good basic understanding how to construct dictionaries. There's a lot more to go into here, but we will revisit dictionaries at later time. After this section all you need to know is how to create a dictionary and how to retrieve values from it.
# 

# In[ ]:




