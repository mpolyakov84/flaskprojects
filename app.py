from myproject import app
from flask import render_template


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
#test commit from pycharm

if __name__ == '__main__':
    app.run(debug=True)
