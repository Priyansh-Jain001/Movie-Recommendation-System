import streamlit as st
import pickle
import heapq

# -----------------------------
# Load data with caching
# -----------------------------
@st.cache_resource
def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies_list, similarity = load_data()

# -----------------------------
# Recommend function
# -----------------------------
def recommend(movie):
    movie_idx = movies_list[movies_list["title"] == movie].index[0]
    distances = list(enumerate(similarity[movie_idx]))

    # Get top 6 movies (including the selected one at index 0)
    top_movies = heapq.nlargest(6, distances, key=lambda x: x[1])

    movies = []

    for idx, _ in top_movies[1:]:  # skip the selected movie itself
        movies.append(movies_list.loc[idx, 'title'])

    return movies

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎬 Movie Recommender System")

select_movie = st.selectbox(
    "Select your :rainbow[favourite] movie",
    movies_list["title"]
)

st.write("You selected:", select_movie)

if st.button("Get Recommendations"):
    reco_movies = recommend(select_movie)

    st.subheader("✨ Recommended Movies:")
    for title in reco_movies:
        st.write("- ", title)
