Google Reviews Spam Detector
This project is a Python application that downloads Google reviews for a given restaurant, preprocesses the reviews, and uses a pre-trained machine learning model to detect spam reviews. The application then flags any detected spam reviews and outputs a list of the flagged reviews.

Prerequisites
To run the application, you will need to have the following installed:

Python 3.x
Scikit-learn
Pandas
Google Maps Python client
OpenAI API key


Getting Started
Clone this repository to your local machine 
Install the required Python packages by running pip install -r requirements.txt in your terminal.
Obtain a Google Maps API key by following the instructions here.
Obtain an OpenAI API key by following the instructions here.
Replace YOUR_API_KEY in detect_spam_review.py with your OpenAI API key.
Replace YOUR_API_KEY in main.py with your Google Maps API key.
Run main.py in your terminal by running python main.py.
Note: The free Google Maps API tier limits the number of reviews that can be retrieved to 5. To retrieve more reviews, a paid Google Maps API plan is required. Additionally, the OpenAI API is a paid service, so to run the code successfully, you will need to have a valid OpenAI API key.

Usage
The application prompts the user to enter the name and location of the restaurant for which they want to download reviews. The location can be entered in the format of latitude and longitude coordinates or as an address. Once the reviews have been downloaded, preprocessed, and analyzed for spam, the application outputs a list of the flagged reviews.
