import sqlite3

from datetime import datetime
from flask import Flask, g, render_template, url_for
from flask.ext.markdown import Markdown
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from forms import newGuideForm
app = Flask(__name__)

Markdown(app)
DATABASE = './belajarkod.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    db = get_db()
    print(db)
    cur = db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(statement, args=()):
    db = get_db()
    try:
        cur = get_db().execute(statement, args)
        cur.commit()
        print('Successul!')
    except:
        cur.rollback()
        print('Failed!')
    finally:
        cur.close()

# db connect
'''
engine = create_engine('sqlite:///belajarkod.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
'''
# routing


@app.route('/')
@app.route('/index')
def index():
    cur = get_db.cursor()
    cur.execute
    guides = query_db('SELECT * FROM guides LIMIT 5')
    #guides = session.query(Guide).all()
    return render_template('main.html', guides=guides)

@app.route('/panduan')
@app.route('/panduan/semua')
def all_guides():
    guides = query_db('SELECT * FROM guides LIMIT 5')
    #guides = session.query(Guide).all()
    return render_template('guide.html', guides=guides)

@app.route('/panduan/baru', methods=['GET', 'POST'])
def new_guide():
    form = newGuideForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body
        timestamp = datetime.utcnow()
        insert_db("INSERT INTO guides (title, body, timestamp) "
            "VALUES (?, ?, ?)", (title, body, timestamp))
        return redirect(url_for('index'))
    return render_template('newguide.html', form=form)
if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'dev'
    app.run(host='0.0.0.0', port=5000)