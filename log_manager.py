import json

LOG_FILE = "logbook.json"

def load_logbook():
    """
    Loads the logbook from the JSON file.
    Returns an empty list if the file doesn't exist or is empty.
    """
    try:
        with open(LOG_FILE, "r") as f:
            logbook = json.load(f)
        return logbook
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or is empty/corrupted, start fresh
        return []

def save_logbook(logbook_data):
    """
    Saves the entire logbook list to the JSON file.
    """
    try:
        with open(LOG_FILE, "w") as f:
            json.dump(logbook_data, f, indent=4)
        return True # Return True on success
    except Exception as e:
        print(f"Error saving logbook: {e}")
        return False # Return False on failure