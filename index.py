from flask import Flask
from views import views

def create_app():
    app = Flask(__name__, template_folder="website/templates")
    return app

app = create_app()

app.register_blueprint(views, url_prefix='/')




if __name__ == '__main__':
        app.run(debug=True)
