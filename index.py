from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Derman@localhost/nodejs'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

db = SQLAlchemy(app)
db.create_all()

class Dde(db.Model):
    __tablename__ = 't_dde'
    id = db.Column(db.Integer, primary_key=True)
    stockcode = db.Column(db.String(16), unique=True)
    price = db.Column(db.Float)
    margin = db.Column(db.Float)
    turnover = db.Column(db.Float)
    ratio = db.Column(db.Float)
    BBD = db.Column(db.Float)
    volume = db.Column(db.Integer)
    sweepdeck = db.Column(db.Float)
    DDX = db.Column(db.Float)
    DDY = db.Column(db.Float)
    DDZ = db.Column(db.Float)
    tenDDX = db.Column(db.Float)
    tenDDY = db.Column(db.Float)
    continues = db.Column(db.Float)
    largediff = db.Column(db.Float)
    bigdiff = db.Column(db.Float)
    middlediff = db.Column(db.Float)
    smalldiff = db.Column(db.Float)
    sheetrate = db.Column(db.Float)
    updatetime = db.Column(db.DateTime)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<User %r>' % self.username


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    # dde = Dde()
    # list = dde.query.all()
    list1 = Dde.query.all()
    # list = dde.get_tables_for_bind()
    return render_template('index.html', list1=list1)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()