import yagmail

sender = yagmail.SMTP(user="youremail@gmail.com", password="yourpassword")
sender.send(to="recieveremail",
            subject="Hello",
            contents="asd")
