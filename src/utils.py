import os
import sys

import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):

    try:
        results = []

        for i in range(len(list(models))):

            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            parameters = param.get(model_name, {})

            gs = GridSearchCV(model, parameters, cv=3)
            gs.fit(X_train, y_train)

            best_params = gs.best_params_
            model.set_params(**best_params)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            result = {
                'Model': model_name,
                'Best Parameters': best_params,
                'Train R2 Score': train_model_score,
                'Test R2 Score': test_model_score,
                'Model_Instance': model
            }

            results.append(result)

        report_df = pd.DataFrame(results)

        return report_df

    except Exception as e:

        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)