from flask import Flask
from views import views



app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")



# initializing Navigations
# nav.Bar('top', [
#     nav.Item('Home', 'index'),
#     nav.Item('Gfg', 'gfg', {'page': 5}),
# ])

if __name__ == '__main__':
        app.run(debug=True)
