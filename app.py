#coding:utf8
from datetime import datetime
import os,time,json
from flask import Flask, request,jsonify
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route("/test")
def hello():
    return "你好"


@app.route("/chatbot")
def chat():
    content = request.args.get('content')
    
    if  u'新建仓库' in content :
        answer = u'在地图要建立仓库的地方单击，在弹出窗口中选择新建仓库。'
    if  u'提升品牌关注度' in content :
        answer = u'我建议你通过参考市场调研报告，在流量比较大的平台加大广告的投入'

    print(content)
    print(answer)
    return  json.dumps({'as':answer}) 


# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=True)

