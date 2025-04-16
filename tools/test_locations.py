import json
import requests

# URL of the JSON file
json_url = "https://pinjoa.github.io/commons/braga_locations.json"

# Fetch the JSON data
response = requests.get(json_url)
response.raise_for_status()  # Raise an exception for bad status codes
data = response.json()

# Initialize documents and iddocs
documents = list(data.values())
iddocs = list(data.keys())

print(f"Number of documents: {len(documents)}")
print(f"Number of document IDs: {len(iddocs)}")

# Verify the first few documents
print("\nFirst 3 Documents:")
for i in range(3):
    print(f"{iddocs[i]}: {documents[i][:50]}...")  # Print first 50 characters
