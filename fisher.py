from flask import Flask

from helper import is_isbn_or_key

app = Flask(__name__)

app.config.from_object('config')

@app.route('/book/sreach/<q>/<page>')
def sreach(q, page):
    """
        q: 普通关键字 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)

if __name__ == '__main__':
    app.run(
        host = app.config['HOST'],
        port = app.config['PORT'],
        debug = app.config['DEBUG'],
    )
