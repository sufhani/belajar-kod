import sqlite3

from datetime import datetime
from flask import Flask, g, render_template, url_for, redirect
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
    return db;

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
    cur = db.execute(statement, args)
    try:
        db.commit()
        print('Successul!')
    except:
        db.rollback()
        print('Failed!')
    finally:
        db.close()

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
    guides = query_db('SELECT * FROM guides LIMIT 5')
    #guides = session.query(Guide).all()
    return render_template('main.html', guides=guides)

@app.route('/panduan')
@app.route('/panduan/semua')
def all_guides():
    guides = query_db('SELECT * FROM guides LIMIT 5')
    #guides = session.query(Guide).all()
    return render_template('allguides.html', guides=guides)

@app.route('/panduan/baru', methods=['GET', 'POST'])
def new_guide():
    form = newGuideForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        timestamp = datetime.utcnow()
        insert_db("INSERT INTO guides (title, body, timestamp) "
            "VALUES (?, ?, ?)", (title, body, timestamp))

        return redirect(url_for('index'))
    return render_template('newguide.html', form=form)


@app.route('/panduan/<int:guide_id>')
def show_guide(guide_id):
    id = (guide_id,)
    guide = query_db('SELECT * FROM guides WHERE id=?', id,one=True)
    if guide == None:
        return redirect(urlf_for('index'))
    return render_template('guide.html', guide=guide)
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'dev'
    app.run(host='0.0.0.0', port=5000)