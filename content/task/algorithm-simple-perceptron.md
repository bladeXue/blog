---
title: 初识感知机算法
date: 2020-05-22 14:40:11
tags:
- 算法
- 神经网络
categories:
- [算法]
---

# 初识感知机算法
<!-- more -->
#### 现代神经网络的基础-感知机算法

感知机（英语：Perceptron）是康奈尔航空实验室的Frank Rosenblatt在1957年提出的一种神经网络结构，其本质是一种二元分类器，目前在机器学习领域都认为感知机是最早出现的一种简单前馈神经网络
> 基本上在计算机领域，由于历史渊源，算法中的很多概念都是来自数字电路的数学设计模型，比如像感知机和状态机这种类似xx机这种命名，最早都是数字电路的概念，在本文的后面我们会体会到这一点的

前文提到了感知机是一个二元分类器，什么是二元分类，其实就是把一系列具有同种属性的(x,y)的物体集合{(x,y)}进行分类，对其中某个个体来说，x是其属性，y是其分类结果，在这种分类中，y只有诸如0/1和true/false这样的两种结果，所以称为二元分类器。
<div style="margin:auto;">
<img src="/images/algorithm/liner.png" title="sombra" alt="sombra" style="max-width:50%;margin-bottom: 0;"/>
<p style="text-align: center;">图1-我用Matplotlib写的一个线性分类器的案例</p>
</div>


