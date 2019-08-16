# -*- coding:utf-8 -*-
from xml.parsers.expat import ParserCreate
from urllib import request

class weathersaxhandler(object):
    def __init__(self):
        super().__init__()

    def start_element(self, name, attrs):
        if 'city' not in name:
            print('城市: %s\n' % name)

        if 'cityname' in attrs:
            print('******************')
            print('地区:',attrs['cityname'])

        if 'temNow' in attrs:
            print('温度:',attrs['temNow'])

        if 'stateDetailed' in attrs:
             print('天气:',attrs['stateDetailed'])
             print('******************\n')

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

def parsexml(xml_str):
    handler=weathersaxhandler()
    parser=ParserCreate()
    parser.StartElementHandler=handler.start_element
    parser.Parse(xml_str)

URL='http://flash.weather.com.cn/wmaps/xml/beijing.xml'
with request.urlopen(URL,timeout=4) as f:
    data=f.read()
result=parsexml(data.decode('utf-8'))
