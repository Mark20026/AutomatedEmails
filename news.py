# Import the necessary module for accessing news data
from newsapi import NewsApiClient


# Define a class called NewsFeed to retrieve news articles
class NewsFeed:

    # Constructor to initialize the class with required parameters
    def __init__(self, interest, from_param, to_param, language="en"):
        # Initialize NewsApiClient with your API key (replace 'your_api_key' with your actual API key)
        self.newsapi = NewsApiClient(api_key='your_api_key')
        self.interest = interest  # The topic or interest for which news is retrieved
        self.language = language  # Language for the news (default is English)
        self.from_param = from_param  # Start date for news retrieval
        self.to_param = to_param  # End date for news retrieval

    # Method to retrieve and format news articles
    def get(self):
        headlines = self._get_headlines()  # Call the private method to get news data

        articles = headlines["articles"]  # Extract the articles from the retrieved data
        email_body = ""  # Initialize an empty string to store the email content

        # Iterate through each article and append its title and URL to the email_body
        for article in articles:
            email_body = email_body + article["title"] + "\n" + article["url"] + "\n\n"

        return email_body  # Return the formatted email content

    # Private method to fetch news headlines
    def _get_headlines(self):
        # Use the NewsApiClient to retrieve news articles based on specified parameters
        headlines = self.newsapi.get_everything(qintitle=self.interest,
                                                from_param=self.from_param,
                                                to=self.to_param,
                                                language=self.language)
        return headlines  # Return the retrieved headlines


# Main section to demonstrate the NewsFeed class
if __name__ == "__main__":
    # Create a NewsFeed instance with specific parameters (interest, language, from_param, to_param)
    news_file = NewsFeed("gym", "en", "2023-09-02", "2023-09-04")

    # Retrieve and print the formatted news content
    results = news_file.get()
    print(results)
