#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install PyPDF2')
get_ipython().system('pip install pdfplumber')
get_ipython().system('pip install pandas')


# In[5]:


import pdfplumber

with pdfplumber.open('Millenium Yogesh Two.pdf') as pdf:
    text1 = ''
    for page in pdf.pages:
        text1 += page.extract_text()
print(text1)


# In[6]:


import re

amounts = re.findall(r'€\d+(?:,\d{3})*(?:\.\d{2})?',text1)
percentages = re.findall(r'\b\d+(?:\.\d+)?%',text1)
financial_metrics = re.findall(r'\b(?:NOI|Debt Yield)\b.*?(\d+(?:,\d{3})*(?:\.\d+)?)',text1)

# Print the extracted information
print("Amounts:", amounts)
print("Percentages:", percentages)
print("Financial Metrics:", financial_metrics)


# In[8]:


import re
import pandas as pd

# Sample document content
document_content = """
...  # (Amounts: ['€6']
Percentages: ['87%', '40%', '78%', '4.25%', '6.72%', '87%', '87%', '40%', '40%', '50%', '51%', '67%', '2.86%', '3.45%', '3.30%', '3.30%', '3.43%', '3.55%', '27%', '3.4%', '9.2%', '4.25%', '6.72%']
Financial Metrics: [])
"""

# Extract figures related to financing request
amounts = re.findall(r'€\d+(?:,\d{3})*(?:\.\d{2})?', document_content)
percentages = re.findall(r'\b\d+(?:\.\d+)?%', document_content)
financial_metrics_matches = re.findall(r'\b(?:NOI|Debt Yield)\b.*?(\d+(?:,\d{3})*(?:\.\d+)?)', document_content)

# Extracted financial metrics with labels
financial_metrics = {
    'NOI': [financial_metrics_matches[0]] if financial_metrics_matches else ['N/A'],
    'Debt Yield': [financial_metrics_matches[1]] if len(financial_metrics_matches) > 1 else ['N/A'],
}

# Separate percentages and numerical values in Financial Metrics
percentages_in_metrics = [value for value in financial_metrics['NOI'] + financial_metrics['Debt Yield'] if '%' in value]
numerical_values_in_metrics = [value.replace(',', '') for value in financial_metrics['NOI'] + financial_metrics['Debt Yield'] if '%' not in value]

# Determine the maximum length among amounts, percentages, and lists of financial metrics values
max_length = max(len(amounts), len(percentages), len(percentages_in_metrics), len(numerical_values_in_metrics))

# Pad lists to the maximum length
amounts += ['N/A'] * (max_length - len(amounts))
percentages += ['N/A'] * (max_length - len(percentages))
percentages_in_metrics += ['N/A'] * (max_length - len(percentages_in_metrics))
numerical_values_in_metrics += ['N/A'] * (max_length - len(numerical_values_in_metrics))

# Create a DataFrame
data = {
    'Amounts': amounts,
    'Percentages': percentages,
    'NOI': percentages_in_metrics[:max_length],
    'Debt Yield': numerical_values_in_metrics[:max_length],
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)


# In[ ]:




