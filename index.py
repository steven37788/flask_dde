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

class DayData(db.Model):
    __tablename__ = 't_daydata'
    # id = db.Column(db.Integer, primary_key=True)
    openingprice = db.Column(db.Float)
    closingprice = db.Column(db.Float)
    highestprice = db.Column(db.Float)
    floorPrice = db.Column(db.Float)
    increase = db.Column(db.Float)
    volume = db.Column(db.Float)
    takeRate = db.Column(db.Float)
    bbd = db.Column(db.Float)
    ddx = db.Column(db.Float)
    ddy = db.Column(db.Float)
    listRate = db.Column(db.Float)
    sListDiff = db.Column(db.Float)
    sInflow = db.Column(db.Float)
    mListDiff = db.Column(db.Float)
    mInflow = db.Column(db.Float)
    xListDiff = db.Column(db.Float)
    xInflow = db.Column(db.Float)
    xxListDiff = db.Column(db.Float)
    xxInflow = db.Column(db.Float)
    stockcode = db.Column(db.String(16), unique=True, primary_key=True)
    updatedate = db.Column(db.DateTime, primary_key=True)

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
    list_dde = Dde.query.all()
    return render_template('index.html', list_dde=list_dde)

@app.route('/daydata')
def daydata():
    list_daydata = DayData.query.all()
    print len(list_daydata);
    return render_template('daydata.html', list_daydata=list_daydata)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
