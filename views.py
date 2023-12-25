from flask import Blueprint, render_template

views = Blueprint("veiws", __name__)

@views.route("/")
def home():
  return render_template("index.html")

@views.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@views.route("/spotifychecker")
def spotifychecker():
    return render_template("spotifychecker.html")
