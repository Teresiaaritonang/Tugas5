#!/usr/bin/env python
# coding: utf-8

# In[1]:


myDict= {'name':'Edy','agae':'26'}
myDict['address'] = 'London'
print(myDict)


# In[5]:


# Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key,dict[key])
traverseDict(myDict)


# In[8]:


# Search a dicionary

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict,27))


# In[20]:


myDict.pop('name')


# In[16]:


print(myDict)


# In[18]:


myDict.clear()


# In[24]:


myDict = {'name':'edy','age':26}


# In[25]:


print(myDict)


# In[26]:


dict = myDict.copy()


# In[27]:


print(dict)


# In[29]:


newDict = {}.fromkeys([1,2,3],0)
print(newDict)


# In[30]:


print(myDict.get('city',26))


# In[31]:


print(myDict.get('city',27))


# In[32]:


print(myDict.get('city'))


# In[33]:


print(myDict.items())


# In[34]:


print(myDict.keys())


# In[35]:


print(myDict.values())


# In[36]:


print(myDict.popitem())


# In[40]:


print(myDict.setdefault('name','added'))


# In[41]:


print(myDict)


# In[44]:


print(myDict.setdefault('name1','added'))


# In[46]:


print(myDict)


# In[51]:


print(myDict.pop('name1','not'))


# In[52]:


print(myDict)


# In[53]:


newDict = {'a':1,'b':2,'c':3}
myDict.update(newDict)
print(myDict)

