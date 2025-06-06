import numpy as np

def get_prediction(model, age, sex, bmi, glucose, smoke, drink):
    user_input = np.array([[age, sex, bmi, glucose, smoke, drink]])
    result = model.predict(user_input)[0]
    proba = model.predict_proba(user_input)[0][1]
    return result, proba
