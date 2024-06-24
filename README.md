# FIND IN X | Test Project

Find In X is a web application that allows you to search for tweets using a keyword and display the results in a user-friendly format. this method is done using Googles Custom Search Engine and Custom search API to search for tweets.

This `README.md` file provides a clear guide on how to set up and run the project, along with an overview of the project structure and required environment variables.

peace and bleassings to you friend.

>**Disclaimer**: This application is for informational purposes only.

## Table of Contents

- [FIND IN X | Test Project](#find-in-x--test-project)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Environment Variables](#environment-variables)
  - [Dependencies](#dependencies)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/note-xin/find-in-x.git
   cd find-in-x
   ```
   To adjust the time duration. You can change it in the `app.py` file.
   ```python
   # Function to search for tweets
    def search_tweets(query, date_range="d1"):
        try:
            service = build("customsearch", "v1", developerKey=API_KEY)
            result = service.cse().list(
                q=query,
                cx=CSE_ID,
                dateRestrict='h3'
            ).execute()
    ```
    The `date_range` and `dateRestrict` parameters.
    
    >**Note**: The default time is set to `h3` which means the last 3 hours.


2. **Create a virtual environment:**
    >**note**: You can skip this step if you prefer not to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Head over to the [Google Developers Console](https://console.developers.google.com/) and create a new project to get your Google API key and Custom Search Engine ID. And then 
    - go to your custom search engine control panel and configre it to `https://x.com/`.
    - Also, set filter by relevence.

   Create a `.env` file in the root directory of the project and add your Google API key and Custom Search Engine ID:
   ```
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_CSE_ID=your_custom_search_engine_id
   ```

## Usage

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your web browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

3. **Use the search form to enter a keyword and view the results.**

## Project Structure

```
project/
│
├── templates/
│   ├── index.html          # Main search page
│   ├── results.html        # Results display page
│
├── static/
│   ├── style.css           # CSS styles
│   ├── script.js           # JavaScript for search functionality
│   ├── results.js          # JavaScript for displaying results
│
├── app.py                  # Flask application
├── .env                    # Environment variables (not included in version control)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## Environment Variables

- `GOOGLE_API_KEY`: Your Google API key.
- `GOOGLE_CSE_ID`: Your Custom Search Engine ID.

## Dependencies

- Flask
- python-dotenv
- google-api-python-client