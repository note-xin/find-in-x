from flask import Flask, render_template, request, jsonify
import os
import json
import requests
from datetime import datetime, timezone, timedelta
from googleapiclient.discovery import build
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Reading your Google API key and Custom Search Engine ID
API_KEY = os.getenv('GOOGLE_API_KEY')
CSE_ID = os.getenv('GOOGLE_CSE_ID')

# Function to search for tweets
def search_tweets(query, date_range="d1"):
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        result = service.cse().list(
            q=query,
            cx=CSE_ID,
            dateRestrict='h3'
        ).execute()

        # Return the raw API response
        return result.get('items', [])
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to extract tweet details
def process_data(raw_data):
    extracted_data = []
    for item in raw_data:
        # Initialize variables to store the latest dates
        latest_date_created = "0000-00-00T00:00:00.000Z"
        latest_date_published = "0000-00-00T00:00:00.000Z"

        # Iterate through each post to find the latest dates
        for post in item['pagemap']['socialmediaposting']:
            if post['datecreated'] > latest_date_created:
                latest_date_created = post['datecreated']
            if post['datepublished'] > latest_date_published:
                latest_date_published = post['datepublished']

        extracted_item = {
            'title': item.get('title', ''),
            'link': item.get('link', ''),
            'snippet': item.get('snippet', ''),
            'htmlSnippet': item.get('htmlSnippet', ''),
            'datecreated': latest_date_created,
            'datepublished': latest_date_published
        }
        extracted_data.append(extracted_item)

    return extracted_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('keyword')
    raw_data = search_tweets(query)
    processed_data = process_data(raw_data)
    return jsonify(processed_data)

if __name__ == "__main__":
    app.run(debug=True)
