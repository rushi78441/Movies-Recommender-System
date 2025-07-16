# Movies-Recommender-System

This is my first mini Project based on Recommender Systems.I used Content-based Filtering algorithm in which I used Cosine similarity to find most relative movies based on movies tags. I used lemmatizer and Bag of Word for text preprocessing and also used TMDB api to render movies poster and used database of TMDB

## 🧠Content-Based Filtering Algorithm Steps
### Data Collection:
##### Title
##### Genres
##### Cast
##### Overview/Description
##### Keywords, Tags

## Feature Engineering:
##### Combine all these attributes into a single string/text per movie.
##### Example: "action adventure space alien war tom cruise"

## Text Vectorization:
##### Convert text into numbers using CountVectorizer or TF-IDF Vectorizer.
##### This turns your movie corpus into a matrix of token counts (or TF-IDF scores).

## Similarity Calculation:
##### Use Cosine Similarity between movie vectors.
##### This creates a similarity.pkl matrix where similarity[i][j] tells how similar movie i is to movie j.

## Recommendation:
##### When a user selects a movie, find its row in the similarity matrix.
##### Sort other movies based on similarity score.
##### Return top 5 most similar movies.

## 🔧 Tools Used in Your Project
##### Feature extraction --> Tag-based text
##### Vectorization --> CountVectorizer 
##### Similarity measure --> Cosine Similarity

## 💡 Example
##### If the user selects "Interstellar", the algorithm looks at its:
##### Genre: Sci-fi, Drama
##### Keywords: space, time, blackhole
##### Description
##### Then it finds other movies with similar content vectors like:
##### Gravity
##### The Martian
##### 2001: A Space Odyssey

