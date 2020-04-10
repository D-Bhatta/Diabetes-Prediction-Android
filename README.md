# Diabetes-Prediction-Android

An android app with a python backend to do diabetes prediction

## Idea

The android app uses a python backend to do the prediction based on an aggregation of models. The results and data are written to a database.
The app connects to a server through a URL.
A base request handler handles the request here, through a socket. Then, it calls a Classification function.
The results of the classification function are sent to the android app via callback function. Then, the results are written to the database with a user identifier.

## Classification function

The function returns the aggregate result of several models, whose results are summarized as text and returned.

## Callback function

The callback function returns to the app first a response of 200. If there is no result then a 400 is returned. This is followed by a string containing the results.

### 400

The app displays an error and handles appropriately.

### 200

The app receives the result and displays it.

## The app

There is a splash screen at first. Then the app has a login/registration id page, along with server address. This is used to login.
The app then stores the data from the user. It sends the data to the server. It displays a result.

### Improvements

use flask instead of the base request handler: Search for 'simple flask app' in google.  
Attach a weight tracker to the app.  
Display list of improvements in health the user can make.  

## List of To-dos

- ### Train the models and save them

  1. [x] Train the models and save them as files.
  2. [x] Load and test them for predictions.
  3. [x] Create a class that classifies input data.
  4. [x] Summarize the aggregate result of several models as text in the class and analyse accuracy.
  5. [x] Return the accuracy and the predictions.
  6. [ ] Test it with stubs.

- ### Create the app with stubs
  
  1. [ ] Create a nav drawer page as the main page.
  2. [ ] Create the splash screen and test it with stubs.
  3. [ ] Create a login and registration page and test it with stubs.
  4. [ ] Create a form page for user data input
  5. [ ] Create a result page and test it with stubs.

- ### Create the webs server with stubs

  1. [x] Create a flask app. If that doesn't work, create a simple HTTP base handler server.
  2. [x] Set it to handle some requests.
  3. [x] Test the requests with stubs.
  4. [x] Set it to return responses.
  5. [x] Test the responses with stubs.
  6. [x] Create the Classification function.
  7. [x] Attach it to the Classification function.
  8. [x] Test requests and responses with stubs.

- ### Attach the server to the app
  
  1. [ ] Attach the server to the app.
  2. [ ] Test for sample input data.
  3. [ ] Remove bugs.
  4. [ ] Publish as Alpha version.

- ### Test the app
  
  1. [ ] Test it for a wide range of input data.
  2. [ ] Find its limitations.
  3. [ ] Document it's expected input and output.

- ### Create the documentation

  1. [ ] Create the project report.
     1. [ ] Use README.md as a reference to create the report introduction and methodology.
     2. [ ] Display statistics and figures about the data.
     3. [ ] Show mockup figures.
     4. [ ] Display expected results for sample inputs.
     5. [ ] Talk about future imporvements.
     6. [ ] Conclusion
  2. [ ] Create the project PowerPoint.
     1. [ ] Turn the report into a PPT.
     2. [ ] Divide roles of speaking.
  3. [ ] Create a paper on the software.
