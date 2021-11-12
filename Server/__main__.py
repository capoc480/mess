import users
import chats

from flask import Flask, jsonify, request

app = Flask(__name__)

def SuccessResponse(result):
    response = {"ok":True, "result":result}

    return jsonify(response)

def ErrorResponse(description, error_code):
    response = {"ok":False, "error_code":error_code, "description":description}

    return jsonify(response), error_code

@app.route('/api/v1/sendMessage')
def send_message():
    arguments = request.args

    text = arguments.get("text")
    user_id = arguments.get("user_id")
    chat_id = arguments.get("chat_id")

    if text == None:
        return ErrorResponse("text equals nil", 400)
    elif text.__len__() == 0:
        return ErrorResponse("text length equals 0", 400)

    if user_id == None:
        return ErrorResponse("user_id equals nil", 400)
    elif not user_id.isdecimal():
        return ErrorResponse("user_id not is decimal", 400)

    if chat_id == None:
        return ErrorResponse("chat_id equals nil", 400)
    elif chat_id.isdecimal():
        return ErrorResponse("chat_id not is decimal", 400)

@app.route('/api/v1/login')
def login():
    arguments = request.args

    username = arguments.get("username")
    password = arguments.get("password")

    if username == None:
        return ErrorResponse("username equals nil", 400)
    elif username.__len__() == 0:
        return ErrorResponse("username length cannot be 0", 400)
    elif username.__len__() > 32:
        return ErrorResponse("username length must be less or equal 32", 400)

    if password == None:
        return ErrorResponse("password equals nil", 400)
    elif password.__len__() == 0:
        return ErrorResponse("password length cannot be 0", 400)
    elif password.__len__() > 32:
        return ErrorResponse("password length must be less or equal 32", 400)

    #return "success"
 
    user = users.get_user(username, password)
    if user == None:
        user = users.add_user(username, password)

    return SuccessResponse(user)
# D:\OpenSSL-Win64\bin
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    context = ("server.pem",)
    app.run(debug=True, ssl_context=context)