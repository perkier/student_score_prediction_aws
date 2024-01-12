import requests
import json

import pandas as pd
import numpy as np
import matplotlib
import sklearn
import catboost
import xgboost
import dill
import flask

print("pandas==", pd.__version__)
print("numpy==", np.__version__)
print("matplotlib==", matplotlib.__version__)
print("scikit-learn==", sklearn.__version__)
print("catboost==", catboost.__version__)
print("xgboost==", xgboost.__version__)
print("dill==", dill.__version__)
print("Flask==", flask.__version__)
print("requests==", requests.__version__)

quit()

def predict(data):

    # Make a POST request to the API endpoint
    try:
        response = requests.post(url, json=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:

            try:
                # Try to parse the response as JSON
                predictions = float(response.text.split(":")[1].strip().strip("[]"))
                print("Model Predictions:", predictions)

            except json.JSONDecodeError:

                print("Error: Unable to decode JSON response")
                print("Response Content:", response.text)

        else:
            print("Fatal Error:", response.status_code, response.text)

    except requests.exceptions.RequestException as e:
        print("Exception Error:", e)

url = "http://3.8.186.173:5000/predict"

data_1 = {"gender": "female",
          "race_ethnicity": 'group A',
          "parental_level_of_education": "bachelor's degree",
          "lunch": 'standard',
          "test_preparation_course": 'completed',
          "reading_score": 55,
          "writing_score": 79}

data_2 = {"gender": "male",
          "race_ethnicity": 'group E',
          "parental_level_of_education": "master's degree",
          "lunch": 'free/reduced',
          "test_preparation_course": 'completed',
          "reading_score": 15,
          "writing_score": 22}

data_3 = {"gender": "male",
          "race_ethnicity": 'group A',
          "parental_level_of_education": "bachelor's degree",
          "lunch": 'free/reduced',
          "test_preparation_course": 'completed',
          "reading_score": 95,
          "writing_score": 92}


predict(data_1)
# predict(data_2)
# predict(data_3)

quit()
