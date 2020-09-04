from flask import Flask,render_template,request
import util
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()
app = Flask(__name__)
@app.route("/")
@app.route("/home",methods=['GET','POST'])
def home():
    if request.method=="POST":
        a  = request.form['spread']
        b = request.form['mdvp_apq']
        c = request.form['ppe']
        d = request.form['mdvp_shimmer']
        e = request.form['mdvp_shimmerdb']

        message = util.predict(a,b,c,d,e)

        return render_template("predict.html",message=message)
    return render_template("index.html")

if __name__=="__main__":
    print("Starting Python Flask server for detecting Parkinson's Diseases ...")
    util.load_saved_artifacts()
    app.run(debug=True)