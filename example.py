from flask import Flask, request,render_template 

## other pip installs 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address 

app = Flask(__name__)

## limiter code ... 
## https://flask-limiter.readthedocs.io/en/stable/
limiter = Limiter (
    app,
    key_func = get_remote_address, 
    default_limits= ["10 per second"]
)


## example for templates
@app.route('/')
def home():
    return render_template('example.html')

## example for handling http requests 
@app.route('/api/requestExample',methods = ['POST', 'GET'])
def request_examples():
   if request.method == 'POST':
      content = request.get_json(silent=True)
      print(content)
      message = {
          'method': 'POST',
          'message': 'post request was a success!',
          'content': content 
      }
      return message 
   if request.method =='GET':
      return  'this is get from /api/requestExample'

## example for querystring
@app.route('/data', methods=['GET'])
def data():
    return request.query_string

##url named parameters
@app.route('/data1', methods=['GEt'])
def data1(): 
    test1 = request.args.get('test1')
    test2 = request.args.get('test2')
    message = {
        'from_test1': test1, 
        'from_test2': test2
    }
    return message 
if __name__=='__main__':
    app.run(debug=True)