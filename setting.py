xiaomi = {
    # 此选项隔一会就会过期，需要注意
    "serviceToken": '',

    # 设置请求头   Cookie此选项隔一会就会过期，需要注意
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Cookie": ""
    }

}

vivo = {
    "header": {
        "X-Yun-Csrftoken": '',
        "Cookie": "",
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


# 是否在笔记内容底部添加创建时间和更新时间
addTime = True