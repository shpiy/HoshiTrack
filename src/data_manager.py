import json
import pandas as pd

DATA_FILE = "data.json"

def load_entries():
    '''Loads all entries from the JSON file into a DataFrame.'''
    try:
        # Use orient='records' to handle list of dicts gracefully
        df = pd.read_json(DATA_FILE, orient='records')
        return df
    except (FileNotFoundError, ValueError):
        # Return an empty DataFrame if file doesn't exist or is empty/invalid
        return pd.DataFrame()
    
def save_entries(new_entry):
    '''Appends a new entry to JSON data file.'''
    df = load_entries()

    # Use pd.concat to add the new entry (as a single-row DataFrame)
    new_df = pd.DataFrame([new_entry])
    df = pd.concat([df, new_df], ignore_index=True)

    # Save back to JSON
    df.to_json(DATA_FILE, orient='records', indent=4)

def is_duplicate(title, df):
    '''Checks if a title already exists in the DataFrame.'''
    if 'title' in df.columns:
        return title.lower() in df['title'].str.lower().values
    return False