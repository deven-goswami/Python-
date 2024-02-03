#!/usr/bin/env python
# coding: utf-8

# 
# # Amazon_Sales_Analysis

# In[1]:


import pandas as pd
import os  


# In[2]:


dataset = pd.read_csv(r"C:/Users/dilip/Amazon Sale Report.csv",dtype={'column23': float})
dataset.tail(1)


# In[3]:


df = pd.DataFrame(dataset)


# In[4]:


Total_Amount = round(df['Amount'].sum(),2) 
print(Total_Amount)


# In[5]:


Avg_Amount = round(df['Amount'].mean(),2)
print(Avg_Amount)


# In[6]:


High_Amount = round(df['Amount'].max(),2)
low_A = round(df['Amount'].min(),2)
print(High_Amount)
print(low_A)


# In[7]:


Total_raws = df.shape[0]
print('Total number of Raws:',Total_raws)


# In[8]:


#more amount to 5000
k5 =df[df['Amount']>5000]
count_k5 = len(k5)
print(f"Number of rows with Amount greater than 5000:", count_k5)


# In[9]:


Value_100 =df[df['Amount']<100]
count_Value_100 = Value_100.shape[0]
print('Number of Orders with Amount less than 100:',count_Value_100)


# In[10]:


df=df.drop('ship-postal-code', axis=1)
df=df.iloc[:,1:]
df


# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt
#df.head()
df.corr()


# In[12]:


df = df.rename(columns={'ship-state': 'ship_state'})
df.head(1)


# In[13]:


df.groupby(['ship_state','Fulfilment']).sum()
float_value = 3.14
string_value = str(float_value)


# In[14]:


sns.heatmap(df.corr())


# In[ ]:


sns.jointplot(y='Qty', x='Amount',data=df,kind='reg', color="#4CB391")


# In[ ]:


plt.hexbin(x, y, gridsize=(15, 15), cmap='Blues')
plt.xlabel('Amount')
plt.ylabel('Qty')
plt.title('Qty vs Amount')
plt.show()


# In[ ]:


Zero_Amount=df[df["Amount"]==0]
count_Zero_Amount = Zero_Amount.shape[0]

Zero_Qty=df[df["Qty"]==0]
count_Zero_Qty = Zero_Qty.shape[0]

print('Number of rows with Amount 0:',count_Zero_Amount)
print('Number of rows with Qty 0:',count_Zero_Qty)


# In[ ]:


# Group by 'Status' and calculate both sum of 'Amount' and count of 'Status'
Total_Amount= df.groupby('Status').agg({'Amount':'sum','Status':'count'})

# Rename the columns 
Total_Amount= Total_Amount.rename(columns={'Amount':'Total Amount', 'Status': 'Count_of_Status'})
print(Total_Amount)


# In[ ]:


total_cancelled_orders=( df['Status'] == 'Cancelled').sum()
print("Total cancelled orders:", total_cancelled_orders)


# # Total cancelled orders: 18332

# In[ ]:


Total_cancelled_Amount =df.loc[df["Status"] == 'Cancelled','Amount'].sum()
print("Total Amount of cancelled order:",Total_cancelled_Amount)


# # Total Amount of cancelled order: 6919284.3
