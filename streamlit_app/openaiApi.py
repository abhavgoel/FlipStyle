from decouple import config
import openai
from user_data_prompt import userData
import random
import requests
import json

openai.organization = config("ORG_ID")
openai.api_key = config("API_KEY")
random.seed(36)
user_id = random.randint(1,500)
# user_data = userData(user_id)

user_data_url = f"http://127.0.0.1:1236/api/user_data/{user_id}"
user_browsing_url = f"http://127.0.0.1:1234/api/browsing_data/{user_id}"
user_purchase_url = f"http://127.0.0.1:1235/api/purchase_data/{user_id}"

user_data = requests.get(user_data_url)
# print(user_data.json())

browsing_history = requests.get(user_browsing_url)
# print(browsing_history.json())

purchase_history = requests.get(user_purchase_url)
# print(purchase_history.json())

def join_json(response):
    str=""
    for i in response:
        str+=i +" "
    return str

# print(join_json(purchase_history.json()))

messages = [
    {"role": "system", "content": f"You are an outfit recommender, that keeps in mind user's past purchase history, online fashion trends and browsing habits of a user. The data of user currently chatting with you is {user_data.json()}. the browsing history products are {join_json(browsing_history.json())} and purchase history products are {join_json(purchase_history.json())}. Dont only revolve around these orders , generate new and relevant outfits just by keeping in mind these details."},
]

# while True:
#     message = input("User : ")
#     if message:
#         messages.append(
#             {"role": "user", "content": message},
#         )
#         chat = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=messages
#         )
    
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})

def outfit_generator(msg):
    message = msg
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
        reply = chat.choices[0].message.content
        return f"{reply}"
        
