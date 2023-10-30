import pandas as pd
import os
from pymongo import MongoClient

# Load data from the CSV file into a pandas DataFrame
data = pd.read_csv('versioned_data.csv')

# Convert the DataFrame to a list of dictionaries (each row is a dictionary)
data_dict = data.to_dict(orient='records')

# Connect to the MongoDB instance in your development environment (replace with your MongoDB connection string)
MONGODB_URI = os.environ.get('MONGODB_URI_DEV')
client = MongoClient(MONGODB_URI)

# Select (or create) the database in your development environment
db = client.surveyDB_dev

# Select (or create) the collection in your development environment
collection = db.answers_dev

# Insert each document from the loaded data
for document in data_dict:
    # Insert the document into MongoDB
    collection.insert_one(document)

print("Documents inserted into development environment successfully!")

# Close the connection
client.close()
