from flask import Flask
from models.classifier import Classifier
from numpy import array

app = Flask(__name__)


data = array([[7,150,66,42,342,34.7,0.718,42]]) 


@app.route('/')
def index():
    return '<h1>Hello! Welcome to Diabetes Classifier app.</h1>'

@app.route('/classify', methods=['GET'])
def classify_input():
    classifier = Classifier(data=data)
    accuracy, prediction = classifier.classifier_predict()
    return ('<h1>{}</h1><br/><h2>{}</h2>'.format(prediction,accuracy))  

if __name__ == '__main__':
    app.run(threaded=True, debug=True)