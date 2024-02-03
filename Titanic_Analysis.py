#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[70]:


titanic =pd.read_csv('titanic_train.csv')
titanic.head(1)


# In[49]:


#titanic.isnull()


# In[106]:


survived_1 = titanic[titanic['Survived'] == 1]
avg_age_by_group = survived_1.groupby(['Sex','Pclass','Survived']).agg({'Age': ['count', 'mean']}).reset_index()
avg_age_by_group.columns = ['Sex', 'Pclass','Survived', 'Count', 'Average_Age']
print(avg_age_by_group)


# In[50]:


sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap="flare")


# In[51]:


sns.set_style("whitegrid")
sns.countplot(x="Survived",data=titanic, hue='Sex',palette='rainbow')


# In[52]:


ax=sns.countplot(x="Survived",hue="Pclass",data=titanic,palette="rainbow")
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Show the plot
plt.show()


# In[68]:


sns.distplot(titanic["Age"].dropna(),kde=True,bins=40,color="darkblue")


# In[54]:


sns.countplot(x="SibSp",data=titanic)


# In[55]:


titanic["Fare"].hist(color="green",bins=10,figsize=(8,4))


# In[56]:


sns.boxplot(x="Pclass",y="Age",data=titanic,palette="winter")
plt.figure(figsize=(12,7))


# In[57]:


def impute_age(cols):
    Age = cols[0]
    Pclass =cols[1]
    
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        
        elif Pclass==2:
            return 29
        
        elif Pclass==3:
            return 24
    else:
        return Age


# In[58]:


titanic["Age"] = titanic[["Age","Pclass"]].apply(impute_age, axis=1)


# In[59]:


sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap="flare")


# In[60]:


titanic.drop("Cabin",axis=1,inplace=True)


# In[61]:


titanic.head(1)


# In[62]:


Sex=pd.get_dummies(titanic["Sex"], drop_first= True)
Embarked=pd.get_dummies(titanic["Embarked"], drop_first= True)


# In[63]:


titanic=pd.concat([titanic,Sex,Embarked],axis=1)
titanic.head(1)


# In[64]:


titanic.drop(["Sex","Name","Embarked","Ticket"],axis=1, inplace=True)
titanic.head(1)


# In[44]:


#titanic.drop(["Survived"],inplace=True,axis=1)


# In[65]:


titanic.head()


# In[66]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Perform train-test split
x_train, x_test, y_train, y_test = train_test_split(
    titanic.drop("Survived", axis=1),
    titanic["Survived"],
    test_size=0.30,
    random_state=101)

# Scale the data using StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Initialize the Logistic Regression model with an increased max_iter
logmodel = LogisticRegression(max_iter=1000)

# Train the model on the scaled training data
logmodel.fit(x_train_scaled, y_train)

# Make predictions on the scaled test set
y_pred = logmodel.predict(x_test_scaled)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


# In[ ]:




