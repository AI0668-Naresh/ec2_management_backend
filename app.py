from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Initialize Flask app and MongoDB 
app = Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)
jwt = JWTManager(app)
CORS(app)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username', '')
    password = data.get('password', '')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    # Check if the user already exists in the MongoDB collection
    user = mongo.db.users.find_one({'username': username})
    if user:
        return jsonify({"msg": "User already exists"}), 400

    # Hash the password and save user to the database
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({
        'username': username,
        'password': hashed_password
    })

    return jsonify({"msg": "User created successfully"}), 201

# Login route to authenticate and issue JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    username = data.get('username', '')
    password = data.get('password', '')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    # Find the user in MongoDB
    user = mongo.db.users.find_one({'username': username})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Invalid username or password"}), 401

    # Create JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Protected route that requires JWT token for access
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True,port=5000)
