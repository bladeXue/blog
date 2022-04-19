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

## 获取帮助信息

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

## 查看仓库状态

查看当前分支和文件修改情况。

```bash
git status
git status --ignored
git status --ignore-submodules
```

## 对比文件修改


```bash
git diff
```






## 总结

好
