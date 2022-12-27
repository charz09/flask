from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

# Create a route decorator


# def index():
#     return "<h1>Why always hello world?!</h1>"


'''safe
capitalize
lower
upper
title
trim
striptags'''

@app.route('/')

def index():
    favourite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
    example = "This is a <strong>BOLD</strong> text to post"
    first_name = "Charles Ikusan"
    return render_template("index.html", first_name=first_name, example=example,favourite_pizza=favourite_pizza)

@app.route('/user/<name>')

# def user(name):
#     return "<h1>Merry Christmas {}!!!</h1>".format(name)

def user(name):
    return render_template('user.html', cool_name=name)


# Custom Error Pages

# Invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Error status notification
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


