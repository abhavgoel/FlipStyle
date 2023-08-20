from flask import Flask, request, jsonify
import requests
import pandas as pd
from pathlib import Path

app=Flask(__name__)
@app.route('/')  #home page
def home():
    return "Purchase history API"
parent_dir = Path(__file__).parent.parent
data_dir = parent_dir.joinpath("User data")
purchase_history = pd.read_csv(data_dir.joinpath('purchase_history.csv'))

@app.route('/api/purchase_data/<string:user_id>',methods=['GET'])
def purchase(user_id):
    user_data = purchase_history.query(f"UserID == {user_id}")
    
    if user_data.empty:
        return jsonify(error='User not found')
    
    prev_history = user_data['ItemsPurchased'].tolist()
    return jsonify(prev_history)
    

if __name__=='__main__':
    app.run(debug=False,port = 1235)