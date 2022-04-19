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

## 关于分支

采用主从分支模型，具体参考Vincent Driessen的[A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)

## 关于变基

？

## 关于标签

Git的标签有两种：

1. 轻标签：仅添加名称，主要用于本地仓库的一次性使用。
2. 注解标签：添加名称，注解和签名，用于协助管理版本数据库。

## 关于别名

？

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

## 删除文件

```bash
git rm <filename>           ;; 连本地文件和索引一起删除
git rm --cached <filename>  ;; 放弃索引，但会保留本地文件
```

查看索引区：

```bash
git ls-files --stage
```

## 重置版本

本质是通过重写`.git/refs/`来重置版本（切换版本），通过重置引用指针可以达到回退版本的目的。

```bash
git reset --hard <commit-id>    ;; 仅重置HEAD位置
git reset --soft <commit-id>    ;; 仅重置HEAD，索引
git reset --mixed <commit-id>   ;; 重置HEAD，索引，工作树
```

提交新版本，或者切换版本都会在`.git/logs/`会留下相应的指针变动记录，想查看可以使用：

```bash
git reflog <branch-id>
```

## 修改最近一次版本

取缔最近一次提交并和当前缓冲区融合，变成一次新提交。如果缓存区没有内容，那么仅仅修改上一次提交的message。

```bash
git commit --amend
```

## 还原版本

类似`reset`，但是产生一个新版本。

```bash
git revert <commit-id>  ;; 会产生一个“否定了目标版本”的新版本
git revert HEAD         ;; 撤销前一次提交
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
git log --abbrev-commit     ;; 简化版本id
git log --pretty=oneline    ;; 简短版输出
git log --graph             ;; 输出树形图
git log --decorate          ;; 输出注解
```

查看目标版本的具体信息。

```bash
git show
git show <commit-id>  
```

## 关联远程仓库

```bash
git remote add origin <repo-url>
```

## 建立远程分支副本

```bash
git checkout -b <branch-id> origin/<branch-id>
```

## 建立上游分支

```bash
git branch --set-upstream-to <branch-id> origin/<branch-id>
```

## 查看远程仓库

```bash
git remote 
git remote -v
```


## 获取远程仓库

```bash
git pull
```

这个命令等同于```git fetch && git merge```，很多情况下不建议使用（而且这里的`merge`还是fast-forward），推荐直接```git fetch```然后手动处理冲突。

想要获取远程仓库并重置状态，可以获取后强行同步成远端版本：

```bash
git fetch --all && git reset --hard origin/master
;; --all是获取所有remote
```

## 推送远程仓库

```bash
git push
git push -u origin master   ;; 向远程仓库推送本地master的所有提交
```
## 创建分支

以前的写法：

```bash
git checkout -b <branch-id>
```

这个命令等同于：`git branch <branch-id> && git checkout <branch-id>`。现在推荐的写法，使用`switch`替换`checkout`来切换分支：

```bash
git branch                      ;; 查看分支
git branch <branch-id>          ;; 新建分支
git switch -c <branch-id>
git switch --create <branch-id>
```

## 快速切换回上个分支

```bash
git switch -
```

## 合并分支和变基

切换到主分支，就可以尝试合并副分支了，合并后，副分支会保留。

```bash
git merge <branch-id>           ;; 默认是--ff
git merge –no-ff <branch-id>    ;; 拒绝快速合并
git merge --squash <branch-id>  ;; 伪合并，将副分支上的所有版本直接
                                ;; 做一个汇总版暂存到主分支，不产生交汇
```

采用**变基**，将副分支上的版本在主分支上重新提交（并处理相关冲突），副分支不会消失但是指针会贴主分支上。

```bash
git rebase <branch-id>  ;; 如果变基过程发生冲突，就要修改后再次add
git rebase --continue   ;; add后才能用这行命令，此时Git会让你填message
git rebase --skip       ;; 无视冲突，直接提交
git rebase --abort      ;; 放弃变基
```

## 合并其它分支的某次历史提交

```bash
git switch <branch-id> && git cherry-pick <commit-id>
```

## 变基的`-i`选项

> 非常NB的选项。

使用交互式选项`-i`可以手动选择目标分支上的需要加入主分支的版本，允许改写，替换，删除和合并。

```bash
git rebase -i <branch-id> 
```

## 删除分支

```bash
git branch -d <branch-id>
```

## 添加标签

```bash
git tag                     ;; 查看标签
git tag <tag-name>          ;; 添加轻标签
git tag -a <tag-name>       ;; 添加注解标签
git tag -am "" <tag-name>   ;;
git tag -n                  ;;  查看列表
```

## 删除标签

```bash
git tag -d <tagname>
```

## 回收

```bash
git gc --prune=now
```

## 忽略文件

？

## 总结

好
