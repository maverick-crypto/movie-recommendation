import pickle
import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=0f87300450b36eee04d157aeceee17d4&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    index = movieData[movieData['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x: x[1])

    recommended = []
    recommended_posters = []
    for i in distances[1:10]:
        movie_id = movieData.iloc[i[0]].id
        recommended_posters.append(fetch_poster(movie_id))
        recommended.append(movieData.iloc[i[0]].title)

    return recommended, recommended_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movieData = pd.DataFrame(movies)

movie_list = movieData['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended, recommended_posters = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(recommended_posters[0])
        st.text(recommended[0])
    with col2:

        st.image(recommended_posters[1])
        st.text(recommended[1])

    with col3:

        st.image(recommended_posters[2])
        st.text(recommended[2])
    with col4:

        st.image(recommended_posters[3])
        st.text(recommended[3])

    col1, col2, col3, col4 = st.columns(4)
    with col1:

        st.image(recommended_posters[4])
        st.text(recommended[4])
    with col2:

        st.image(recommended_posters[5])
        st.text(recommended[5])

    with col3:

        st.image(recommended_posters[6])
        st.text(recommended[6])
    with col4:

        st.image(recommended_posters[7])
        st.text(recommended[7])


