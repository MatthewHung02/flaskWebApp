from flask import Flask, render_template
from views import views



app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')



# initializing Navigations
# nav.Bar('top', [
#     nav.Item('Home', 'index'),
#     nav.Item('Gfg', 'gfg', {'page': 5}),
# ])

if __name__ == '__main__':
        app.run(debug=True)
