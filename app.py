import streamlit as st
import pickle

movies_list = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie_idx = movies_list[movies_list["title"] == movie].index[0]
    distances = list(enumerate(similarity[movie_idx]))  # list of tuples (index, value)

    sorted_dist = sorted(distances, reverse=True, key=lambda x: x[1])  # sorting on the basis of distance

    movies = []
    movie_ids = []
    for i in range(1, 6):
        movie_idx = sorted_dist[i][0]
        movies.append(movies_list.loc[movie_idx, 'title'])
        movie_ids.append(movies_list.loc[movie_idx, 'movie_id'])


    return movies, movie_ids

st.title("Movie Recommender System")

select_movie = st.selectbox(
    "Select you :rainbow[favourite] movie",
    (movies_list["title"]),
)

st.write("You selected:", select_movie)

if st.button("Recommendations"):
    reco_movies, movie_id = recommend(select_movie)

    for i in range(5):
        st.write(reco_movies[i])
        # st.write(movie_id[i])


