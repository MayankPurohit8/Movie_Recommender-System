import streamlit as st
import pandas as pd
import pickle
import requests
import requests
import streamlit as st
st.markdown("""
    <style>
    .movie-title {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: block;
        width: 150px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
DEFAULT_POSTER = "nofound.png"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=66e8d9a6809e9a5532dd0a0a79e08be3&language=en-US"
    try:
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception as e:
         return DEFAULT_POSTER



def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate( similarity[movie_index])),reverse=True , key=lambda x :x[1])
    recommended_movies = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))

        recommended_movies.append(movies.iloc[i[0]].title)
    return  recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recomender System")
option = st.selectbox(
    "Select a movie to get recommendation😊",
    movies['title'].values,
)

if st.button('Recommend'):
    names, poster = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f'<p class="movie-title">{names[0]}</p>', unsafe_allow_html=True)
        if poster[0] != "":
            st.image(poster[0])

    with col2:
        st.markdown(f'<p class="movie-title">{names[1]}</p>', unsafe_allow_html=True)
        if poster[1] != "":
            st.image(poster[1])

    with col3:
        st.markdown(f'<p class="movie-title">{names[2]}</p>', unsafe_allow_html=True)
        if poster[2] != "":
            st.image(poster[2])

    with col4:
        st.markdown(f'<p class="movie-title">{names[3]}</p>', unsafe_allow_html=True)
        if poster[3] != "":
            st.image(poster[3])

    with col5:
        st.markdown(f'<p class="movie-title">{names[4]}</p>', unsafe_allow_html=True)
        if poster[4] != "":
            st.image(poster[4])


