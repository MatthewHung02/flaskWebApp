from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates")
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app