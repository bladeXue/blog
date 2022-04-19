# Git小魔术

Git的命令繁多，这里收录一些常用的命令片段和知识碎片，用作平时快速复习和CV。

> 文章使用的Git是`2.35.2`版本，诸如`checkout`等命令已经被`switch`和`restore`替代了，使用时请和传统教程区分。

## 关于`.git`目录

这个目录是Git仓库的本体，可以由`git init`创建，操作Git的过程其实就是修改`.git`目录下文件的过程，目录下包括：

```bash
+---hooks/      ;; 存放钩子脚本
+---info/       ;; 存放规则和分支信息
+---logs/       ;; 日志和分支变动记录
+---objects/    ;; 存储具体的版本对象
+---refs/       ;; 各类引用和标签
|   config      ;; 仓库配置文件
|   description ;; 仓库描述
\   HEAD        ;; 一个纯文本文件，存的是当前版本号ID
```

## 关于引用

Git仓库的每一个版本其实都是一个文本补丁的压缩包，称为Git对象，存放在`.git/objects/`目录下，每个Git对象的文件名都是一个SHA1计算出来64位数字，作为这个版本的`commit-id`。可以使用引用替代`commit-id`。

形似`HEAD^^2^^~3`称为**相对引用**，详情参考[Git Head 解释](https://www.wonderhows.com/post/git-head-explaination/)

> 注意相对引用必须“先树后线”。

## 获取Help信息

```bash
git --help
git help -a
```

## 配置个人信息

```bash
git config --global user.name ""
git config --global user.email ""
```

这里的个人信息不是指Github账户，而是会作为提交人信息记录在版本数据库里。
关于设置代理可以参考[一文让你了解如何为 Git 设置代理](https://ericclose.github.io/git-proxy-config.html)。

## 提交版本

```bash
git add <filenames>
git commit -m ""
```
> 不使用`-m`参数的话，git会弹出一个编辑器来给你填commit message，一般默认是vim。

## 提交驻藏

贮藏其实是一个无状态版本，可以在`.git/refs/stash`里找到贮藏引用。

```bash
git stash       ;; 贮藏当前索引区，包括暂存和非暂存
git stash -u    ;; 贮藏整个工作区，包括没索引的文件
```

查看驻藏列表。

```bash
git stash list
```

使用驻藏。

```bash
git stash apply <stash@{n}> ;; 应用某个贮藏
git stash pop               ;; 弹出最近一次贮藏
```

清空贮藏。

```bash
git stash clear
```

> 养成随手贮藏的好习惯可以帮你避免很多麻烦。

## 丢弃修改

以前的做法，使用`checkout`：

```bash
git checkout
git checkout -- <filename>  ;; --是必须的，不然checkout会跑去切换分支
```

现在的做法，使用`restore`：

```bash
git restore <filename>          ;; 将未暂存的修改丢弃
git restore --staged <filename> ;; 将已暂存的修改设置为未暂存
```

## 对比修改

将当前**工作区**和**暂存区**进行对比。

```bash
git diff
git diff -- readme.txt  ;; 对比具体文件
```

查看当前至**目标版本**或**任意两个版本**的对比。

```bash
git diff <commit-id>                ;; <ref-id>也是可以的
git diff <commit-id> <commit-id>
```

检索工作区的冲突文件列表。

```bash
git diff --name-only --diff-filter=U
```

详细展示一行中的修改。

```bash
git diff --word-diff
```

## 切换版本

本质是通过重写`.git/refs/`来切换版本，通过重置引用指针可以达到回退版本的目的。

```bash
git reset --hard <commit-id>
```

提交新版本，或者切换版本都会在`.git/logs/`会留下相应的指针变动记录，想查看可以使用：

```bash
git reflog <branch-id>
```

## 查看仓库状态

查看当前分支和文件修改情况。

```bash
git status
git status --ignored
git status --ignore-submodules
```

## 查看历史版本

查看历史版本列表。

```bash
git log
git log --pretty=oneline    ;; 简短版输出
```

查看目标版本的具体信息。

```bash
git show
git show <commit-id>  
```

## 推送远程仓库

```bash
git push
```

## 获取远程仓库

```bash
git pull
```

这个命令等同于```git fetch && git merge```，很多情况下不建议使用，推荐直接```git fetch```然后手动处理冲突。

想要获取远程仓库并重置状态，可以获取后强行同步成远端版本：

```bash
git fetch --all && git reset --hard origin/master
;; --all是获取所有remote
```








## 快速切换回上一个分支

```bash
git switch -
```

## 忽略文件

## 总结

好
