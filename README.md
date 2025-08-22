# HoshiTrack: A Personal Media Consumption Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

HoshiTrack is a simple web application built with Python and Streamlit to help track, visualize, and analyze all the media consumed. From movies and TV shows to books and podcasts, never lose track of what is once experienced.


## 🌟 Features
* **API-Powered Discovery:** Search for add new movies directly from The Movie Database (TMDB), complete with posters and release information.
* **Intelligent Local Search:** Uses a custom-built **fuzzy search algorithm** (Levenshtein distance) to find items in library even with typos.
* **Modern Card UI:** A clean, modern interface displays your media collection as interactive cards with posters, ratings, and status.
* **Simple Data Storage:** The media library is stored in a human-readable `data.json` file.

## 🚀 Usage

To run HoshiTrack on our local machine, follow these steps.

### 1. Prerequisites

* Python 3.9+
* An API Key from [The Movie Database (TMDB)](https://themoviedb.org/signup)

### 2. Installation

Clone the repository and install the required packages:
```bash
git clone git@github.com:shpiy/HoshiTrack.git
cd HoshiTrack
pip install -r requirements.txt
```

### 3. Configure API Key

Create a folder and file for your Streamlit secrets:
```bash
mkdir .streamlit
touch .streamlit/secrets.toml
```

Open the `secrets.toml` file and add your TMDB API key:
```bash
TMDB_API_KEY="paste_your_api_key_here"
```

### 4. Run the Application

Launch the Streamlit app from your terminal:
```bash
streamlit run App.py
```

The application should now be open and running in your web browser.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/shpiy/HoshiTrack/issues).

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
