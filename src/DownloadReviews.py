import googlemaps
import json
import pandas as pd


def download_reviews(restaurant_name,restaurant_location):
    # Set up Google Maps API client
    gmaps = googlemaps.Client(key='API_KEY')



    # Make API request to get place ID for restaurant
    place_result = gmaps.find_place(input=restaurant_name, input_type='textquery', fields=['place_id'])

    # Extract place ID from response
    place_id = place_result['candidates'][0]['place_id']

    # Make API request to get details for restaurant
    place_details = gmaps.place(place_id=place_id, fields=['name', 'rating', 'reviews'])

    # Extract reviews from response
    reviews = place_details['result']["reviews"]

    # Convert reviews to pandas DataFrame
    reviews_df = pd.DataFrame.from_dict(reviews)

    return reviews_df
