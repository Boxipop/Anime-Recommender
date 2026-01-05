# Anime Recommender
## [Web Application Link](https://anime-recommender-application.streamlit.app/)
Built a full-stack machine learning web application that uses K-Nearest Neighbors (KNN) to suggest anime based on user preferences. The model takes in an anime from the user and returns the top 10 most similar anime based off the following features: Demographics (e.g. Shonen), Themes (e.g. Time Travel), Genres (e.g. Action), Synopsis, Studio, and Anime Type (e.g. Series, Movie). 

## Data Collection
All anime data was obtained through Jikan, an unofficial and open-source API for MyAnimeList (the world's most active online anime and manga community and database). The anime data that was used consisted of the first 200 pages of top anime results in MyAnimeList. The reason I focused on top anime was because of the desire for high quality data (more common in top rated anime), which allowed my model to output the best results possible and also recommend anime with high ratings.

## Feature Consideration for Model (the types and weights)
After lots of experimenting with the types of features (variables) to include and their relative weight to each other in the recommendation system, the combination of features that were found to output the most promising results consisted of demographcis (weight 15), Themes (weight 10), Genres (weight 7), Synopsis (weight 5), Anime Type (weight 0.5), and Studio (weight 0.5). For reference, the standard weight is 1. Demographics had the highest weight as I first and foremost wanted to make sure the model was recommending anime for the same target audience as the one inputted. Themes was the second highest weighed feature as it considered the nuanced characteristics of an anime which would be important for matching anime with similar characteristics. Themes had more specific and identifying information of an anime, more so than genre (e.g. martial arts and military (theme) is more specific and useful than just action or adventure (genre)). Genre was used to ensure that the anime recommended falled under the same broad category/categories as the input anime. 

## Making the Recommendation System Interactive 
In order to make my recommendation system easily accessible and interactive, I built and deployed a web application using Streamlit.  
