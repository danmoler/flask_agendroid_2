# ffs: flask from scratch
from flask import Flask, render_template
from data import Articles

ffsapp = Flask(__name__)

Articles = Articles()


@ffsapp.route('/')
def index():
    # return 'Hallo Welt noch einmal!!!!'
    return render_template('home.html')


@ffsapp.route('/about')
def about():
    return render_template('about.html')


@ffsapp.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@ffsapp.route('/article/<string:id>/')
def article(id):
    # return render_template('articles.html', articles=Articles)
    # while we don't have sql ready, pass hardcoded id
    return render_template('article.html', id=id)


# debug=True so that doesnt have to reinit server each time
if __name__ == '__main__':
    ffsapp.run(debug=True)
