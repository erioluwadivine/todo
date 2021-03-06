import os
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from flask_cors import CORS, cross_origin
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL = 'mysql+pymysql://erioluwa:erioluwa@127.0.0.1/erioluwa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class tableTodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(32))

db.create_all()

@app.route("/" , methods= ['GET'])
def index():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def add():
    todo = request.json.get("todo")
    newTodo = tableTodo(todo=todo)
    db.session.add(newTodo) 
    db.session.commit()
    return jsonify({
        "message" : "todo submit successful"
    })


@app.route("/delete", methods=["POST"])
def delete():
    todoId = request.json.get("todoId")
    tableTodo.query.filter_by(id=todoId).delete()
    db.session.commit()
    return jsonify({
        "message" : "todo deleted successful"
    })
    
    
if __name__ == "__main__":
    app.run(debug=True)