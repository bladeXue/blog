# coding=utf-8
import os
import glob
import json

configFilename = "info.json"
summaryFilename = "SUMMARY.md"

articleTemplate = "- {x} {title}({url}){tags}  {desc}"
tagTemplate = "`{}` "
categoryTemplate = """
## {cate}

"""
summaryTemplate = """\
# 目录

- [x] 完成
- [ ] 未完成
{summaryStr}
"""


def scanInfos():

    infos = {}  # 路径名字串:json字典
    infoJsons = glob.glob('**/{}'.format(configFilename), recursive=True)

    for info in infoJsons:
        with open(info, "rb") as f:
            data = json.load(f)  # 小心空文件，文件操作要处理好映射关系
            path = info.rstrip().replace(os.sep, "/").replace("info.json", "")
            infos[path] = data

    return infos


def buildTags(tags):
    tagStr = ""
    for tag in tags:
        tagStr = tagStr+tagTemplate.format(tag)

    return tagStr


def buildSummaryData(infos):

    categories = {}  # 字符串:["",""]
    categoriesData = ""
    for path in infos:

        # 获取文章信息和路径
        info = infos[path]

        # 为每篇文章生成字符串
        # articleTemplate = "- {x} {title}({url}){tags}  {desc}"
        article = articleTemplate.format(
            x="[x]" if info["release"] else "[ ]",
            title="["+info["title"]+"]",
            url=path,
            tags=buildTags(info["tags"]),
            desc=info["description"],
        )
        # 将每篇文章分类，类别唯一，注意空的情况
        category = info["categories"][0]
        if categories.get(category) == None:
            categories[category] = [article]
        else:
            categories[category].append(article)

    for category in categories:
        categoriesData = categoriesData + \
            categoryTemplate.format(cate=category)
        for article in categories[category]:
            categoriesData = categoriesData + article+"\n"

    return summaryTemplate.format(summaryStr=categoriesData)


if __name__ == "__main__":

    if os.listdir(".").count(summaryFilename) < 1:
        print("!!!wrong directory")
        print("execute from the dir where gets "+summaryFilename)
        exit(0)

    with open(summaryFilename, "w+", encoding="UTF-8") as f:
        f.write(buildSummaryData(scanInfos()))
