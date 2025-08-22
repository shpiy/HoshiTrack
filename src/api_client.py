import streamlit as st
import requests

# Retrieve the API key from Streamlit secrets
API_KEY = st.secrets['TMDB_API_KEY']
BASE_URL = 'https://api.themoviedb.org/3'

def search_media(query):
    '''Searches for movies on TMDB based on a query.'''
    search_url = f'{BASE_URL}/search/movie'
    params = {
        'api_key': API_KEY,
        'query': query
    }

    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        results = response.json().get('results', [])

        formatted_results = []
        for item in results:
            formatted_results.append({
                'title': item.get('title'),
                'genre': item.get('genre_ids'), # Genre IDs mapped to names later
                'release_date': item.get('release_date'),
                'poster_path': item.get('poster_path')
            })
            return formatted_results
    else:
        # Return an empty list if there's an error
        return []
    
def get_poster_url(poster_path, size='w500'):
    '''Returns the full URL for a movie poster.'''
    if poster_path:
        return f'https://image.tmdb.org/t/p/{size}{poster_path}'
    return None # Or a placeholder image URL
