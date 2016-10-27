from flask import Flask, jsonify, render_template, request
from SearchWord import Dic
mydic=Dic()
app = Flask(__name__)
def test(word):
 	return "8"
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')+" hi"}

    return jsonify(ret_data)
@app.route('/preword/', methods=['GET'])
def preword():
    data =  request.args.get('word')
    mydic.look(data)
    data = {"value": mydic.lookup('word')}
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
