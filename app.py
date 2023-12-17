from flask import Flask
import bookstore

app = Flask(__name__)

store = bookstore.BookStore("db/")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
