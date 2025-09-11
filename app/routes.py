from random import choice
from flask import render_template, jsonify
from app import app

# index page route
@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

# quotes route
@app.route("/quote")
def quote():

    quotes = {"Dune":[("Deep in the human unconscious is a pervasive need for a logical universe \
                       that makes sense. But the real universe is always one step beyond logic.",
                       "Frank Herbert"), 
                       ("When religion and politics travel in the same cart, the riders believe\
                         nothing can stand in their way. Their movements become headlong - faster\
                         and faster and faster. They put aside all thoughts of obstacles and forget\
                         the precipice does not show itself to the man in a blind rush until it's\
                         too late.", "Frank Herbert")],
              "Neuromancer":[("Cyberspace. A consensual hallucination experienced daily by billions\
                               of legitimate operators, in every nation.", "William Gibson"),
                               ("Night City wasn’t there for its inhabitants, but as a deliberately\
                                 unsupervised playground for technology itself.", "William Gibson")
                                 ]}
    book, quotes_list = choice(list(quotes.items()))
    quote, author = choice(quotes_list)
    return jsonify({"book": book, "quote": quote,"author": author})
