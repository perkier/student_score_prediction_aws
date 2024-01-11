import requests
import json

url = "http://localhost:5000/predict"

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

# Set the content type
headers = {"Content-Type": "application/json"}

# Make the request and display the response
resp = requests.post(url, json=data_1, headers=headers)
print(resp.text)
resp = requests.post(url, json=data_2, headers=headers)
print(resp.text)
resp = requests.post(url, json=data_3, headers=headers)
print(resp.text)

