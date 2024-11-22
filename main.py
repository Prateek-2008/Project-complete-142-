from flask import Flask, jsonify, request # type: ignore
import pandas as pd # type: ignore
from demographic_filtering import output
from content_filtering import get_recommendations

articles_data = pd.read_csv('articles.csv')

all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = [['url' , 'title' , 'text' , 'lang' , 'total_events']]
not_liked_articles = [['url' , 'title' , 'text' , 'lang' , 'total_events']]
popular_article=[['url' , 'title' , 'text' , 'lang' , 'total_events']]
recommended_article=[["url" , "title" , "text" , "lang"]]

app = Flask(__name__)

def assign_val():

    m_data = {

        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]/2

    }
    return m_data

@app.route("/get-article")

def get_article():

    article_info = assign_val()
    return jsonify({

        "data": article_info,
        "status": "success"

    })

@app.route("/liked-article")

def liked_article():

    global all_articles
    article_info = assign_val()
    liked_articles.append(article_info)
    all_articles.drop([0], inplace=True)
    liked_articles = all_articles.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

@app.route("/unliked-article")
def unliked_article():
    global all_articles
    article_info = assign_val()
    not_liked_articles.append(article_info)
    all_articles.drop([0], inplace=True)
    unliked_article = all_articles.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

# API to return most popular articles.
@app.route("/popular-articles")
def popular_articles():
    global all_articles
    article_info = assign_val()
    popular_article.append(article_info)
    all_articles.drop([0,1,2,3,4,5,6], inplace=True)
    popular_article = all_articles.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

# API to return top 10 similar articles using content based filtering method.
@app.route("/recommended-articles")
def recommended_articles():
    global all_articles
    article_info = assign_val()
    recommended_article.append(article_info)
    all_articles.drop([0,1,2,3,4,5,6,7,8,9], inplace=True)
    all_articles = all_articles.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

if __name__ == "__main__":
    app.run()