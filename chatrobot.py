# -*- coding: utf-8 -*-

"""
功能：测试PyNLPIR包
时间：2018年1月31日
"""
import pynlpir

pynlpir.open()

s='聊天机器人到底该怎么做呢？'
segments=pynlpir.segment(s,pos_english=False,pos_names='all',pos_tagging=True)
for segment in segments:
    print(segment[0],'\t',segment[1],)


key_words = pynlpir.get_key_words(s,weighted=True)
for key_word in key_words:
    print(key_word[0], '\t', key_word[1])

pynlpir.close()
