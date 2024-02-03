#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os
ab =pd.read_csv('pokemon_data.csv')
ab.head()


# In[4]:


df = pd.DataFrame(ab)

# Counting the total number of rows using shape
total_rows_shape = df.shape[0]

# Counting the total number of rows using len
total_rows_len = len(df)

print(f'Total Rows (using shape): {total_rows_shape}')
print(f'Total Rows (using len): {total_rows_len}')


# In[5]:


unique_value =df['Type 1'].unique()
print(unique_value)


# In[8]:


grouped_df=ab.groupby("Type 1")

mean_hp_per_type = grouped_df['HP'].mean()

fig = ab.bar(x=mean_hp_per_type.index, y=mean_hp_per_type.values, labels={'x': 'Type 1', 'y': 'Mean HP'},
             title='Mean HP per Type 1')
fig.show()


# In[49]:


unik1 =df["Generation"].unique()
print(unik1)


# In[ ]:




