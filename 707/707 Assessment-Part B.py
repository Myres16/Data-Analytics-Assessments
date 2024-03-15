#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data_df = pd.read_csv('data.csv')


# In[4]:


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_mongodbclient():
    
    uri = 'mongodb+srv://707user:ADzgnRDrEQj3FqfD@707assessment.eld0gap.mongodb.net/?retryWrites=true&w=majority&appName=707Assessment'

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None
    
    
# Connect to MongoDB Atlas
client = get_mongodbclient()
# Initiate an instance of the database
db = client['Assessment2_707_Part_B'] 


# In[5]:


# f) Import the dataset into a table or collection within the database.
# In this case, import the data frame to the collection
data_records = data_df.to_dict(orient='records')
collection = db.data
collection.insert_many(data_records)


# In[33]:


# g) Retrieve and display records or documents from the table or collection.
# using collection.find to get all the records from adidas_collection
collection = db.data
data = collection.find()

new_data_df = pd.DataFrame(list(data))
new_data_df


# In[34]:


# h) Sort the records or documents based on a given condition.
# Sort by InvoiceDate
sorted_new_data_df = new_data_df.sort_values(by='InvoiceDate', ascending=False)
sorted_new_data_df


# In[35]:


# i) Count the number of records or documents present in the table or collection.(
collection = db.data
document_count = collection.count_documents({})
print(f'Total Documents in data: {document_count}')


# In[36]:


# j) Perform grouping operations on records or documents within the table or collection.
collection = db.data
grouping = [{
    "$group": {
        "_id" : "$Country",
        "count" : {"$sum" : 1}
    }
}]
result = list(collection.aggregate(grouping))
print(result)

