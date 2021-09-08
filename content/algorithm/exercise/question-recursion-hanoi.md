---
title: 经典算法题解-汉诺塔
date: 2020-04-16 14:00:21
tags:
- 算法
- 递归
categories:
- [算法, 算法题解]
---

# 递归算法实现汉诺塔
<!-- more -->
#### 代码实例

```java
package com.blade.exercise.recursion.hanoi;

import java.util.Stack;

public class App {

    private static Integer callCount = 0;   // 空间复杂度计数器
    private static Integer moveCount = 0;   // 时间复杂度计数器

    /**
     * 把from栈上n个元素移植到to栈上
     * 从src上的n个元素中，取出n-1移动到aux上
     */
    private static void move(Stack<Integer> src, Stack<Integer> des, Stack<Integer> aux, Integer num) {

        // 计数器和日志型输出
        callCount++;
        System.out.println("move "+(num)+" elements form src."+ src +" to des." + des + " with aux." + aux);

        if (num == 1) {
            moveCount++;
            des.push(src.pop());
        } else {
            // 递归核心，大问题依赖小问题的解决，会有空间延伸
            move(src, aux, des, num-1); // 移动n-1的上层建筑到辅助柱
            move(src, des, aux, 1);     // 移动底盘到目标柱
            move(aux, des, src, num-1); // 移动n-1的上层建筑回到目标柱上的底盘上
        }
    }

    public static void main(String[] args) {

        Stack<Integer> src = new Stack<>();
        Stack<Integer> aux = new Stack<>();
        Stack<Integer> des = new Stack<>();

        src.push(5);
        src.push(4);
        src.push(3);
        src.push(2);
        src.push(1);
        System.out.println("src stack: " + src + "\ndes stack: " + des +"\naux stack: " + aux);

        System.out.println("********************* Start To Move Elements **********************");
        move(src, des, aux, src.size());
        System.out.println("********************* Stop To Move Elements **********************");

        System.out.println("total call count: " + callCount + " times");
        System.out.println("total move count: " + moveCount + " times, equals to -1+2^n");
        System.out.println("src stack: " + src + "\ndes stack: " + des +"\naux stack: " + aux);
    }
}

```
> 代码中的日志型输出可以一律清除
