# Fish Species Classification Web App
This repository contains code and data for a web application that can classify fish species based on their physical measurements. The web app is built using Flask and hosted on Heroku.

Introduction
With this Fish Species Classification Web App, you can now easily identify the species of a fish by inputting its physical measurements. This app uses a machine learning model trained on a dataset of fish measurements and their corresponding species labels.

How It Works
Input the Fish Measurements: Enter the weight, lengths, height, and width of the fish in the provided form on the web app.

Get the Predicted Species: Click the "Predict" button, and the app will use a Support Vector Machine (SVM) classifier to predict the species based on the provided measurements.

View the Result: The app will display the predicted species of the fish, providing you with valuable insights into the fish's identity.

Dataset
The machine learning model used in this app was trained on a carefully curated dataset containing various fish species and their corresponding physical measurements. The data was preprocessed to handle missing values, normalize the features, and remove outliers for better model performance. Dataset url: https://www.kaggle.com/datasets/aungpyaeap/fish-market

Model
The SVM classifier was chosen for its ability to handle multi-class classification tasks like fish species identification. The model's hyperparameters were tuned using GridSearchCV to find the best combination for accurate predictions.

Web App
The web application was built using Flask, a lightweight Python web framework, to create a user-friendly interface for predicting fish species. The app is hosted on Heroku, making it easily accessible from any device with an internet connection.

Usage
You can access the Fish Species Classification Web App by visiting the following link

Upon reaching the web app, you will see a form prompting you to enter the fish's weight, lengths, height, and width. Once you input the required measurements, simply click the "Predict" button, and the app will quickly analyze the data and display the predicted species
