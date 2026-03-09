from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class jeff(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self) -> str:
        return f"{self.sno}  -   {self.title}"
    
    


@app.route('/')
def hello_world():
    obj =jeff(title="first to do",desc="indosss")
    db.session.add(obj)
    db.session.commit()
    alljeff=jeff.query.all()
    return render_template('ankit.html',alljeff=alljeff)
   # return 'hello world!'


@app.route('/there')
def there():
    alljeff=jeff.query.all()
    print(alljeff)
    return 'hello there'

with app.app_context():
    db.create_all()
    
    
if __name__ == "__main__":
    app.run(debug=True,port =9000)