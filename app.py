from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tech = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return self.id

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