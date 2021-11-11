# -*- coding: utf-8 -*-  
""" 
* file description 
    - Copyright ⓒ 2021 KCNET, All rights reserved.
    - fileName : ``app.py``
    - author : ``이서용 (Lee Seo Yong)``
    - date : ``2021-11-11 오후 11:52``
    - comment : `` ``
       
* revision history 
    - 2021-11-11    Lee Seo Yong    최초 작성
"""


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello world!</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)