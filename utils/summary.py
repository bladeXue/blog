# coding=utf-8
import os
import glob
import json

configFilename = "info.json"
summaryFilename = "SUMMARY.md"

articleTemplate = "- {x} {title}({url}){tags}"
categoryTemplate = "## {}"
tagTemplate = "`{}` "
summaryTemplate = """\
# 目录

- [x] 完成
- [ ] 未完成
\
"""

# done


def scanInfos():

    infos = {}
    infoJsons = glob.glob('**/info.json', recursive=True)

    for info in infoJsons:
        # print(info)
        with open(info, "rb") as f:
            data = json.load(f)  # 小心空文件，文件操作要处理好映射关系
            path = info.rstrip().replace(os.sep, "/").replace("info.json", "")
            infos[path] = data

    # 路径名字串:json字典
    return infos


def buildSummaryData(infos):
    articles = {}
    categories = {}
    summaryData = {}
    for path in infos:

        info = infos[path]

        # articleTemplate = "- [{x}​] [{title}​]({url}){tags}"
        article = articleTemplate.format(
            x="[x]" if info["release"] else "[ ]",
            title="["+info["title"]+"]",
            url=path,
            tags=buildTags(info["tags"])
        )

    


def buildTags(tags):
    tagStr = ""
    for tag in tags:
        tagStr =tagStr+tagTemplate.format(tag)
    
    return tagStr


    # for info in scanInfos():
    #     print(info)
    # scanInfos()
if __name__ == "__main__":
    os.chdir("../")
    # 获取所有info文件
    # 克隆文章模板，将info文件解析成单个article
    # 克隆目录模板，填写文章和类别
    infos = scanInfos()
    # for path in infos:
    #     print(infos[path])
    buildSummaryData(infos)
