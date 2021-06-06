#!/usr/bin/env python
# coding: utf-8

# ## Part I: Bult-in Data Structures
# ### list, tuple(immutable), set, and dictionary
# 
# https://towardsdatascience.com/data-structures-algorithms-in-python-68c8dbb19c90
# 
# https://towardsdatascience.com/data-structures-algorithms-in-python-68c8dbb19c90
# 
# ### Simple put, a mutable object can be changed (we can change its state or contents) after it is created, and an immutable object can’t.
# 
# ### Objects of built-in types like (int, float, bool, str, tuple, unicode, frozenset) are immutable. 
# ### Objects of built-in types like (list, set, dict) are mutable. 
# 
# ### Custom classes are generally mutable. To simulate immutability in a class, one should override attribute setting and deletion to raise exceptions

# In[1]:


a = "abc"


# In[2]:


type(a) #returns the type of an object


# In[3]:


id(a) #returns the identity of an object as an integer


# In[4]:


b = "abc"


# In[5]:


id(b)


# In[6]:


print(a is b) #compares the identity of two objects


# ### Immutable objects doesn’t allow modification after creation

# In[7]:


x = 10
y = x


# In[8]:


id(x)


# In[9]:


id(y)


# In[10]:


print(x is y)


# In[11]:


x = x + 1


# In[12]:


id(x)


# In[13]:


id(y)


# In[14]:


print(x is y)


# ### Mutable objects does allow modification after creation
# 

# In[15]:


m = list([1, 2, 3])
n = m


# In[16]:


id(m)


# In[17]:


id(n)


# In[18]:


print(m is n)


# In[19]:


m.pop()


# In[20]:


print(m is n)


# In[21]:


m


# In[22]:


n


# #### in above line, object ids of mutables will not be changed
# ####  m and n will be pointing to the same list object after the modification. The list object will now contain [1, 2].

# ### So what have we seen so far from the above examples?
# Python handles mutable and immutable objects differently.
# 
# Immutable are quicker to access than mutable objects.
# 
# Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. 
# Immutables are used when you need to ensure that the object you made will always stay the same.
# 
# Immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable objects is cheap.

# #### Exceptions in immutability..
# #### Let us consider a tuple t = (‘holberton’, [1, 2, 3])
# The above tuple t contains elements of different data types, the first one is an immutable string and the second one is a mutable list.The tuple itself isn’t mutable . i.e. it doesn’t have any methods for changing its contents. Likewise, the string is immutable because strings don’t have any mutating methods. But the list object does have mutating methods, so it can be changed. This is a subtle point, but nonetheless important: the “value” of an immutable object can’t change, but it’s constituent objects can.

# ### How objects are passed to Functions
# Its important for us to know difference between mutable and immutable types and how they are treated when passed onto functions .Memory efficiency is highly affected when the proper objects are used.
# 
# For example if a mutable object is called by reference in a function, it can change the original variable itself. Hence to avoid this, the original variable needs to be copied to another variable. Immutable objects can be called by reference because its value cannot be changed anyways.
# #### ------------mutable--------------------
# def updateList(list1):
# 
#     list1 += [10]
#     
# n = [5, 6]
# 
# print(id(n))                  # 140312184155336
# 
# updateList(n)
# 
# print(n)                      # [5, 6, 10]
# 
# print(id(n))                  # 140312184155336
# 
# #### ---------------------------------
# As we can see from the above example, we have called the list via call by reference, so the changes are made to the original list itself.
# 
# Lets take a look at another example:
# #### ---------------immutable------------------
# def updateNumber(n):
# 
#     print(id(n))
#     
#     n += 10
#     
# b = 5
# 
# print(id(b))                   # 10055680
# 
# updateNumber(b)                # 10055680
# 
# print(b)                       # 5
# #### ---------------------------------
# 
# In the above example the same object is passed to the function, but the variables value doesn’t change even though the object is identical. This is called pass by value. 
# #### So what is exactly happening here? 
# 
# #### When the value is called by the function, only the value of the variable is passed, not the object itself. So the variable referencing the object is not changed, but the object itself is being changed but within the function scope only. Hence the change is not reflected.

# ## List
# ### A list is defined using square brackets and holds data that is separated by commas. The list is mutable and ordered. It can contain a mix of different data types.
# 

# In[23]:



# Join is a string method that takes a list of strings as an argument, 
# and returns a string consisting of the list elements joined by a separator string.

first_str = "\n".join(["What","is","your","favourite","painting","?"])
second_str = "-".join(["Who","is","your","favourite","artist","?"])

print(first_str)
print(second_str)


# In[24]:


artist = ['Chagall', 'Kandinskij', 'Dalí', 'da Vinci', 'Picasso', 'Warhol']

artist.append('Basquiat') # append method permits us to add Basquiat in our list of artists
print(artist)


# ## Tuple
# #### A tuple is another container. It is a data type for immutable ordered sequences of elements. Immutable because you can’t add and remove elements from tuples, or sort them in place.
# 
# #### A tuple is a collection which is ordered and unchangeable.
# 
# #### Tuples are written with round brackets.
# 
# ### Tuple Items
# #### 1. Tuple items are ordered, unchangeable, and allow duplicate values.
# 
# #### 2. Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# 
# #### Ordered
# #### When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# 
# #### Unchangeable
# #### Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# 
# #### Allow Duplicates
# #### Since tuple are indexed, tuples can have items with the same value:

# In[25]:


length, width, height = 7, 3, 1 # we can assign multiple varibles in one shot
print("The dimensions are {} x {} x {}".format(length, width, height))


# In[26]:


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# In[27]:


my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple


# In[32]:


a


# ### Set
# #### Set is a mutable and unordered collection of unique elements. It can permit us to remove duplicate quickly from a list.

# In[34]:


numbers = [1, 2, 6, 3, 1, 1, 5] 

unique_nums = set(numbers)
print(unique_nums)
print(type(unique_nums))


# ### Dictionary
# #### Dictionary is a mutable and unordered data structure. It permits storing a pair of items (i.e. keys and values).
# #### As the example below shows, in the dictionary, it is possible to include containers into other containers to create compound data structures.

# In[37]:


music = { 'jazz': {"Coltrane": "In a Sentimental Mood",
                          "M.Davis":"Blue in Green" ,
                          "T.Monk":"Don't Blame Me"},
            "classical" : {"Bach": "Cello Suit",
                        "Mozart": "Lacrimosa",
                        "Satie": "Gymnopédie"}}

print(music["jazz"]["Coltrane"]) # we select the value of the key Coltrane
print("\n")
print(music)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




