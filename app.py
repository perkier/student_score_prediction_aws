import pickle
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Prediction for Student Score Prediction</h3>"

@app.route("/predict", methods=["POST"])
def predict():

    data = CustomData(gender=request.get_json()["gender"],
                      race_ethnicity=request.get_json()["race_ethnicity"],
                      parental_level_of_education=request.get_json()["parental_level_of_education"],
                      lunch=request.get_json()["lunch"],
                      test_preparation_course=request.get_json()["test_preparation_course"],
                      reading_score=int(request.get_json()["reading_score"]),
                      writing_score=int(request.get_json()["writing_score"]))

    pred_df = data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()

    prediction = predict_pipeline.predict(pred_df)

    return f"prediction: {prediction}"


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)
