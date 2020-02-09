from flask import Flask,jsonify
from users import users

app=Flask(__name__)

@app.route('/',methods=['GET'])

def ping():
    return jsonify({"response":"hello wrold"})

@app.route('/users',methods=['GET'])

def usershandler():
    return jsonify({"response":users})

if __name__=='__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)