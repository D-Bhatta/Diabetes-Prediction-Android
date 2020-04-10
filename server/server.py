from flask import Flask
from models.classifier import Classifier
from random import choice

app = Flask(__name__)





@app.route('/')
def index():
    return '<h1>Hello! Welcome to Diabetes Classifier app.</h1>'

@app.route('/classify', methods=['GET'])
def classify_input():
    data = choice([(1,85,66,29,0,26.6,0.351,31),(5,116,74,0,0,25.6,0.201,30),(11,138,76,0,0,33.2,0.42,35)])
    classifier = Classifier(data=data)
    accuracy, prediction = classifier.classifier_classify()
    del(classifier)
    return ('<h1>{}</h1><br/><h2>{}</h2>'.format(prediction,accuracy))

if __name__ == '__main__':
    app.run(threaded=True, debug=True)