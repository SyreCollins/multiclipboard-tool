import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if (
        command == "save"
    ):  # this command would require a key and then save whatever is already on your normal clipboard to the multiclipboard data.
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved.")
    elif (
        command == "load"
    ):  # this command command would require a key and then copy the value of any key you pass in.
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print(
                f"The data in {key} is: {data[key]} \n Data has been copied to clipboard"
            )
        else:
            print("Key doesn't exist.")
    elif (
        command == "list"
    ):  # this command would list out every data stored in the multiclipboard.
        print(data)
    elif (
        command == "delete"
    ):  # this command would delete a value no longer needed based on its key.
        key = input("Enter key to delete value: ")
        if key in data:
            data.pop(key)
            save_data(SAVED_DATA, data)
            print(f"data has been deleted, Objects in clipboard: \n {data}")
    elif (
        command == "update"
    ):  # this command would require a key and update the value of that key to whatever input the user wants.
        key = input("Enter key to update value: ")
        if key in data:
            print(f"Current Value: {data[key]}")
            reverse_var = [data[key]]
            value_update = input("What do you want to update the value to? ")
            clipboard.copy(value_update)
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)

            print(
                f"'{key}' value has been updated. \n Previous Value: {reverse_var[0]} \n Current Value: {data[key]}"
            )
    else:
        print("Unknown command")

else:
    print("Please pass in exactly one command.")
