from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL = 'mysql+pymysql://erioluwa:erioluwa@127.0.0.1/erioluwa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/index" , methods= ['GET'])
def index():
    return render_template("index.html")

# @app.route("/", methods=['POST'])
# def add():
    
if __name__ == "__main__":
    app.run(debug=True)