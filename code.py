import requests
import json
import pandas as pd

# Your Google Custom Search API key
API_KEY = ''

# Your Custom Search Engine ID
CSE_ID = ''

# Your items list
items_list = []


def get_image_url(query):
    url = f'https://www.googleapis.com/customsearch/v1?q={query}&cx={CSE_ID}&searchType=image&key={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Extract the first image URL (larger image)
    if 'items' in data and len(data['items']) > 0:
        return data['items'][0]['link']
    else:
        return None

# Fetch image URLs for each item
image_urls = {}
for item in items_list:
    image_url = get_image_url(item)
    if image_url:
        image_urls[item] = image_url
        print(f"Fetching image for {item}: {image_url}")
    else:
        print(f"No image found for {item}")

# Convert the dictionary to a DataFrame
df = pd.DataFrame(list(image_urls.items()), columns=['Item', 'Image URL'])

# Save the DataFrame to an Excel file
df.to_excel('item_list_file.xlsx', index=False)
