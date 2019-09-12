import json
data = {
 'key': '3d9e296f52384d6caf3de2d9dda509a7',
 'info': '查询快递0013259337250101', #发送的消息
 'userid': 'ismon',
}

r=json.dumps(data)
print(r)
