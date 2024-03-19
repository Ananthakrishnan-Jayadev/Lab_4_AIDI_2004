from flask import Flask, render_template, request, jsonify, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('fish_classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    weight = float(request.form['Weight'])
    length1 = float(request.form['Length1'])
    length2 = float(request.form['Length2'])
    length3 = float(request.form['Length3'])
    height = float(request.form['Height'])
    width = float(request.form['Width'])

    prediction = model.predict([[weight,length1,length2,length3,height,width]])[0]

    # Redirect to the result route with prediction
    return redirect(url_for('result', prediction=prediction))

@app.route('/result/<prediction>')
def result(prediction):
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
