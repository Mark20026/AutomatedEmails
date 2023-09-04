import yagmail
from news import NewsFeed
import pandas
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    news_feed = NewsFeed(interest=row["interest"],
                         from_param=yesterday,
                         to_param=today)
    # Type your email and app password here
    sender = yagmail.SMTP(user="youremail@gmail.com",
                          password="yourpassword")
    sender.send(to=row["email"],
                subject=f"Your {row['interest']} news for today!",
                contents=f"Hi {row['name']} \n"
                         f" See what is on about {row['interest']} today!\n"
                         f"{news_feed.get()}")


while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 49:
        df = pandas.read_csv("people.csv")

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
