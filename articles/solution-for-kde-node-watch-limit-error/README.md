---
title: 解决Node报错 System limit for number of file watchers reached
date: 2020-03-21 15:27:40
tags: 
- linux
- manjaro kde plasma
categories:
- [Linux, 踩坑日常]
---

# 解决 Error: ENOSPC: System limit for number of file watchers reached

#### 问题场景

最近突发奇想想写一个小例子，为了图省事直接用browser-sync做了个小服务器，用了简单粗暴的一条命令：

```shell
$ browser-sync start --server --files "**"
```

这条命令以前一直没什么问题，我的系统是Manjaro Kde Plasma 19.0.2，报了一个奇奇怪怪的错误Error: ENOSPC: System limit for number of file watchers reached，完整输入如下：
<!-- more -->
```shell
[Browsersync] Access URLs:
 -------------------------------------
       Local: http://localhost:3000
    External: http://192.168.1.10:3000
 -------------------------------------
          UI: http://localhost:3001
 UI External: http://localhost:3001
 -------------------------------------
[Browsersync] Serving files from: ./
[Browsersync] Watching files...
events.js:293
      throw er; // Unhandled 'error' event
      ^

Error: ENOSPC: System limit for number of file watchers reached, watch '/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/rxjs/observable/SubscribeOnObservable.js.map'
    at FSWatcher.<computed> (internal/fs/watchers.js:169:26)
    at Object.watch (fs.js:1366:34)
    at createFsWatchInstance (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:38:15)
    at setFsWatchListener (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:81:15)
    at FSWatcher.NodeFsHandler._watchWithNodeFs (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:233:14)
    at FSWatcher.NodeFsHandler._handleFile (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:262:21)
    at FSWatcher.<anonymous> (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:495:21)
    at FSReqCallback.oncomplete (fs.js:171:5)
Emitted 'error' event on FSWatcher instance at:
    at FSWatcher._handleError (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/index.js:260:10)
    at createFsWatchInstance (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:40:5)
    at setFsWatchListener (/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/chokidar/lib/nodefs-handler.js:81:15)
    [... lines matching original stack trace ...]
    at FSReqCallback.oncomplete (fs.js:171:5) {
  errno: -28,
  syscall: 'watch',
  code: 'ENOSPC',
  path: '/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/rxjs/observable/SubscribeOnObservable.js.map',
  filename: '/home/blade/桌面/github-project/j2ee-demo/chapter01/message-board/node_modules/rxjs/observable/SubscribeOnObservable.js.map'
}
```

#### 问题解决

从报错的字面看，是操作系统限制了node脚本运行监视的文件数目，本着“99%的计算机问题都有前辈解决过”原则，直接把报错丢上[stackoverflow.com](https://stackoverflow.com/)，然后找到了这篇[metro-bundler-ready-error-enospc-system-limit-for-number-of-file-watchers-reac](https://stackoverflow.com/questions/54532803/metro-bundler-ready-error-enospc-system-limit-for-number-of-file-watchers-reac)，按照前辈们踩坑之路顺利解决了

```shell 
// 应该存在一个/etc/sysctl.d/50-max_user_watches.conf的文件
$ cd /etc/sysctl.d                              
$ cat 50-max_user_watches.conf 
fs.inotify.max_user_watches = 16384
```
用vim将限制数16384修改成524288后，启用修改：
```shell
$ sudo sysctl -p
$ sudo sysctl --system
```

#### 总结

从问题上看是简单粗暴用browser-sync监视了所有文件导致的，我这里应该是把node_modules/中的文件也纳入监视了，导致监视数爆了，除了修改50-max_user_watches.conf，其实简单修改一下sync命令也可以，只监控需要参与变动的文件：

```shell
$ browser-sync start --server --files "dist/**, pages/**"
```
