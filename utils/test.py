# coding=utf-8

import json
import os

infoJson="""
{
    "title": "test",
    "release": true,
    "description":"this is just a test article.",
    "date": "2020-06-05 13:43:57",
    "tags": [
        "算法",
        "数据结构",
        "字符串"
    ],
    "categories": [
        "算法",
        "经典算法",
        "字符串"
    ]
}
"""

s = "title: {title}"
info = json.loads(infoJson)
print(s.format(**info))

