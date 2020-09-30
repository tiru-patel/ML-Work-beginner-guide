import json
import pickle
import numpy as np

__data_columns=None
__model=None
def predict(spread1,mdvp_apq,ppe,mdvp_shimmer,mdvp_shimmerdb):
    x1 = np.zeros(len(__data_columns))
    x1[0]=spread1
    x1[1]=mdvp_apq
    x1[2]=ppe
    x1[3]=mdvp_shimmer
    x1[4]=mdvp_shimmerdb
    q=__model.predict([x1])[0]
    if q==1:
        return "Default Rate is High ..."
    else:
        return "Default Rate is Low ..."
def col():
    return __data_columns
def load_saved_artifacts():
    print("Loading saved artifacts ...")
    global __data_columns
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)['data_columns']
    with open("./artifacts/default.pickle","rb") as f:
        __model=pickle.load(f)
    print("Artifacts loading completed ...")
if __name__=="__main__":
    load_saved_artifacts()
    print(col())
    print(predict(-1,240000,17409,47622,12279))