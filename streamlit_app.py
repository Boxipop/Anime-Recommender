import streamlit as st
import pandas as pd
import joblib
import re

# 1. Load the files we saved in Step 1
df = pd.read_pickle("anime_data.pkl")
model = joblib.load("knn_model.pkl")
matrix = joblib.load("matrix.pkl")


# 2. Your smart cleaning function
def get_root(t):
    first_word = t.split()[0].lower()
    return re.sub(r'[^a-z0-9]', '', first_word)


# 3. The App Interface
st.set_page_config(layout="wide")  # Makes it look professional
st.title("🌸 Anime Recommender 🌸")
st.markdown("---")

# Search box
target_anime = st.selectbox("Search for an anime you love:", df['title'].values)

if target_anime:
    idx = df[df['title'] == target_anime].index[0]
    # We increase n_neighbors to 60 to ensure we find 10 unique series after filtering
    distances, indices = model.kneighbors(matrix[idx], n_neighbors=60)

    st.subheader(f"If you liked {target_anime}, you might enjoy:")

    seen_roots = {get_root(target_anime)}
    count = 0

    # Create a grid of 5 columns
    cols = st.columns(5)

    for i in indices[0]:
        row = df.iloc[i]
        root = get_root(row['title'])

        if root not in seen_roots:
            # This logic places 1-5 in the first row and 6-10 in the second row
            with cols[count % 5]:
                st.image(row['image'], use_container_width=True)
                st.write(f"**{row['title']}**")

            seen_roots.add(root)
            count += 1

        if count == 10:  # Stop once we hit 10 unique shows
            break

with st.expander("ℹ️ How the Recommendation System Works (Technical Details)"):
    st.write("""
    This recommender uses a **K-Nearest Neighbors (KNN)** algorithm to find anime with the most similar 'feel.' 
    Instead of just looking at names, it calculates a weighted score based on:
    """)

    # Create a small table to show your logic
    stats = {
        "Feature": ["Themes", "Synopsis", "Genres", "Demographics", "Studio", "Anime format (e.g. Series, Movie))"],
        "Weight": ["10.0", "5.0", "7.0", "15.0", "0.5", "0.5"],
        "Goal": ["Matches specific themes (e.g., Ninjas)", "Finds plot similarities", "Broad category matching",
                 "Target audience alignment (e.g. Shonen)", "Considers studio matches", "Considers anime format"]
    }
    st.table(stats)

    st.info(
        "**Methodology:** The text data is vectorized using TF-IDF, combined into a sparse matrix, and measured using Cosine Similarity.")