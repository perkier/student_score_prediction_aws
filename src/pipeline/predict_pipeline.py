import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os
import dill


class PredictPipeline:

    def __init__(self):
        pass

    def predict(self, features):

        try:

            # Get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))

            model_path_relative = os.path.join('..','..', 'components', 'artifacts', 'model.pkl')
            preprocessor_path_relative = os.path.join('..','..',  'components', 'artifacts', 'proprocessor.pkl')

            # Get the absolute path using the relative path
            model_path = os.path.abspath(os.path.join(script_dir, model_path_relative))
            preprocessor_path = os.path.abspath(os.path.join(script_dir, preprocessor_path_relative))

            print("Before Loading")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            print("After Loading")

            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:

    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):

        try:

            custom_data_input_dict = {"gender": [self.gender],
                                      "race_ethnicity": [self.race_ethnicity],
                                      "parental_level_of_education": [self.parental_level_of_education],
                                      "lunch": [self.lunch],
                                      "test_preparation_course": [self.test_preparation_course],
                                      "reading_score": [self.reading_score],
                                      "writing_score": [self.writing_score]}

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:

            raise CustomException(e, sys)