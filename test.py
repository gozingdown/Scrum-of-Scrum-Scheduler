import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/zhengnetwork.com/messages",
        auth=("api", "key-dacf79d108c1c1b7a9dcbf6b0f46b8fa"),
        data={"from": "Zheng Gong <postmaster@zhengnetwork.com>",
              "to": "Zheng <gongzhenggz@gmail.com>",
              "subject": "Hello Zheng",
              "text": ""})

print send_simple_message()
