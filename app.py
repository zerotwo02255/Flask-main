from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)

with app.app_context():
    db.create_all()

class jeff(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)


def __repr__(self)-> str:
    return f"{self.sno}-{self.title}"
@app.route('/')
def hello_world():
    return render_template('ankit.html')
   # return 'hello world!'


@app.route('/there')
def there():
    return 'hello there'

if __name__ == "__main__":
    app.run(debug=True,port =9000)