#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


SalesTransactionDF=pd.read_csv('Sales Transaction v.4a.csv')
SalesTransactionDF


# In[3]:


SalesTransactionDF.isnull().sum()


# In[4]:


SalesTransactionDF['CustomerNo'].fillna('12835', inplace=True)


# In[5]:


SalesTransactionDF.isnull().sum()


# In[6]:


SalesTransactionDF.to_csv('Cleaned_SalesTransactionDF.csv')


# In[8]:


from google.cloud import storage

# Load service account credentials 
credentials_path = 'assessment-2-etl-95c16a484157.json'
storage_client = storage.Client.from_service_account_json(credentials_path)

# Bucket name
bucket_name = 'assessment2_bucket'
# Get the bucket
bucket = storage_client.get_bucket(bucket_name)

# Specify the remote filename in the bucket
blob = bucket.blob('Cleaned_SalesTransactionDF.csv')

# Upload the local file
blob.upload_from_filename('./Cleaned_SalesTransactionDF.csv')


# In[ ]:




