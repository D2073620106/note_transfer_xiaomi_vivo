import datetime
import time

import requests
import json


# 小米笔记 包含创建和保存
class XiaoMiNote:
    noteId = ''
    serviceToken = ''
    headers = {}
    # 创建时间,初始化的时候不传入默认当前时间，传入了则使用传入时间--->后经测试，不可用，传入了时间，接口创建出出来的还是会使用当前时间
    createDate = ''
    content = ''
    title = ''

    def __init__(self, serviceToken=None, headers=None, content=None, title=None):
        if (serviceToken is None) or (headers is None) or (content is None) or (title is None):
            raise Exception('serviceToken、headers、content或者title未传入')
        self.serviceToken = serviceToken
        self.headers = headers
        self.content = content
        self.title = title
        self.createDate = int(datetime.datetime.now().timestamp() * 1000)
        print('初始化完成')

    def now(self):
        return int(datetime.datetime.now().timestamp() * 1000)

    def createNote(self):

        obj = {"content": "", "colorId": 0, "folderId": "0", "createDate": self.createDate, "modifyDate": self.now()}
        kw = {
            'entry': json.dumps(obj),
            "serviceToken": self.serviceToken
        }
        # 发送请求 创建笔记
        res = requests.post("https://i.mi.com/note/note", data=kw, headers=self.headers)
        if res.status_code != 200:
            raise Exception('创建笔记请求失败，状态码：' + str(res.status_code))
        data = json.loads(res.text)
        self.noteId = str(data.get('data').get('entry').get('id'))
        print('创建笔记完成')

    def setContent(self, content):
        self.content = content

    def setTitle(self, title):
        self.title = title

    def saveNote(self, addTime=True, createTime=None,updateTime=None):
        createTimeStr = ''

        if updateTime:
            createTimeStr += '\n<text indent=\"1\"></text>\n<text indent=\"1\"><u><background color=\"#4139ff\"><b><i>更新时间：{}</i></b></background></u></text>'.format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(int(updateTime)/1000))))

        if createTime:
            createTimeStr += '\n<text indent=\"1\"></text>\n<text indent=\"1\"><u><background color=\"#9affe8af\"><b><i>创建时间：{}</i></b></background></u></text>'.format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(int(createTime)/1000))))


        # 保存笔记
        obj = {
            "id": self.noteId,
            "tag": self.noteId,
            "status": "normal",
            "createDate": self.createDate,
            "modifyDate": self.now(),
            "colorId": 0,
            "folderId": "0",
            "alertDate": 0,
            "extraInfo": {"title": self.title},
            "content": self.content + createTimeStr if (addTime and createTimeStr != '') else self.content
        }
        kw2 = {
            'entry': json.dumps(obj),
            "serviceToken": self.serviceToken
        }
        # https://i.mi.com/note/note/38151228775875424
        url = "https://i.mi.com/note/note/" + self.noteId
        res = requests.post(url, data=kw2, headers=self.headers)
        if res.status_code != 200:
            raise Exception('保存笔记请求失败，状态码：' + str(res.status_code))
        data = json.loads(res.text)
        print('保存笔记完成')
