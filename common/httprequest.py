#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

from urllib import request, parse


def httpget(url,header,data=None):
    '''http get request, url为必传参数，url中的参数需要提前拼接好，
    header可根据需要为None get 场景 data不传入'''
    req = request.Request(url)
    if header:
        for k,v in header:
            req.add_header(k,v)
      
    getapi = request.urlopen(req)
    response = getapi.read()
    responsecode = getapi.status
    responsedes = getapi.reason

    print("response code:",responsecode)
    print("reason:",responsedes)
    getapi.close()


#httpget('https://api.douban.com/v2/book/2129650',None,None)

def httppost(url,header,data):
    '''url为post api的地址，api地址如果包含参数，需要提前拼接好。
    post 必须传入data. header可根据实际情况可以不传入，即None即可'''
    req = request.Request(url)
    if header:
        for k,v in header:
            req.add_header(k,v)
    data = parse.urlencode(data)
    
    postapi = request.urlopen(req, data = data.encode('utf-8'))

    responsecode = postapi.status
    responsedes = postapi.reason

    print("response code:",responsecode)
    print("reason:",responsedes)
    postapi.close()

