import streamlit as st
import api_client

def show_search_bar():
    '''Displays a search bar and returns the user's query.'''
    query = st.text_input(
        'Search to add from TMDB for find in our library',
        '',
        placeholder='e.g., The Matrix, Dune, etc.'
    )
    return query

def display_media_card(item, is_local):
    '''
    Displays a single media item as a card
    'item' can be a dictionary from the API or a row from the local DataFrame.
    '''

    # Use the item's title or another unique identifier for the key
    unique_key = item.get('id', item.get('title', ''))

    # Get the full poster URL
    poster_url = api_client.get_poster_url(item.get('poster_path'))

    # Use a placeholder if no poster is available
    if not poster_url:
        poster_url = 'https://via.placeholder.com/500x750.png?text=No+Image'

    # Create a container for each card for better styling
    with st.container(border=True):
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(poster_url)

        with col2:
            st.subheader(item.get('title', 'No Title'))

            if is_local:
                # Display details for items already in the library
                st.caption(f'Status: {item.get('status', 'N/A')}')
                st.progress(item.get('rating', 0) * 20, text=f'Rating: {item.get('rating', 0)}/5')
                st.write(f'Genre: {item.get('genre', 'N/A')}')
            else:
                # Display details for items from the API search
                release_date = item.get('release_date', 'N/A')
                st.caption(f'Released: {release_date}')

                # The 'Add to Library' button
                if st.button('Add to Library', key=f'add_{unique_key}'):
                    # When clicked, we rerun the script with the item's info stored in session state
                    st.session_state['add_media'] = item

def display_results(results, is_local):
    '''
    Displays a list of media items.
    'results' can be an API response (list of dicts) or a local DataFrame.
    '''

    if is_local:
        st.subheader('Found in your library:')
        # Iterate over DataFrame rows
        for _, row in results.iterrows():
            display_media_card(row, is_local=True)
    else:
        st.subheader('Found online (from TMDB):')
        # Iterate over list of dictionaries from API
        for item in results:
            display_media_card(item, is_local=False)