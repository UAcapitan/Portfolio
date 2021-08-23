from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/article/<int:id>')
def page(id):
    return render_template('article.html')

@app.route('/add-article')
def add_article():
    return render_template('add_article.html')

if __name__ == '__main__':
    app.run(debug='True')