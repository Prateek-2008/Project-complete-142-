from sklearn.feature_extraction.text import CountVectorizer# type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

df = pd.read_csv('articles.csv')
df = df[df['title'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['title'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df = df.reset_index()
indices = pd.Series(df.index, index=df['contentId'])

def get_recommendations(contentId):
    idx = indices[int(contentId)]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    return df[[ "url" , "title" , "text" , "lang" , "total_events" ]].iloc[article_indices]

