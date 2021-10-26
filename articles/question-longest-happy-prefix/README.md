---
title: 经典算法题解-最长快乐前缀
date: 2020-06-10 15:48:16
tags:
- 算法
- 字符串
- 习题
categories:
- [算法, 算法题解]
---

# 最长快乐前缀问题

> 题目描述来源：[LeetCode-最长快乐前缀](https://leetcode-cn.com/problems/longest-happy-prefix/)
> 题目难度：困难
> 本题是KMP算法的应用变种，阅读本文前最好阅读一下我的另一篇博客[最大相同前缀后缀问题](https://bladexue.github.io/2020/06/04/algorithm/classical-algorithm-maximum-same-prefix-suffix/)中对于最大相同前缀后缀问题的讨论
<!-- more -->
#### 问题描述

定义：快乐前缀，是在原字符串中既是**非空**前缀也是后缀（不包括原字符串自身）的字符串

问题要求：

1. 给你一个字符串s，请你返回它的**最长快乐前缀**
2. 如果不存在满足题意的前缀，则返回一个空字符串

示例：

1. 给出```S = "ababab"```，输出```"abab"```
2. 给出```S = "leetcodeleet"```，输出```"leet"```
3. 给出```S = "a"```，输出```""```

#### 问题分析

如果你有好好看完我开头提到的那篇讲前后缀的文章，那么这个题目的解答显而易见了，其实就是KMP算法中next\[]数组的定义，通过遍历字符串，递推构造就行，代码甚至可以直接从[最大相同前缀后缀问题](https://bladexue.github.io/2020/06/04/algorithm/classical-algorithm-maximum-same-prefix-suffix/)里抄过来，只要针对长度为0和1的输入进行一点点调整即可。不多废话，直接看代码

#### 代码示例

这里只给出Java的示例，基本是next\[]的简单修改，如果看不懂请回到我那篇讲前后缀问题的博客看一下

```java
class Solution {

    static int[] getMax(String pat) {

        int len = pat.length();
        int[] max = new int[len];
        max[0] = 0;

        int i = 0;  // 表示当前最大共缀长度的候选值
        int j = 1;  // 从第二位开始遍历

        while (j < len) {

            if (pat.charAt(i) == pat.charAt(j))
                max[j++] = ++i;
            else if (i == 0)
                max[j++] = 0;
            else
                i = max[i - 1]; // 递推核心
        }

        return max;
    }

    public String longestPrefix(String s) {

        int len = s.length();

        if (len < 2) {
            return "";
        } else {
            return s.substring(0, getMax(s)[len - 1]);
        }
    }
}
```
> 时间复杂度O(N)，空间复杂度O(N)

在LeetCode上的运行结果如下，可以看出整体效率还是比较高的：

![result](./images/result.png "result")

#### 总结

这一类的问题很常见，基本就是某一个经典算法的子问题，比如本题就是KMP算法的子问题，也就是求next\[]数组的问题，如果你发现代码有改进之处，或者发现了bug，记得在评论区bb我，感谢阅读

