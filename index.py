from flask import Flask
from views import views

def create_app():
    app = Flask(__name__, template_folder="website/templates")
    return app

app = create_app()

app.register_blueprint(views, url_prefix='/')

'''

@app.route("/")
def base():
  return render_template('index.html')

@app.route("/aboutme")
def aboutme():
  return render_template('aboutme.html')

@app.route("/spotifychecker")
def spotifychecker():
  return render_template('spotifychecker.html')
'''
if __name__ == '__main__':
        app.run(debug=True)
