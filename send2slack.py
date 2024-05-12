from calendar import day_abbr
import json
import os
import webbrowser
import requests

payload = {
    "username": "tmp_bot",
    "icon_emoji": ":power:",
    "text": "Hello, slack!"
}
def send_msg(url:str, msg:str):
    global payload
    payload["text"] = msg
    try:
        data = json.dumps(payload)
        res = requests.post(url, data=data)
        res.raise_for_status() # check the status code
        print(f"status: {res.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"error: {e}")

if __name__ == '__main__':
    # kitalabのserverにメッセージを送るよ
    webhookURL = "***"
    message = "Hello, slack!!"
    send_msg(webhookURL, message)