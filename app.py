import streamlit as st
import requests
import pickle
import pandas as pd
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# -----------------------------
# Load preprocessed movie data
# -----------------------------
with open('Model/movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# -----------------------------
# Function: Get movie recommendations
# -----------------------------
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx = movies[movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  # Get top 10 similar movies
        movie_indices = [i[0] for i in sim_scores]
        return movies[['title', 'movie_id']].iloc[movie_indices]
    except IndexError:
        st.error("Selected movie not found in dataset.")
        return pd.DataFrame(columns=['title', 'movie_id'])

# -----------------------------
# Function: Fetch movie poster from TMDB
# -----------------------------
def fetch_poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'

    # Session with retry strategy
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    try:
        response = session.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id={movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)

    if not recommendations.empty:
        st.subheader("Top 10 Recommended Movies:")

        # Display movies in a 2x5 grid
        for i in range(0, 10, 5):
            cols = st.columns(5)
            for col, j in zip(cols, range(i, i + 5)):
                if j < len(recommendations):
                    movie_title = recommendations.iloc[j]['title']
                    movie_id = recommendations.iloc[j]['movie_id']
                    poster_url = fetch_poster(movie_id)
                    with col:
                        st.image(poster_url, width=150)
                        st.caption(movie_title)
    else:
        st.warning("No recommendations available for this movie.")
