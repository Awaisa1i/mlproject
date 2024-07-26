from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    requirement = []
    with open(file_path, 'r') as f:
        requirement = f.readlines()
        requirement = [r.replace('\n',' ') for r in requirement]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
setup(
    
    name = 'mlproject',
    version='0.0.1',
    author='Awais',
    author_email='mawaisali833@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt') 
    )

