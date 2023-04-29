from flask import Flask, render_template
import random
import time
from requests import get

app = Flask(__name__)


@app.route("/")
def blog_old():
    random_number = random.randint(1, 10)
    current_year = time.strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    response = get(f"https://api.genderize.io/?name={name}")
    gender = response.json()["gender"]
    response = get(f"https://api.agify.io/?name={name}")
    age = response.json()["age"]
    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/735db34186544c5e408f"
    response = get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
