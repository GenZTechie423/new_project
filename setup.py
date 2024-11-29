# setup.py is responsible for creating a machine learning application as a package
# and can be deployed in PyPI
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirments(filepath: str) -> list[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="new_project",
    version="1.0",
    author="Sudd",
    author_email="sudhrshnnaresh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
