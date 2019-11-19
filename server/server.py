from flask import Flask
from models.classifier import Classifier

app = Flask(__name__)

@app.route('/classify', methods=['GET'])
def classify_input(data):
    classifier = Classifier(data)
    accuracy, prediction = classifier.classifier_classify()
    print(prediction,accuracy, sep="\n")    

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)