from flask import Flask, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200),  nullable=False)
    def __repr__(self):
        return "<User %r>" % self.name

@app.route("/")
def Home():
    return render_template ("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user= User(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return "user registered successfully"
        #def __rep__(self):
         #   return '<user %r>' % self.email 
    return render_template ('register.html')

if __name__=="__main__":
    
    app.run(debug=True)