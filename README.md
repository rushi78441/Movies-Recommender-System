# Movies-Recommender-System

This is my first mini Project based on Recommender Systems.I used Content-based Filtering algorithm in which I used Cosine similarity to find most relative movies based on movies tags. I used lemmatizer and Bag of Word for text preprocessing and also used TMDB api to render movies poster and used database of TMDB
## 🧠 Content-Based Filtering Algorithm Steps

### ✅ Data Collection:
- Title  
- Genres  
- Cast  
- Overview/Description  
- Keywords, Tags  

### ✅ Feature Engineering:
- Combine all these attributes into a single string/text per movie.  
- Example: `"action adventure space alien war tom cruise"`  

### ✅ Text Vectorization:
- Convert text into numbers using **CountVectorizer** or **TF-IDF Vectorizer**.  
- This turns your movie corpus into a matrix of token counts (or TF-IDF scores).  

### ✅ Similarity Calculation:
- Use **Cosine Similarity** between movie vectors.  
- This creates a `similarity.pkl` matrix where `similarity[i][j]` tells how similar movie `i` is to movie `j`.

#### 📐 Cosine Similarity Formula:
- Cosine similarity between two vectors A and B is given by:
- cosine similarity(A, B) = (A . B) / (||A|| * ||B||)


Where: