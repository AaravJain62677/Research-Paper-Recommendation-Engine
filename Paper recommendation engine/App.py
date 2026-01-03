import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("papers.csv")
df = df[['title','summary']]
df.dropna(inplace=True)
df['text'] = df['title'] + " " + df['summary']

vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
tfidf_matrix = vectorizer.fit_transform(df['text'])

def recommend(query, top_n=5):
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, tfidf_matrix)[0]
    top_idx = scores.argsort()[-top_n:][::-1]
    return df.iloc[top_idx][['title','summary']]

st.title("Academic Research Paper Recommendation Engine")

query = st.text_input("Enter your research interest")

if query:
    results = recommend(query)
    for _, row in results.iterrows():
        st.subheader(row['title'])
        st.write(row['summary'][:300] + "...")
