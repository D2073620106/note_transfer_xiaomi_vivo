# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from time import sleep

import setting
from xiaomi.XiaoMi import XiaoMiNote
from vivo.Vivo import VivoNote


def start():
    vivoNote = VivoNote(headers=setting.vivo.get('header'))
    # 获取vivo笔记列表，暂时只获取1页，一页500条
    vivoData = vivoNote.getNoteList()
    for index, item in enumerate(vivoData.get('noteList')[::-1]):  # [0:2]    [78:131]    [::-1]倒序
        vivoDeteil = vivoNote.getDetail(item.get('id'))
        content = vivoDeteil.get('data').get('noteDetail')
        title = item.get('title')
        xiaoMiNote = XiaoMiNote(serviceToken=setting.xiaomi.get('serviceToken'), headers=setting.xiaomi.get('headers'),
                                content=content, title=title)
        xiaoMiNote.createNote()
        # 需要添加创建时间，创建时间为createTime
        xiaoMiNote.saveNote(addTime=setting.addTime, createTime=item.get('createtime'), updateTime=item.get('updatedate'))
        print('==================成功添加第{}条==================='.format(index))
        # sleep(1)


if __name__ == '__main__':
    start()
