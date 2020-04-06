class Classifier(object):
    '''Classifies the given input data into binary Yes/No outcome of having diabetes, and analyses accuracy of the result.
    Returns predictions and accuracy.'''
    # define init function
    # add input variables into help string of class.
    def __init__(self,data):
        self.predictions = []
        self.prediction = ""
        self.accuracy = ""
        self.positive_probability = 0.00
        self.negative_probability = 0.00
        from numpy import array
        self.data = array(list(data))
        self.data = self.data.reshape(1,-1)
        self.models = [('decision_tree_model.sav',74.0), ('deep_learning_model.sav',80.2), ('gradient_boost_model.sav',79.2), ('knn_model.sav',78.0), ('svc_model.sav',79.7), ('random_forest_model.sav',78.6), ('logistic_reg_model.sav',76.6)]
    def model_predictions(self):
        '''Imports models, stores model predictions'''
        #joblib is used to serialize loading and storing models
        from joblib import load
        from joblib import dump
        # load a model
        for i in range(len(self.models)):
            filename = self.models[i][0]
            # predict a data
            loaded_model = load(filename)
            model_prediction = loaded_model.predict(self.data) 
            model_prediction = list(model_prediction)[0]
            # store the predictions
            self.predictions.append([model_prediction,self.models[i][1]])
    def analyse_accuracy(self):
        '''Analyse accuracy of model predictions'''
        self.positive_probability = 0.00
        self.negative_probability = 0.00
        positive_probability = 0.00
        negative_probability = 0.00
        total_probability = 0.00
        for i in range(len(self.predictions)):
            # calculate total accuracy of positive result
            if self.predictions[i][0] == 1:
                positive_probability += self.predictions[i][1]
            # calculate total accuracy of negative result
            else:
                negative_probability += self.predictions[i][1]
            total_probability += self.predictions[i][1]
        # divide total accuracy of positive result by total accuracy and store in self.positive_probability as percentage
        self.positive_probability = (positive_probability/total_probability)*100
        # divide total accuracy of negative result by total accuracy and store in self.negative_probability as percentage
        self.negative_probability = (negative_probability/total_probability)*100
    def predict_diabetes(self):
        '''Predicts whether there is diabetes or not'''
        # check whether positive probability or negative probability is higher
        if self.positive_probability > self.negative_probability:
            # predict whether there is diabetes or not
            # construct prediction string
            self.prediction = "Diabetes detectecion is positive"
            # construct accuracy string
            self.accuracy = "Accuracy of prediction is " + str(self.positive_probability)
        elif self.positive_probability < self.negative_probability:
            # construct prediction string
            self.prediction = "Diabetes detectecion is negative"
            # construct accuracy string
            self.accuracy = "Accuracy of prediction is " + str(self.negative_probability)
        else:
            self.prediction = "Diabetes detectecion is inconclusive"
            # construct accuracy string
            self.accuracy = "Accuracy of prediction is " + str(self.positive_probability)
    def classifier_classify(self):
        '''driver function to classify the data. it calls the methods defined in the class above it and returns 2 values: prediction and accuracy'''
        self.model_predictions()
        self.analyse_accuracy()
        self.predict_diabetes()
        accuracy, prediction = self.accuracy, self.prediction
        return accuracy, prediction
    def classifier_predict(self):
        """ Dummy test function """
        self.prediction = "Diabetes detectecion is positive"
        self.accuracy = "Accuracy of prediction is 80%"
        accuracy, prediction = self.accuracy, self.prediction
        return accuracy, prediction