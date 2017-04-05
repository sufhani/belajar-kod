from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Base, Guide
app = Flask(__name__)

# db connect
engine = create_engine('sqlite:///belajarkod.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# routing


@app.route('/')
@app.route('/index')
def index():
    #guides = session.query(Guide).all()
    return render_template('main.html')#,guides=guides)

@app.route('/panduan')
@app.route('/panduan/semua')
def all_guides():
    guides = session.query(Guide).all()
    return render_template('guide.html', guides=guides)

@app.route('/panduan/baru', methods=['GET', 'POST'])
def new_guide():
    if request.method == 'POST':

    render_template('newguide.html')
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)