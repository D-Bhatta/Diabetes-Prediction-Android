# Diabetes-Prediction-Android
An android app with a python backend to do diabetes prediction


# Idea
The android app uses a python backend to do the prediction based on an aggregation of models. The results and data are written to a database.
The app connects to a server through a URL.
A base request handler handles the request here, through a socket. Then, it calls a Classification function. 
The results of the classification function are sent to the android app via callback function. Then, the results are written to the database with a user identifier.

# Classification function
The function returns the aggregate result of several models, whose results are summarized as text and returned.

# Callback function
The callback function returns to the app first a response of 200. If there is no result then a 400 is returned. This is followed by a string containing the results.
## 400
The app displays an error and handles appropriately.
## 200
The app receives the result and displays it.

# The app
There is a splash screen at first. Then the app has a login/registration id page, along with server address. This is used to login.
The app then stores the data from the user. It sends the data to the server. It displays a result.

## Improvements
use flask instead of the base request handler: Search for 'simple flask app' in google.
Attach a weight tracker to the app.
Display list of improvements in health the user can make.