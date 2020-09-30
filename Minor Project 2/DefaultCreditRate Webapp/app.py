from flask import Flask,render_template,request
import util

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET','POST'])
def predict():
    global message
    if request.method=="POST":
        a  = request.form['PAY_1']
        b = request.form['LIMIT_BAL']
        c = request.form['PAY_AMT1']
        d = request.form['PAY_AMT2']
        e = request.form['PAY_AMT3']

        message = util.predict(a,b,c,d,e)

    return render_template("predict.html",message=message)

if __name__=="__main__":
    print("Starting Python Flask server for detecting Parkinson's Diseases ...")
    util.load_saved_artifacts()
    app.run(debug=True)