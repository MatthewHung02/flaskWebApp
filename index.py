from flask import Flask, render_template
from views import views
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def base():
  return render_template('index.html')

@app.route('/aboutme')
def aboutme():
  return render_template('aboutme.html')





# initializing Navigations
# nav.Bar('top', [
#     nav.Item('Home', 'index'),
#     nav.Item('Gfg', 'gfg', {'page': 5}),
# ])

if __name__ == '__main__':
        app.run(debug=True)
