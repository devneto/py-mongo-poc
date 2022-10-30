from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pymongopoc'
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    return {"message":"ok"}

if __name__ == "__main__":
    app.run(debug=True)