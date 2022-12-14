from flask import Flask,request, url_for, redirect, render_template
import numpy as np
import joblib

app = Flask(__name__,static_url_path='/static')

#model=joblib.load('forestfiremodel_1.pkl')
model=joblib.load('C:/Users/91918/Documents/Forest_fire_prediction/Forest_fire_prediction/forestfiremodel_1.pkl')

@app.route('/')
def dash():
    return render_template("dash.html")
@app.route('/predict')
def dash_1  ():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.7):
        return render_template('index.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))
    else:
        return render_template('index.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
