# ffs: flask from scratch
from flask import Flask, render_template
ffsapp = Flask(__name__)


@ffsapp.route('/')
def index():
    # return 'Hallo Welt noch einmal!!!!'
    return render_template('home.html')


# debug=True so that doesnt have to reinit server each time
if __name__ == '__main__':
    ffsapp.run(debug=True)
