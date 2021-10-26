---
title: Linux命令汇总
date: 2020-03-20 16:59:56
tags: 
- linux
categories: 
- Linux
---

# Linux常用命令汇总

#### 关于本文

这里整理工作和学习中常用的Linux命令，长期更新，部分命令会给出实际案例
> 本文是命令收录，不是正儿八经的教程，教程还得看鸟哥的
> 写错的地方，可以在评论区bb我，Disqus要梯子

#### 命令收录

目录相关：

|命令|描述|备注|
|-|-|-|
|cd [dir]|切换目录，单一个cd和cd ～同意，切回用户根目录，cd -表示回溯之前停留的目录，支持绝对和相对路径|cd的权限指向x，不是r|
<!-- more -->
#### 一些碎碎念

###### 1. cd命令的权限

如果有一个权限模型为drw-rw-rw-的目录test，用户是无法使用cd切换到该目录的，因为根据Linux的权限模型，将当前目标作为参数递给一个程序（比如cd test/）就是执行行为，权限类型会划给执行。Linux权限模型中的可读和可写和我们一般认为的不太一样，主要是由于Unix哲学的“一切皆文件”，目录本身也是一个文件，可读和可写是针对目录本身而言的，而不是目录下的各个文件。但root用户是无视的，root用户可以cd进任何一个目录，无论是不是有执行权限

<img src="/images/linux/cd的权限.png" title="cd的执行权限" style="max-width:80%" />


#### 一个有趣的小程序

安利一个有用的小程序，用于速查各种命令的手册，出品方是[Linux中国](https://linux.cn/)，项目本身是开源的，有兴趣的达瓦里希可以去贡献自己的命令条目

<img src="/images/linux/linux小程序.jpg" title="Linux小程序" style="max-width:50%" />

界面很简介，直接搜索命令就行了：

<img src="/images/linux/linux小程序详情.jpg" title="Linux小程序主页面" style="max-width:50%" />



