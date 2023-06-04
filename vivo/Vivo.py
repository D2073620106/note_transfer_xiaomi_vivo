import datetime
from urllib import parse

import requests
import json


class VivoNote:
    headers = {}

    def __init__(self, headers=None):
        if (headers is None):
            raise Exception('headers未传入')
        self.headers = headers
        print('初始化完成')

    def getNoteList(self):
        obj = {
            "pageSize": "500",
            "pageNum": "1",
            "folderName": "便签",
        }
        payload = parse.urlencode(obj)
        res = requests.post('https://webcloud.vivo.com.cn/yunnote/querynotelist', data=payload, headers=self.headers)
        # res.json()
        print(res)
        if res.status_code != 200:
            raise Exception('拉取笔记列表请求失败，状态码：' + str(res.status_code))
        data = json.loads(res.text)
        print('获取列表成功')
        return data.get('data')


    def getDetail(self, noteId=None):
        if noteId is None:
            raise Exception('请传入noteId')
        obj = {
            "noteId": str(noteId),
            # "noteId": str(19436986913),
            "IEFlag": True,
        }
        payload = parse.urlencode(obj)
        res = requests.post('https://webcloud.vivo.com.cn/yunnote/querynotedetail', data=payload, headers=self.headers)
        if res.status_code != 200:
            raise Exception('拉取笔记详情请求失败，状态码：' + str(res.status_code))
        data = json.loads(res.text)
        print('获取笔记详情成功')
        return data
