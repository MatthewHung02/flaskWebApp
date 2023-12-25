from flask import Flask, render_template

#from flask_bootstrap 
#install Bootstrap
#import Bootstrap
from website import create_app
app = create_app()

@app.route("/")
def base():
  return render_template('index.html')

@app.route("/aboutme")
def aboutme():
  return render_template('aboutme.html')

@app.route("/spotifychecker")
def spotifychecker():
  return render_template('spotifychecker.html')

if __name__ == '__main__':
        app.run(debug=True)
