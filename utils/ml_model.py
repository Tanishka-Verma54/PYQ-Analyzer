import pickle

# load trained models
with open("model/models.pkl", "rb") as f:
    clf, reg = pickle.load(f)

def predict(marks, frequency):
    # ML for importance
    label = clf.predict([[marks, frequency]])[0]

    # NEW CONTROLLED TIME LOGIC
    time = (marks * 1.5) + (frequency * 2)

    # cap max time to 20 mins
    if time > 20:
        time = 20

    return label, int(time)