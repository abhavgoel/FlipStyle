from flask import Flask, request, jsonify
import requests
import pandas as pd
from pathlib import Path

app=Flask(__name__)


parent_dir = Path(__file__).parent.parent
data_dir = parent_dir.joinpath("User data")
browsing_history = pd.read_csv(data_dir.joinpath('browsing_history.csv'))

@app.route('/')  #home page
def home():
    return "Bowsing history API"

@app.route('/api/browsing_data/<string:user_id>',methods=['GET'])
def browser(user_id):
    user_data = browsing_history.query(f"UserID == {user_id}")
    
    if user_data.empty:
        return jsonify(error='User not found')
    
    prev_history = user_data['ProductDescription'].tolist()
    return jsonify(prev_history)
    

if __name__=='__main__':
    app.run(debug=False,port = 1234)