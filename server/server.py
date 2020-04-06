from flask import Flask
from models.classifier import Classifier

app = Flask(__name__)


data = (1,85,66,29,0,26.6,0.351,31) 


@app.route('/')
def index():
    return '<h1>Hello! Welcome to Diabetes Classifier app.</h1>'

@app.route('/classify', methods=['GET'])
def classify_input():
    classifier = Classifier(data=data)
    accuracy, prediction = classifier.classifier_classify()
    return ('<h1>{}</h1><br/><h2>{}</h2>'.format(prediction,accuracy))

if __name__ == '__main__':
    app.run(threaded=True, debug=True)