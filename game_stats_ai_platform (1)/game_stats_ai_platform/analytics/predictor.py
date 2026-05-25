
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_score(scores):
    X = np.array(range(1, len(scores)+1)).reshape(-1, 1)
    y = np.array(scores)

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[len(scores)+1]])
    prediction = model.predict(future)

    return round(float(prediction[0]), 2)
