# vivo便签转小米笔记工具，子品牌iqoo，红米同样适用
## 使用教程

1、从小米的云服务中拿到对应的Cookie，填写到setting.py文件中
```python
xiaomi = {
    # 此选项隔一会就会过期，需要注意,在接口https://i.mi.com/note/note 的请求参数中获取
    "serviceToken": '', # # 从请求参数获取

    # 设置请求头   Cookie此选项隔一会就会过期，需要注意
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Cookie": ""  # 从请求头获取
    }

}

```

2、从vivo的云服务中拿到对应的Cookie，填写到setting.py文件中
```python
vivo = {
    "header": {
        "X-Yun-Csrftoken": '', # 从请求头获取
        "Cookie": "", # 从请求头获取
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Host': 'webcloud.vivo.com.cn',
        'Origin': 'https://yun.vivo.com.cn',
        'Referer': 'https://yun.vivo.com.cn/',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
}

```

3、默认会在笔记内容底部添加创建时间和更新时间，如果不需要，可以在setting.py中设置
```python
# 是否在笔记内容底部添加创建时间和更新时间
addTime = True
```
