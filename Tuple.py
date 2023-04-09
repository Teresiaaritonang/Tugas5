#!/usr/bin/env python
# coding: utf-8

# In[1]:


newtuple=('a','b','c','d','d','e')
newtuple1= tuple('abcde')
print(newtuple)


# In[2]:


print(newtuple1)


# In[7]:


#Access tuple element
print(newtuple[0:4])


# In[8]:


#Traverse through tuple
for i in newtuple:
    print(i)


# In[9]:


for index in range(len(newtuple)):
    print(newtuple[index])


# In[12]:


#how to search for an element 
print('a' in newtuple)


# In[14]:


def searchintuple(ptuple,element):
    for i in ptuple:
        if i == element:
            return ptuple.index(i)
    return 'The element does not exist'
print(searchintuple(newtuple, 'a'))
        
    


# In[18]:


#Tuple operation
mytuple =(1,4,3,2,5)
mytuple1 =(1,2,6,9,8,7)

print(mytuple+mytuple1)


# In[19]:


mytuple1.count(2)


# In[20]:


print(mytuple*4)


# In[21]:


mytuple1.index(2)


# In[23]:


x,y,z = (10,15,20,25,30,35,40)[0::3]
print(x,y,z)


# In[24]:


x=3
y=-6

x,y = (y,x)[::-1]
print(x,y)


# In[ ]:




