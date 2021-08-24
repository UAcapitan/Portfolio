from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from password import password_admin
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tech = db.Column(db.String(300), nullable=False)
    img = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return self.id

@app.route('/')
def main():
    articles = Article.query.order_by(desc(Article.id)).all()
    return render_template('main.html', articles=articles)

@app.route('/article/<int:id>')
def page(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

@app.route('/add-article', methods=['POST', 'GET'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        tech = request.form['tech']
        img = request.form['img']
        text = request.form['text']
        link = request.form['link']
        password = request.form['password']

        if password == password_admin:
            article = Article(title=title, tech=tech, img=img, text=text, link=link)
            try:
                db.session.add(article)
                db.session.commit()
                return redirect('/')
            except:
                return 'Error'
        else:
            return 'Incorrect password'
    return render_template('add_article.html')

if __name__ == '__main__':
    app.run(debug='True')