from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, instance_relative_config=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Jeff(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    obj = Jeff(title="first to do", desc="indosss")
    db.session.add(obj)
    db.session.commit()
    alljeff = Jeff.query.all()
    return render_template("ankit.html", alljeff=alljeff)


@app.route("/there")
def there():
    alljeff = Jeff.query.all()
    print(alljeff)
    return "hello there"


if __name__ == "__main__":
    app.run(debug=True, port=9000)