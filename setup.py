from setuptools import find_packages, setup
from typing import List

def get_requirements(path:str)->List[str]:
    """
    This funciton will return a list of requirements
    """

    packages = []

    with open(path) as file_obj:
        packages = file_obj.readlines()
        packages = [req.replace("\n", "") for req in packages]

        if "-e ." in packages:
            packages.remove("-e .")

    return packages

setup(name = "student_score_prediction",
      version = "0.0.1",
      author = "Diogo",
      author_email = "diogoncsa@gmail.com",
      packages = find_packages(),
      install_requires = get_requirements("requirements.txt"))

