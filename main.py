# Import necessary modules
import yagmail
from news import NewsFeed
import pandas
import datetime
import time


# Define a function to send emails
def send_email():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    # Create a NewsFeed object for the specified interest
    news_feed = NewsFeed(interest=row["interest"], from_param=yesterday, to_param=today)

    # Configure your email sender (replace with your actual email and password)
    sender = yagmail.SMTP(user="youremail@gmail.com", password="your-password")

    # Compose and send the email
    sender.send(to=row["email"],
                subject=f"Your {row['interest']} news for today!",
                contents=f"Hi {row['name']} \n"
                         f" See what is on about {row['interest']} today!\n"
                         f"{news_feed.get()}")


# Continuously run the code
while True:
    # Check if the current time is 20:49
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 49:
        # Read the data from the "people.csv" file
        df = pandas.read_csv("people.csv")

        # Iterate through the data and send emails to each person
        for index, row in df.iterrows():
            send_email()

    # Wait for 60 seconds before checking the time again
    time.sleep(60)
