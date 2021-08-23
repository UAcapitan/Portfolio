from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Main page'

@app.route('/article/<int:id>')
def page(id):
    return 'Article ' + str(id)

@app.route('/add-article')
def add_article():
    return 'Add article'

if __name__ == '__main__':
    app.run(debug='True')