from flask import Flask,render_template,request
import json
import pandas as pd
import pickle
import numpy as np
import joblib

with open(f'model/model.pickle', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET','POST'])
def predict():
    global pred
    if request.method=="POST":

        a  = request.form['PAY_1']
        b = request.form['LIMIT_BAL']
        c = request.form['PAY_AMT1']
        d = request.form['PAY_AMT2']
        e = request.form['PAY_AMT3']
        input_variables = pd.DataFrame([[a,b,c,d,e]],
                                       columns=['pay_1', 'limit_bal', 'pay_amt1','pay_amt2','pay_amt3'],
                                       dtype=float)

        q = model.predict(input_variables)[0]
        if q == 1:
            pred= "Default rate is High ..."
        else:
            pred= "Default rate is Low ... !"
    return render_template("predict.html",message=pred)

if __name__=="__main__":
    app.run(debug=True)