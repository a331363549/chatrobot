# -*- coding: utf-8 -*-  

""" 
功能：LTP云平台测试
时间：2018.1.31
"""
import requests


resp = requests.get("http://api.ltp-cloud.com/analysis/?api_key=t1M6G6M8F7ZODNOkeB8TJVvinXgSNjVzCLStipuK&text=我是中国人。&pattern=ws&format=plain")
print(resp.text)

