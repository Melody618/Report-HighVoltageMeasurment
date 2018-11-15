from flask import Flask,request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#对带有/test的url进行响应
@app.route('/test',methods=['GET','POST'])
def test():
	#请求为GET方式，从url中的args提取数据，关键字为"data"
    if request.method  == 'GET':
        msg = request.args.get('data')
    #请求为POST方式，从请求体中获取参数，关键字为"data"
    else:
        msg = request.form.get('data')
    #将请求中附带的数据返回作为相应
    return msg

if __name__ == '__main__':
    manager.run()

