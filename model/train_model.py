import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
import pickle

df = pd.read_csv("../data/dataset.csv")

X = df[["marks", "frequency"]]

clf = LogisticRegression()
clf.fit(X, df["label"])

reg = LinearRegression()
reg.fit(X, df["time_required"])

with open("models.pkl", "wb") as f:
    pickle.dump((clf, reg), f)

print(" Models trained!")