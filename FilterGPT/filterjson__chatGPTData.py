import json

# Specify the string to be filtered
filter_string = 'text_to_be_filtered'

# Load the JSON data from the 'conversations.json' file
with open('conversations.json') as f:
    data = json.load(f)

# Function to check if a JSON object contains a specific string
# This function is recursive and will check all nested dictionaries and lists
def contains_string(obj, string):
    if isinstance(obj, dict):  # If the object is a dictionary
        # Check if any of the values in the dictionary contain the string
        return any(contains_string(v, string) for v in obj.values())
    elif isinstance(obj, list):  # If the object is a list
        # Check if any of the items in the list contain the string
        return any(contains_string(v, string) for v in obj)
    elif isinstance(obj, str):  # If the object is a string
        # Check if the string contains the filter string
        return string in obj.lower()
    else:  # If the object is neither a dictionary, a list, nor a string
        return False

# Filter the JSON data
# Only keep items that contain the filter string
filtered_data = [item for item in data if contains_string(item, filter_string)]

# Save the filtered JSON data to the 'conversations_filtered.json' file
with open('conversations_filtered.json', 'w') as f:
    json.dump(filtered_data, f)