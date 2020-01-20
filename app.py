from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

from flask_cors import CORS

CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL = 'mysql+pymysql://erioluwa:erioluwa@127.0.0.1/erioluwa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(32))

db.create_all()

@app.route("/index" , methods= ['GET'])
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def add():
    todo = request.json.get("todo")
    newTodo = todo(todo=todo)
    db.session.add(newTodo) 
    db.session.commit()
    
if __name__ == "__main__":
    app.run(debug=True)