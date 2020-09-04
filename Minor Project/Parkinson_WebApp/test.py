import util
import numpy as np
from util import predict,load_saved_artifacts
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()

if __name__=="__main__":
    load_saved_artifacts()
    print("Enter inputs")
    a = float(input("Enter"))
    b = float(input("Enter"))
    c = float(input("Enter"))
    d = float(input("Enter"))
    e = float(input("Enter"))
    message = util.predict(a,b,c,d,e)
    print(message)



