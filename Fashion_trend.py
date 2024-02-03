#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
os.getcwd()


# In[9]:


os.getcwd()


# In[20]:


import pandas as pd
import numpy as np
dil =pd.read_csv('Fashion Dataset.csv')


# In[94]:


dil.iloc[:,1:11].head(1)


# In[32]:


Color_red=dil.loc[dil['colour']=='Red','price'].sum()
print('Total price where color is Red =',Color_red)


# In[35]:


dil['price'].max()


# In[47]:


total_price_red_nayo = dil.loc[(dil['colour'] == 'Red') & (dil['brand'] == 'Nayo'), 'price'].sum()

print("Total price where color is red and brand is Nayo:", total_price_red_nayo)


# In[55]:


total_red_prices_by_brand = dil[dil['colour'] == 'Red'].groupby('brand')['price'].sum()
print("Total price where colour is Red and grouped by brand:",total_red_prices_by_brand)


# In[69]:


import matplotlib.pyplot as plt
total_of_price_by_colour = dil.groupby('colour')['price'].sum()

total_of_price_by_colour.plot(kind='bar',color='skyblue',width=1)

plt.title('Total Price by Color')
plt.xlabel('Color')
plt.ylabel('Total Price')
plt.show()


# In[85]:


total_price_by_brand =dil.groupby('brand')['price'].sum()

filtered_brand = total_price_by_brand[total_price_by_brand>500000]

a=filtered_brand.sort_values().plot(kind='bar',color='skyblue')

for p in a.patches:
    a.annotate(str(p.get_height()),(p.get_x() + p.get_width()/2., p.get_height()), 
    ha='center', va='center', xytext=(0,10), textcoords='offset points')

plt.title('Total Price by Brand  > 500000')
plt.xlabel('Brand')
plt.ylabel('Total Price')
plt.show


# In[92]:


total_prices_by_colour_brand = dil.groupby(['brand','colour'])['price'].sum().reset_index()
print("Total price by colour by brand:",total_prices_by_colour_brand)


# In[149]:


mean_rating = dil['avg_rating'].mean() 
dil['avg_rating'].fillna(mean_rating, inplace=True)

# Group by 'brand' and calculate the average rating
mean_rating_by_brand = dil.groupby('brand')['avg_rating'].mean().reset_index()

# Find the brand with the highest mean rating
top_brand = mean_rating_by_brand.loc[mean_rating_by_brand['avg_rating'].idxmax()]

# Find the brand with the lowest mean rating
lowest_brand = mean_rating_by_brand.loc[mean_rating_by_brand['avg_rating'].idxmin()]

print("Brand with the Highest Mean Rating:")
print(top_brand)

print("\nBrand with the Lowest Mean Rating:")
print(lowest_brand)


# In[137]:


mean_rating_by_brand = dil.groupby('brand')['avg_rating'].mean().reset_index()
mean_rating_by_brand


# # Average Rating which is more than 4.5

# In[145]:


mean_rating_4 =mean_rating_by_brand[mean_rating_by_brand['avg_rating']>4.5]
mean_rating_3 


# # Average Rating which is Below 3.5

# In[146]:


min_mean_rating =mean_rating_by_brand[mean_rating_by_brand['avg_rating']<3.5]
min_mean_rating

