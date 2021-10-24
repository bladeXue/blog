---
title: 图论专栏-导读
date: 2020-08-15 22:43:37
tags:
- 算法
- 数据结构
- 图论
categories:
- [算法, 数据结构, 图论专栏]
---

# 图论专栏导读-如何阅读本系列博客

> 图论专栏系列文章的导读和目录

#### 关于专栏

图论算法是一个重要的算法领域，其参与构成了几乎所有计算机领域的算法基础，图论作为数学和计算机分支前后发展了近300年，整个领域的研究至今依旧活跃。我把写的一系列图论的相关理解和算法笔记编辑成博客，收录成了一个专栏，本文是这些文章的导读，同时也是总索引，希望我的这些文章可以帮助你一窥图论的真实秘密
<!-- more -->

#### 阅读之前

本专栏**默认**你已经有了数据结构和组合数学的一些基础，懂得单链表在内的基本数据结构，懂得辨识树的各个结构和性质，最好懂一些集合论和二元关系，如果想看相关的理论基础篇，也可以issue或者评论，我会把这些知识编辑成番外篇补充在文后

专栏内的文章最早是我的上课笔记和辅导学弟学妹的讲义，现编辑成博文，每篇文章都可以单独阅读，但是其中的储备知识是前驱的，建议从图的概念开始顺序阅读，博文中出现的代码均收录在[graph-algorithm-kit](https://github.com/bladeXue/graph-algorithm-kit)

#### 阅读之后

这里列出了我认为的一个程序员读完本系列后必须掌握的**硬知识**：

1. 图的基本概念（点边模型，连通性问题，子图概念和树图转换）
2. 图的4种存储（矩阵，表，十字链表和多重表）和基本操作（封装和核心API）
3. 图的2个核心搜索（BFS和DFS）
4. 图的4个重点应用问题（最小生成树，最短路径，拓扑排序，关键路径）

以及一些我认为比较重要的**软实力**：

1. 对实际问题进行建模
2. 针对问题场景修改存储结构
3. 将复杂的图论问题转换成已知问题的解
4. 分辨不可解问题（有些问题在图论上属于无定论）

#### 图的概念和基本性质

> 基础篇必读

1. [初识图论-概念和模型](/2020/08/16/algorithm/data-structure/graph-theory/graph-theory-first-learn-and-concepts/)
2. 二部图的概念
3. 欧拉图和一笔画问题
4. 哈密尔顿图的概念

#### 图的存储模型

> 要想使用图，必须先将图从纯粹数学模型，转换为计算机可以理解和存储的代码结构

> 记住图的设计重点就是**把图的表示和实现分离开来**，良好的封装是代码可读性的保障

1. [图的存储结构及封装](/2020/08/19/algorithm/data-structure/graph-theory/graph-theory-storage-structure/)
2. AOE和AOV

#### 5个基本问题和8个核心算法

###### 1. 图的搜索和连通性问题

- [深度优先搜索和广度优先搜索](/2020/09/04/algorithm/data-structure/graph-theory/graph-theory-search/)
- 连通性问题

###### 2. 最短路径问题

- [Dijkstra算法](/2020/09/05/algorithm/data-structure/graph-theory/graph-theory-dijkstra-algorithm/)
- Floyd-Warshall算法

###### 3. 最小生成树问题 

- Prim算法
- Kruskal算法

###### 4. 拓扑排序问题

- TSA

###### 5. 关键路径问题

- CPA

#### 图论算法进阶

- 欧拉图，哈密尔顿图和二部图
- 填色问题和四色原理
- 网络流问题
- 强连通性问题
- 子图覆盖问题
- 同构问题
- 自动机

#### 图论题集

- 割点问题
 


















