# 🎬 Movie Recommender System

🚀 **Live Demo:** https://movie-recommender-gk1s.onrender.com

A content-based movie recommendation web app built with Python, Flask, and scikit-learn. Select a movie you like and get the most similar movies ranked by similarity.

---

## How It Works

Each movie is represented as a **meta-features vector** combining plot overview, tagline, cast, director, writer, genres, keywords, and movie era. These are vectorized using **CountVectorizer** and similarity between movies is computed using **cosine similarity**.

Only results scoring at least 50% relative to the top match are shown, filtering out weak recommendations automatically.

---

## Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn (CountVectorizer, Cosine Similarity)
- **Data:** pandas, numpy
- **Frontend:** HTML, CSS, Bootstrap 5
- **Deployment:** Render (gunicorn)

---

## Project Structure

```
Movie_Recommender/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── templates/
│   ├── home.html
│   └── recommendation.html
│
├── app.py               # Flask web application
├── model.ipynb          # Feature engineering, vectorization & similarity matrix generation
├── movies.pkl           # Pickled movie dataframe
├── requirements.txt     # Python dependencies
└── .gitignore
```

> `similarity.pkl` is not stored in the repo due to file size. It is downloaded automatically at startup from Google Drive using `gdown`.

---

## Dataset

[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle — ~5000 movies with metadata including genres, keywords, cast, crew, overview, and tagline.

---

## Local Setup
 
### Prerequisites
- Python 3.8+
- pip
### Steps
 
```bash
# 1. Clone the repo
git clone https://github.com/Uma-Shettar/Movie_Recommender.git
cd Movie_Recommender
 
# 2. Install dependencies
pip install -r requirements.txt
 
# 3. Start the app
python app.py
```
 
Visit `http://localhost:5000` in your browser.
 
> `similarity.pkl` is downloaded automatically on first run via `gdown`. This may take a moment.
 
> To retrain the model from scratch, run all cells in `model.ipynb` to regenerate `movies.pkl` and `similarity.pkl`.
 
---
 
## Deployment
 
Deployed on **Render**. Set the start command to:
 
```bash
gunicorn app:app
```
 
