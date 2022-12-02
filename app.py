from flask import Flask
from views import views


app = Flask(__name__)
nav = Navigation(app)

app.register_blueprint(views, url_prefix="/")



if __name__ == '__main__':
        app.run(debug=True)
