from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from website import create_app

app = create_app()
Bootstrap(app)

# @app.route('/')
# def base():
#   return render_template('index.html')

# @app.route('/aboutme')
# def aboutme():
#   return render_template('aboutme.html')

if __name__ == '__main__':
        app.run(debug=True)
print("testing github on new laptop")