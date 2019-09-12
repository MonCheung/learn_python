#itchatmp示例
# -*- coding: utf-8 -*-
import itchatmp

qr=itchatmp.messages.upload(itchatmp.content.IMAGE,'qrcode.png',permanent=True)
if qr:
    qr=qr['media_id']
print(qr)

media_id=qr
menu = {'button':[
    {
        'name': '关于我',
        'sub_button': [
            {
                'type': 'click',
                'name': '嘘寒问暖',
                'key': 'qr-key',
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
print(r)
