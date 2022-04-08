# 经典算法题解-两个子串

施工ing

> 这个是2018年京东校招的笔试题
> 本质是KMP算法子问题的“最大相同前后缀”的变种（也就是next\[]数组的构造问题），我的另一篇博客[最大相同前缀后缀问题](https://bladexue.github.io/2020/06/04/algorithm/classical-algorithm-maximum-same-prefix-suffix/)有讨论，看本文前请先花20分钟看一下

#### 问题描述

#### 问题分析

如果有好好读完我那篇关于前后缀的文章，那么这个题目的解答





#### 示例代码


```java
class Solution {

    static int[] getNext(String pat) {

        int len = pat.length();
        int[] next = new int[len];
        next[0] = 0;

        for (int i = 0, j = 1; j < len; j++) {

            while (pat.charAt(i) != pat.charAt(j) && i > 0)
                i = next[i - 1];

            if (pat.charAt(i) == pat.charAt(j))
                next[j] = ++i; 
            else
                next[j] = 0;   
        }
        return next;
    }

    public String longestPrefix(String s) {
        
        int len = s.length();

        if (len < 2) {
            return "";
        } else {

            return s.substring(0, getNext(s)[len - 1]);
        }
    }
}
```