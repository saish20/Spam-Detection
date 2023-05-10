import os
import pandas as pd
import pickle
from util import preprocess_text, create_tfidf_vectorizer
from SpamDetection import detect_spam_review
from DownloadReviews import download_reviews
import streamlit as st

# Specify restaurant name and location
st.set_page_config(page_title="Google Reviews Spam Detector")
st.title("Google Reviews Spam Detector")

# Get user input for restaurant name and location
st.header("Enter the restaurant details below")
restaurant_name = st.text_input("Name")
location1 = st.text_input("Latitude")
location2 = st.text_input("Longitude")
restaurant_name = 'Dishoom Manchester'
restaurant_location = location1 + "," + location2

if st.button("Submit"):

    reviews = download_reviews(restaurant_name,restaurant_location)

    reviews['is_spam'] = reviews['text'].apply(detect_spam_review)

    spams  = reviews["is_spam" == True]["text"].tolist()

    if spams:
        st.header("Identified Spam Reviews")
        for i, spam in enumerate(spams):
            st.write(f"{i+1}. {spam}")    
    else:
        st.write("No spam reviews were identified.")