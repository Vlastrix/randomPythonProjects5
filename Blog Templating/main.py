from flask import Flask, render_template
from requests import get

app = Flask(__name__)

blog_url = "https://api.npoint.io/735db34186544c5e408f"
response = get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    global all_posts
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:num>")
def blog(num):
    global all_posts
    print(num)
    return render_template("post.html", id=num, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
