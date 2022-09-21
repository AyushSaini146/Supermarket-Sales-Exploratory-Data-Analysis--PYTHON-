#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import basic libararies which are helpful in  data cleaning , manipulation & visualization .
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Import dataset
df=pd.read_csv('C:/Users/iball/Desktop/supermarket_sales - Sheet1.csv')


# # Data exploration And Cleaning

# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


#check Null values
df.isnull().sum()


# In[ ]:





# In[7]:


#Drop unwamted columns
df=df.drop(['Invoice ID','Date','Time'],axis=1)


# In[8]:


#All value seems same in 'gross marigin percentage' column,so let's find unique value in that column
df['gross margin percentage'].unique()
#RESULT:-All values are same in this column,so let's drop this column also 


# In[9]:


df.drop(['gross margin percentage'],axis=1)


# In[10]:


df.head()


# # Data Visualisation

# ## Q1 Find total Number of Male and Female Customers 

# In[11]:


df['Gender'].value_counts()


# In[12]:


sns.countplot('Gender',data=df)


# # Q2 Show product line wise male and female customers

# ### Creating dummies for Gender column for getting numeric data to make seaborn bar plot

# In[13]:


#making dummies for gender column
gender_dummies=pd.get_dummies(df['Gender'])
gender_dummies.head()


# ### Joining original data frame(df) with gender_dummies data frame(gender_dummies)

# In[14]:


df=pd.concat([df, gender_dummies], axis = 1)
df.head()


# ### Product line wise Male customers

# In[15]:


plt.figure(figsize = (12,6))
sns.barplot(x = 'Product line', y = 'Male', data = df)


# ### Product line wise Female customers

# In[16]:


plt.figure(figsize = (12,6))
sns.barplot(x = 'Product line', y = 'Female', data = df)


# # Q3 Show city wise customers

# In[17]:


place_df = pd.DataFrame(df['City'].value_counts())
place_df


# In[18]:


sns.barplot(x = place_df.index  , y = place_df['City'])


# # Q4 Show number of payments by different payment methods

# In[19]:


payment_df = pd.DataFrame(df['Payment'].value_counts())
payment_df


# In[20]:


sns.barplot(x =payment_df.index , y = payment_df.Payment)


# # Q5 Show gross income Product line wise

# In[21]:


plt.figure(figsize= (12,6))
sns.barplot(x = 'Product line', y = 'gross income',data=df)


# # Q6 Show product line wise Ratings

# In[22]:


xdata=[0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize= (12,6))
sns.barplot( x ='Rating',y = 'Product line',data=df)
plt.xticks(xdata)


# # Q7  Show total bill in each product line

# In[23]:


plt.figure(figsize = (12,6))
sns.barplot(x = 'Total', y = 'Product line',data=df)


# # Q8 Show sales by Quantities sold

# In[24]:


quantity_df = pd.DataFrame(df['Quantity'].value_counts())
quantity_df


# In[25]:


plt.figure(figsize=(12,6))
sns.barplot(x = quantity_df.index , y = quantity_df['Quantity'] , palette = 'inferno')


# # Inference from the Analysis
# 
# 1.Total Customers = 1000
# 
# 2.Total Females = 501
# 
# 3.Total Males = 499
# 
# 4.Min Rating = 4
# 
# 5.Max Rating = 10
# 
# 6.Average Rating = 6.97
# 
# 7.Best Average Rating in Food & Beverages
# 
# 8.Max Average Gross Income in Home & Lifestyle
# 
# 9.Min Average Gross Income in Fashion Accessories
# 
# 10.Maximum customers buys 10 quantities
# 
# 11.Max Average total bill in Home and lifestyle
# 
# 12.Min Average total bill in Fashion Accessories
# 
# 13.Maximum People pays through e-wallet
# 
# 14.Maximum people comes from Yangon City
# 
# 15.Max Average Sales of Fashion Accessories is from Females
# 
# 16.Max Average Sales of Health & Beauty is from Males
