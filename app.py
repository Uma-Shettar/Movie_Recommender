import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

with open("movies.pkl", "rb") as f:
    movies = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html", movies_list = movies["title"].tolist())


@app.route('/recommendations', methods= ['POST'] )
def recommend():
    movie_title = request.form.get("movie") 
    movie_index = movies[movies["title"] == movie_title].index[0]

    similarity_score = similarity[movie_index]
    m_list = sorted(list(enumerate(similarity_score)), reverse= True,key= lambda x:x[1])[1:11]
    top_score = m_list[0][1]
    m_list = [(i, s) for i, s in m_list if s / top_score >= 0.5][:10]

    recommendations = []
    for i in m_list:
        recommendations.append({"title": movies.iloc[i[0]].title, "score": float(i[1])})

    return render_template("recommendation.html", recommendations=recommendations, selected_movie=movie_title)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)