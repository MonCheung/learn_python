#itchatmp示例
# -*- coding: utf-8 -*-
import itchatmp
import requests

itchatmp.update_config(itchatmp.WechatConfig(token='ismon',appId='wxe594addf155f5c03',appSecret='89e513e23edbe6e9c883e1a93c0bafdb'))

qr=itchatmp.messages.upload(itchatmp.content.IMAGE,'qrcode.png',permanent=True)
if qr:
    qr=qr['media_id']

print(qr)

menu = {'button':[
    {
        'name': '关于我',
        'sub_button': [
            {
                'type': 'media_id',
                'name': '嘘寒问暖',
                'media_id': qr,
            },
            {
                'type': 'view',
                'name': '神之审美',
                'url':  'https://www.douban.com/people/james1874/',
            },

        ],
    }
]}

m = itchatmp.menu.create(menu)
print(m)

def getResponse(_info):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
     'key': '3d9e296f52384d6caf3de2d9dda509a7',
     'info': _info, #发送的消息
     'userid': 'ismon',
    }

    r = requests.post(apiUrl, data=data).json()

    return r

@itchatmp.msg_register(itchatmp.content.EVENT)
def event_reply(msg):
    if msg['Event'] == 'subscribe':
        return '关注我，你就是最棒的！\n我是小蒙--mon神的小老弟\n马上开始与我唠嗑吧！'
    else:
        pass


@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    if '妈妈' in msg['Content']:
        return '小蒙:' +'我只知道我的妈妈叫小媛'

    elif '爸爸' in msg['Content']:
        return '小蒙:' +'我只知道我的爸爸是mon神'

    if getResponse(msg['Content'])['code'] == 40004:
        return '小蒙:' +'脑容量已超载，我要休息了'

    else:
        try:
            return '小蒙:' + getResponse(msg['Content'])['text']+'\n'+getResponse(msg['Content'])['url']

        except:
            return '小蒙:' + getResponse(msg['Content'])['text']


@itchatmp.msg_register(itchatmp.content.IMAGE)
def img_reply(msg):
    return '小蒙:' +'斗图失败，图片我收了，输我也认了，再见！'


@itchatmp.msg_register(itchatmp.content.VOICE)
def voc_reply(msg):
    return '小蒙:' +'爱上了你的声音，可我却还不会说话！'

itchatmp.run()
