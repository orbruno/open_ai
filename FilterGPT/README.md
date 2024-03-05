
# ChatGPT Conversation Filter Script

This Python script is designed to filter ChatGPT conversation entries from a JSON file, retaining only those entries that contain a specific string defined by the user. It performs a case-insensitive search across all conversation entries, including nested dictionaries and lists.

## Prerequisites

Ensure that you have Python installed on your system. This script is compatible with Python 3.x versions.

## Setup Instructions

1. **Download ChatGPT Conversation History:**
   - Navigate to your ChatGPT interaction platform and download your conversation history, which should be in JSON format.

2. **Script Preparation:**
   - Place the downloaded `conversations.json` file in the same directory as this script.
   - If your JSON file has a different name, make sure to rename it to `conversations.json` or modify the script accordingly where it opens the JSON file.

3. **Configure the Search String:**
   - Open the script in a text editor or IDE.
   - Locate the `filter_string` variable in the script.
   - Replace `'text_to_be_filtered'` with your desired search string. Note that the search will be conducted in a case-insensitive manner.

## Running the Script

- Open a terminal or command prompt.
- Navigate to the directory containing the script and the `conversations.json` file.
- Run the script using the command: `python <script_name>.py`, replacing `<script_name>` with the actual name of the script file.

## Output

- Upon successful execution, the script will create a `conversations_filtered.json` file in the same directory. This file contains only the conversations that include the specified filter string.
- The search includes all levels of the JSON structure, ensuring no relevant data is missed.

## Important Notes

- The script is designed to be flexible and can handle nested JSON structures, thanks to its recursive search function.
- For large JSON files, the script execution time may vary.

## Contributions

Feedback and contributions are highly welcome. If you have any suggestions for improving this script or encounter any issues, please feel free to open an issue or submit a pull request on the repository.
