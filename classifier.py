class Classifier(object):
    '''Classifies the given input data into binary Yes/No outcome of having diabetes, and analyses accuracy of the result.
    Returns predictions and accuracy.'''
    # define init function
    # add input variables into help string of class.
    def __init__(self,data):
        self.data = []
        self.data = data
        self.predictions = []
        self.prediction = ""
        self.accuracy = ""
        self.positive_probability = 0.00
        self.negative_probability = 0.00
    def model_predictions(self):
        '''Imports models, stores model predictions'''
        # load a model
        # predict a data
        # store the predictions
        pass
    def analyse_accuracy(self):
        '''Analyse accuracy of model predictions'''
        # calculate total accuracy of positive result
        # calculate total accuracy of negative result
        # divide total accuracy of positive result by total accuracy and store in self.positive_probability as percentage
        # divide total accuracy of negative result by total accuracy and store in self.negative_probability as percentage
        pass
    def predict_diabetes(self):
        '''Predicts whether there is diabetes or not'''
        # check whether positive probability or negative probability is higher
        # predict whether there is diabetes or not
        # construct prediction string
        # construct accuracy string
        pass
