import pandas as pd
import numpy as np
import random
from pathlib import Path
#equipping the prompt with user age, region ,bodytype and gender
parent_dir = Path(__file__).parent.parent
data_dir = parent_dir.joinpath("User data")
user_profile = pd.read_csv(data_dir.joinpath('user_profile.csv'))


def userData(user_id):
    user_data = user_profile.query(f"UserID == {user_id}").iloc[0]
    user_gender = user_data['Gender']
    user_age = user_data['Age']
    user_region = user_data['Region']
    user_body_type = user_data['BodyType']
    msg = f"The gender is {user_gender}, age is {user_age} and body type is {user_body_type}. I live in {user_region}"
    return msg
    
