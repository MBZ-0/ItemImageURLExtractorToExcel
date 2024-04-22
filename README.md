**Google Custom Search Image URL Fetcher**
This script fetches image URLs using the Google Custom Search API for a given list of items. It then stores the item names along with their corresponding image URLs in a pandas DataFrame and saves it to an Excel file.

**Features:**
Utilizes the Google Custom Search API to search for images related to a list of items.
Retrieves the first image URL (larger image) for each item.
Stores the item names and their respective image URLs in a pandas DataFrame.
Saves the DataFrame to an Excel file named item_list_file.xlsx.

**Requirements:**
requests: For making HTTP requests to the Google Custom Search API.
json: For parsing the JSON response from the API.
pandas: For creating and manipulating the DataFrame.
xlrd and openpyxl: For saving the DataFrame to an Excel file.

**Usage:**
1. Replace API_KEY and CSE_ID with your Google Custom Search API key and Custom Search Engine ID.
2. Populate items_list with the items for which you want to fetch image URLs.
3. Run the script to fetch image URLs and save them to an Excel file.
