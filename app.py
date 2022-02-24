import random
from flask import Flask, render_template
from get_data import Getmovie
app = Flask(__name__)

@app.route('/')
def pageSetup():
    getCast = ', '.join(Getmovie.Getcast)
    return render_template("pageSetup.html", getTitle = Getmovie.Gettitle, getPoster = Getmovie.Getposter, getTagline = Getmovie.Gettagline, getOverview = Getmovie.Getoverview, getCast = getCast, getRatings = Getmovie.Getratings, getBoxOffice = Getmovie.Getrevenue)

if __name__ == '_main_':
    app.run(debug=True)