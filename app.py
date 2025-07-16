from flask import Flask, render_template, request # type: ignore
import pandas as pd # type: ignore
import pickle
import requests # type: ignore

app = Flask(__name__)

# Load movie data
movies_dict = pickle.load(open("movies_dictionary.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Function to get movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/300x450?text=No+Image"

# Recommendation function
def recommend(movie):
    # Finding the index of the selected movie
    index = movies[movies['title'] == movie].index[0]
    # Getting the similarity scores for the selected movie
    distances = similarity[index]
    # Sorting the movies based on similarity scores
    # Excluding the first movie (itself) and getting the top 5 recommendations
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Fetching recommended movie titles and posters for display
    recommended_titles = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_titles, recommended_posters

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended = []
    posters = []
    selected_movie = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        recommended, posters = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=movies['title'].values,
        selected_movie=selected_movie,
        recommended=recommended,
        posters=posters
    )

if __name__ == '__main__':
    app.run(debug=True)
