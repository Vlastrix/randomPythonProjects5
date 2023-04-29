from flask import Flask

# This code is my honor, made without looking at a solution


def make_bold(function):
    def wrapper1():
        text = function()
        modified_text = "<b>" + text + "</b>"
        return modified_text
    return wrapper1


def make_emphasize(function):
    def wrapper1():
        text = function()
        modified_text = "<em>" + text + "</em>"
        return modified_text
    return wrapper1


def make_underline(function):
    def wrapper1():
        text = function()
        modified_text = "<u>" + text + "</u>"
        return modified_text
    return wrapper1


app = Flask(__name__)

print(__name__)


@app.route("/bye")
@make_bold
@make_emphasize
@make_underline
def bye():
    return "Bye"


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
           '<p>I am not liking flash currently</p>' \
           '<p>You can press enter to enter another line with the same return</p>' \
           '<img src="https://www.citynews1130.com/wp-content/blogs.dir/sites/9/2017/06/05/cat.jpg">'




# Gets the variable from <name> and transfers it to python so we can use it
@app.route("/<name>/<int:n>")
def greet(name, n):
    return f"Hello there {name}, you are {n} years old!"


if __name__ == "__main__":
    app.run(debug=True)
