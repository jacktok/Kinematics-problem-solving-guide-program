from flask import Flask, jsonify, render_template, request
import json
# from wordcut.SearchWord import Dic
# from wordcut.wordFilter import Filter 
# from wordcut.wordCut import WordCut
# from wordcut.wordMap import WordMap
# from wordcut.wordGroup import WordGroup
from controll import Controll

controll=Controll()
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
    controll.look(data)
    data = {"value": controll.lookup('word')}
    
    return jsonify(data)
@app.route('/test/', methods=['GET'])
def test():
    data =  request.args.get('problem')
    print(data)
    controll.includeProblem(data)
    answers = controll.calulate()
    # answers=json.dumps(answers, ensure_ascii=False)
    data = {"value": 'answers'}
    
    return jsonify(data)
@app.route('/recommend/',methods=['GET'])
def recommend():
    data =  request.args.get('problem')
    print(data)
    controll.includeProblem(data)
    answers = controll.returnVariable()
    # answers=json.dumps(answers, ensure_ascii=False)
    data = {"value": answers}

if __name__ == '__main__':
    app.run(port=8000, debug=True)
