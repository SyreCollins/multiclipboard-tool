# multiclipboard-tool
MultiClipboard: A Command-Line Clipboard Manager
Overview
MultiClipboard is a simple command-line tool written in Python that allows you to manage and store multiple items in your clipboard. It provides commands for saving, loading, listing, updating, and deleting data associated with different keys.

Prerequisites
Before using this script, ensure you have Python installed on your system. The script uses the built-in json module and the clipboard library, which you can install using pip:

bash
Copy code
pip install clipboard
Usage
To use MultiClipboard, follow these steps:

Clone this repository or download the script directly.

Open the script (multiclipboard.py) in a Python code editor or IDE.

Customize the SAVED_DATA variable to specify the filepath where your clipboard data will be saved as a JSON file. By default, it's set to "clipboard.json."

Run the script using the command line, passing in one of the following commands:

save: This command requires a key and saves whatever is currently on your system clipboard to the MultiClipboard data under the specified key.

load: This command requires a key and copies the value associated with that key to your clipboard.

list: This command lists all data stored in the MultiClipboard.

delete: This command requires a key and deletes the data associated with that key from the MultiClipboard.

update: This command requires a key and updates the value associated with that key with user-specified input.

Example Usage:
  python multiclipboard.py save
  Enter a key: my_key
  data saved.

  python multiclipboard.py load
  Enter a key: my_key
  The data in my_key is: [clipboard_value]
  Data has been copied to clipboard.

  python multiclipboard.py list
  { "key1": "value1", "key2": "value2" }

  python multiclipboard.py delete
  Enter key to delete value: my_key
  Data has been deleted. Objects in clipboard: { "key2": "value2" }

  python multiclipboard.py update
  Enter key to update value: key2
  Current Value: value2
  What do you want to update the value to? new_value
  'key2' value has been updated. Previous Value: value2. Current Value: new_value
  
License
This script is provided under the MIT License.

I plan on releasing this code as an extension for vs code in the nearest future...a link would be provided when done.
