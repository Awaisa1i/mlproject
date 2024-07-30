import pandas as pd
import numpy as np
import os
import sys
from src.exception import CustomException
import dill

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as handle:
            dill.dump(obj,handle)
    except Exception as e:
        raise CustomException(e,sys)