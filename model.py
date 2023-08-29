
import xgboost as xgb

BST = xgb.Booster()
BST.load_model("model/model.json")

def predict(X):
    X_ = xgb.DMatrix(X)
    y = BST.predict(X_)
    return y