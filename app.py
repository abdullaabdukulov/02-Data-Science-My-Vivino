import streamlit as st
import pickle
import pandas as pd

wines = pickle.load(open("wines.pkl", 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
wines_name = wines['Full name'].values

st.header("Wine Recommender System")
select_wine = st.selectbox("Select wine from", wines_name)


def recommend(wine):
    index = wines[wines['Full name'] == wine].index[0]
    similarity_score = list(enumerate(similarity[index]))
    sorted_similar_vines = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommend_wine = []
    for i, dist in sorted_similar_vines:
        if pd.notna(dist):
            recommend_wine.append({
                'Full name': wines.iloc[i]['Full name'],
                'Image': wines.iloc[i]['Image'],
                'Price': wines.iloc[i]['Price'],
                'Description': wines.iloc[i]['Description'],
                'Similarity Score': dist  # Add similarity score to the dictionary
            })
    return recommend_wine[:5]


if st.button("Show Recommendations"):
    recommended_wines = recommend(select_wine)
    for wine in recommended_wines:
        st.text(wine['Full name'])
        st.image(wine['Image'])
        st.write(f"Price: {wine['Price']} €")
        st.write(f"Similarity Score: {wine['Similarity Score'] * 100:.1f}%")
        st.write(f"Description: {wine['Description']}")
        st.markdown("<br><br>", unsafe_allow_html=True)




