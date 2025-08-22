import streamlit as st
import pandas as pd

import data_manager
import ui
import api_client
import fuzzy_search

# --- 1. Page Configuration & Initialization ---
st.set_page_config(layout='wide', page_title='HoshiTrack')
st.title('HoshiTrack 🔭')

# Initialize session state to handle the 'add media' action
if 'add_media' not in st.session_state:
    st.session_state['add_media'] = None


# --- 2. Load Local Data ---
df_entries = data_manager.load_entries()

# --- 3. Handle the 'Add Media' Action ---
# The block checks if a user clicked the 'Add to Library' button in the UI
if st.session_state['add_media']:
    media_to_add = st.session_state['add_media']

    # Check for duplicates before adding
    if not data_manager.is_duplicate(media_to_add['title'], df_entries):
        # Prepare the new entry with default values
        new_entry = {
            'title': media_to_add.get('title'),
            'media_type': 'Movie', # Defaulting to Movie (for now)
            'genre': media_to_add.get('genre', 'N/A'),
            'status': 'Plan to Watch', # Default status
            'progress': 'Not Started',
            'rating': 0,
            'poster_path': media_to_add.get('poster_path')
        }
        data_manager.save_entry(new_entry)
        st.success(f'\'{new_entry['title']}\' was added to your library!')
        # Reload data to show the new entry immediately
        df_entries = data_manager.load_entries()
    else:
        st.warning(f'\'{media_to_add['title']}\' is already in your library.')
    
    # IMPORTANT: Clear the session state to reset the action
    st.session_state['add_media'] = None

# --- 4. Display Search and Main Content ---
query = ui.show_search_bar()

if query:
    # Check if the DataFrame has data AND a 'title' column before searching
    if not df_entries.empty and 'title' in df_entries.columns:
        # Try to find a match in the local data using fuzzy search
        local_matches_info = fuzzy_search.find_best_matches(query, df_entries['title'])
    else:
        local_matches_info = [] # If no local data, treat as no matches

    if local_matches_info:
        match_indices = [match['index'] for match in local_matches_info]
        df_local_results = df_entries.loc[match_indices]
        ui.display_results(df_local_results, is_local=True)

    else:
        # If no local matches, search the TMDB API
        with st.spinner('Searching online...'):
            api_results = api_client.search_media(query)
            if api_results:
                ui.display_results(api_results, is_local=False)
            else:
                st.warning('No matches found locally or online.')
else:
    # By default (no search query), display the user's entire library
    ui.display_results(df_entries, is_local=True)