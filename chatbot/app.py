from datetime import datetime
import os,time,json
from flask import Flask, request,jsonify
from flask import render_template
from flask_cors import CORS
from readvec import *
from qsresouce import *

queList=[]
ansList=[]
qsresouce.readQSresouce('wordresource.txt',queList,ansList)
#加载所有问答列表
vectors = {}
read_vectors('C:\\Users\\datab\\Downloads\\embedding', 635973,vectors)
#加载全部词向量



app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/check",methods=['post'])
def check():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('qsSystem.html')
    return "账号密码错误"


@app.route("/question",methods=['post'])
def add():
    ques=request.form['question']
    ans=request.form['answer']
    queList.append(ques)
    ansList.append(ans)
    file1=open("wordresource.txt","a")
    file1.write('\n')
    file1.write(ques)
    file1.write('\n')
    file1.write(ans)
    file1.close()
    return queList[0]
    

@app.route("/hello")
def hello():
    return "hello"


@app.route("/chatbot")
def chat():
    content = request.args.get('content')
    answer=similarityCheck(content,vectors,queList,ansList)
    print(content)
    print(answer)
    return  json.dumps({'as':answer}) 


if __name__ == '__main__':
    app.run(debug=True)






# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 80))
#     app.run(host='0.0.0.0', port=port, debug=True)#coding:utf8

