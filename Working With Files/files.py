#!/usr/bin/env python
# coding: utf-8

# In[2]:


file_obj = open('Downloads/sample1.txt', 'r')
fie_data = file_obj.read(100)
fie_data


# In[2]:


file_obj = open('Downloads/sample1.txt', 'r')
file_data = file_obj.readlines()
print(type(file_data))
print (len(file_data))


# In[3]:


with open('Downloads/sample1.txt', 'r') as file_obj
    file_data = file_obj.readlines


# In[5]:


with open('Downloads/sample1.txt', 'r') as file_obj :
    file_data = file_obj.readlines()
print(file_data[1])


# In[8]:


with open('Downloads/sample4.csv') as file_obj :
    file_data = file_obj.readlines()
print(file_data[:5])


# In[10]:


import csv
with open('Downloads/sample4.csv') as file_obj :
    file_data = csv.reader(file_obj)
    for row in file_data :
        print(row)
print(type(file_data))


# In[11]:


import csv
with open('Downloads/sample4.csv') as file_obj :
    file_data = csv.reader(file_obj) 
    file_list = list(file_data)
file_list


# In[16]:


import csv
with open('Downloads/sample4.csv') as file_obj :
    file_data = csv.reader(file_obj) 
    file_list = list(file_data)
    
number =[]
for row in file_list[1:] :
    number.append(row[1])
number


# In[18]:


import csv
with open('Downloads/sample4.csv') as file_obj :
    file_data = csv.DictReader(file_obj) 
    for row in file_data :
        print(row)


# In[22]:


import csv
with open('Downloads/sample4.csv') as file_obj :
    file_data = csv.DictReader(file_obj) 
    for row in file_data :
        print(row['Game Number'])


# In[ ]:




