from newsapi import NewsApiClient


class NewsFeed:

    def __init__(self, interest, from_param, to_param, language="en"):
        self.newsapi = NewsApiClient(api_key='your_api_key')
        self.interest = interest
        self.language = language
        self.from_param = from_param
        self.to_param = to_param

    def get(self):
        headlines = self.newsapi.get_everything(qintitle=self.interest,
                                                from_param=self.from_param,
                                                to=self.to_param,
                                                language=self.language)

        articles = headlines["articles"]
        email_body = ""

        for article in articles:
            email_body = email_body + article["title"] + "\n" + article["url"] + "\n\n"

        return email_body


if __name__ == "__main__":
    news_file = NewsFeed("gym", "en", "2023-09-02", "2023-09-04")
    results = news_file.get()
    print(results)

