from flask import Flask, request, jsonify
import requests
import pandas as pd
from pathlib import Path

app=Flask(__name__)
@app.route('/')  #home page
def home():
    return "User data API"

parent_dir = Path(__file__).parent.parent
data_dir = parent_dir.joinpath("User data")
user_profile = pd.read_csv(data_dir.joinpath('user_profile.csv'))

@app.route('/api/user_data/<string:user_id>',methods=['GET'])
def user(user_id):
    user_data = user_profile.query(f"UserID == {user_id}").iloc[0]
    if user_data.empty:
        return jsonify(error='User not found')
    else:
        user_gender = user_data['Gender']
        user_age = user_data['Age']
        user_region = user_data['Region']
        user_body_type = user_data['BodyType']
        msg = f"The gender is {user_gender}, age is {user_age} and body type is {user_body_type} and lives in {user_region}"
        return jsonify(msg)

    

if __name__=='__main__':
    app.run(debug=False,port = 1236)