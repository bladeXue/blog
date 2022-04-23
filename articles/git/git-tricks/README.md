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

## 关于`checkout`

在以前的写法里，`checkout`命令被称为**检出**，用于切换分支和重置工作区的文件。所以`checkout`的语义有些混乱，为了避免这个问题，新版本的git增加了`switch`和`restore`两个指令，来分割`checkout`的职责。

## 关于`--`

主要是文件名的分隔符，因为在以前的`checkout`里，不用`--`的文件会被当成分支处理，有时候会有麻烦。

## 关于提交规范

目前还是参考[Angular提交规范](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#)多一点。


## 关于分支规范

采用主从分支模型，具体参考Vincent Driessen的[A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)


## 关于合并策略

策略有5种：

1. `--ff`快速合并
2. `--no-ff`提交合并
3. `--squash`伪合并
4. `rebase`变基
5. `cherry-pick`提取

`--squash`和`cherry-pick`除了hotfix一类的场景外尽可能少用，因为会产生不好理解的分支记录（除非你的目的就是隐藏某些提交细节，或想让版本树看上去简洁些）。至于什么时候使用变基一直是个问题，这个看团队自己选择。

## 关于标签

Git的标签有两种：

1. 轻标签：仅添加名称，主要用于本地仓库的一次性使用。
2. 注解标签：添加名称，注解和签名，用于协助管理版本数据库。

## 关于别名

个人不推荐使用别名。

## 关于SourceTree

命令行当然挺好的，实际开发中，SourceTree也挺好的，基本上80%的Git操作都在面板上了。团队如果采用Gui管理Git的话，尽量用一样的比较靠谱。

## 关于托管

Git原生的组织方式就是打补丁后抄送邮件列表，从而达到团队协作的目的。现在流行的Github一类的托管平台不过是把这个步骤自动化了，包括Linux在内的一些老牌项目依旧在使用邮件列表。不管是选择自建，或者上平台，还是用邮件列表，都有各自的优势，但是Github作为第三方平台，是否值得信任要团队自己考虑。可以看看Nimble的Jesse Squires怎么[解释这个问题](https://www.jessesquires.com/blog/2022/04/19/github-suspending-russian-accounts/)。

## 获取Help信息

```bash
git --help
git help -a
```

直接运行`git`命令也可以获得一份指令摘要：

```bash
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```

## 配置`.gitconfig`

```bash
git config --global user.name ""
git config --global user.email ""
```

这里的个人信息不是指Github账户，而是会作为提交人信息记录在版本数据库里。
关于设置代理可以参考[一文让你了解如何为 Git 设置代理](https://ericclose.github.io/git-proxy-config.html)。

## 配置`.gitignore`

参考GitHub官方的模板[github/gitignore](https://github.com/github/gitignore)。主要针对3种文件：

1. 自动生成文件，如各种缓存。
2. 中间编译物和非必要二进制文件（Git不追踪二进制变化）。
3. 屏蔽敏感文件。

检查忽略文件可以使用`check-ignore`：

```bash
git check-ignore -v <filename>
```

## 克隆仓库

```bash
git clone <repo-url>
git clone --depth=1 <repo-url>
git clone -b <branch-name> --single-branch <repo-url>
```

## 提交版本

```bash
git add <filenames>
git commit -m ""
```
> 不使用`-m`参数的话，git会弹出一个编辑器来给你填commit message，一般默认是vim。

## 提交分块

```bash
git add -p <filenames>
```

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

> `apply`一个贮藏时，如果工作区已经有同名文件了，`apply`会被工作区拒绝，此时可以新建一个临时分支来存放`apply`，然后手动合并回原分支来达成目的。

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

现在的做法，使用`restore`来进行还原操作：

```bash
git restore <filename>                       ;; 暂存区->工作区
git restore --staged <filename>              ;; 版本->暂存区
git restore --staged --worktree <filename>   ;; 版本->暂存区->工作区
git restore --source <commit-id> <filename>  ;; 从某次提交中恢复文件到工作区
```

> 丢弃修改仅仅是针对追踪了的文件，想加大力度，可以尝试下面的`git clean`。

## 清理工作区

清空整个工作区，让工作区和版本内容完全一致。

```bash
git clean -d -f
```

按照gitignore记录来清理文件。

```bash
git clean -X -f
```

## 恢复被删文件

先定位到删文件的那一个版本，再用版本号检出具体文件。

```bash
git rev-list -n 1 HEAD -- <filename>                ;; 得到目标版本
git checkout <delete-file-commit-id>^ -- <filename> ;; 回溯文件
```

使用`restore`替换`checkout`的做法。

```bash
git rev-list -n 1 HEAD -- <filename>                   ;; 得到目标版本
git restore -s <delete-file-commit-id>^ -- <filename>  ;; 回溯文件
```

## 对比修改

将当前工作区和**暂存区**进行对比。

```bash
git diff
git diff <filename>  ;; 对比具体文件
```

将暂存区和**最新版本**进行对比。

```bash
git diff --cached
git diff --cached <filename> 
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

## 查看冲突文件列表

展示工作区的冲突文件列表。

```bash
git diff --name-only --diff-filter=U
```

## 重命名文件

如果在文件系统里直接改名或者改目录，Git会把这个文件标记成删除，然后建一个新的，这对于历史跟踪非常不利，推荐使用git的`mv`指令。

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

## 重设第一次提交

`update-ref -d`指令会删除目标引用和其在`.git/logs/`里的记录，然后再次提交工作区会把历史定位回第一次提交。其效果就是会清空里`git log`所有的提交，并将所有的改动放回工作区。

```bash
git update-ref -d HEAD
```

> 但实际上版本并没有消失，只是不显示了而已，在`git reflog`里依旧可以看到所有版本的记录。

> 慎用！

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

## 比较两个分支的历史记录

对比分支1有，但2没有的提交记录。

```bash
git log <branch-id1> ^<branch-id2>
```

## 关联远程仓库

```bash
git remote add origin <repo-url>
```

## 关联远程分支

```bash
git branch -u origin/<branch-id>
```

## 展示本地分支关联远程仓库的情况

```bash
git branch -vv
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

推送是分支推送到分支，不是仓库对仓库。

```bash
git push
git push -u origin master               ;; 向远程推送本地所有提交
git push -f <remote-name> <branch-name> ;; 强制推送
```

## 查看远程分支

```bash
git branch -r   ;; 查看远程分支
git branch -a   ;; 查看远程和本地的所有分支
```

## 查看分支映射关系

```bash
git remote show origin
```

## 同步远程的分支删除情况

```bash
git remote prune origin
```

## 创建分支和切换

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

## 保护性切换

在Git里，分支其实是commit-id的一个别名，所以在以前的写法里，`checkout`除了切换分支，还能用来直接跳转到某一个版本，但是这次跳转不属于任何一个分支，会留下一个分离式的HEAD。在这个HEAD的环境下，做的任何提交都不会影响其它分支。

```bash
git checkout <commit-id>
```

## 快速切换回上个分支

```bash
git switch -
```

## 合并分支和变基

切换到主分支，就可以尝试合并副分支了，合并后，副分支会保留。合并会自己生成一个message，也可以开`-m`自己写。

```bash
git merge <branch-id>           ;; 默认是--ff
git merge --no-ff <branch-id>   ;; 拒绝快速合并
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

## 提取其它分支的提交

```bash
git switch <branch-id> && git cherry-pick <commit-id>
```

## 变基前自动储藏

```bash
git rebase --autostash
```

## 变基的`-i`选项

> 非常NB的选项，可以完成类似“将3次连续提交整合成1次后导入新分支”这样的神奇操作。

使用交互式选项`-i`可以手动选择目标分支上的需要加入主分支的版本，允许改写，替换，删除和合并。

```bash
git rebase -i <branch-id> 
```

## 重命名分支

重命名本地分支。

```bash
git branch -m <new-branch-id>
```

## 删除分支

删除本地分支。

```bash
git branch -d <branch-id>  
```

## 删除已合并分支

删除已经合并到主分支的分支。

```bash
git branch --merged master | grep -v '^\*\| master' | xargs -n 1 git branch -d  ;; 删除已经合并到主分支的副分支
```

## 删除远程分支

删除远程分支。

```bash         
git push origin -d <remote-branch-id>
git push origin :<remote-branch-id>     ;; 和上面一个效果
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

## 一键背锅

查看某段代码是谁写的。

```bash
git blame <filename>
```

## 回收空间

```bash
git gc --prune=now
```

## 总结

不定期更新ψ(｀∇´)ψ
