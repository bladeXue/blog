---
title: 最大相同前缀后缀问题
date: 2020-06-04 15:14:17
tags:
- 算法
- 数据结构
- 字符串
categories:
- [算法, 经典算法, 字符串]
---

# 经典字符串算法-最大相同前缀后缀问题

> 这个是学习KMP算法的前置问题，已经有几十年历史了
> 本质是个很经典的有限状态机
> 我看过很多关于这个问题的博客，要么是特别长根本看不懂，要么根本就是错的，所以我决定自己写一篇，中间解释部分有点长，喜欢直接看源码可以直接翻到源码那个节，算法比较难理解，但是实现代码就一点点，很短很巧妙
<!-- more -->
#### 问题描述

首先了解一个概念，有一个字符串ABCDE，其中从首字母A开始的子字符串，如AB或ABC，称为这个字符串的前缀，同样的以尾字母结束的子字符串，如CDE或DE，称后缀。其中，子字符串的长度len必须有0<len<整体长度，也就是说子字符串必须是个真子集，A是ABCDE的前缀，ABCD是ABCDE的前缀，但ABCDE不能作为其本身的子字符串

在了解完前后缀概念后，我们的问题来了：给定一个字符串S，找出其相同前缀后缀的最大长度

示例：有字符串ABCAB，其最大的相同前缀和后缀是AB，所以这个字符串的最大相同前缀后缀长度为2
<img src="/images/algorithm/kmp/ABCAB的共坠.png" title="ABCAB的共坠" alt="ABCAB的共坠" style="max-width:60%;margin:auto;" />
同时在此给出几个名词（我自己创的或者习惯称呼，为的是表达方便），一共三处：

1. 对于一个字符串ABCAB，如果其拥有相同的前缀后缀存在，那么称这个字符串为**共生串**，这其中拥有对应相同的后缀的前缀称**共生前缀**，对应的后缀称**共生后缀**，统称**共生缀**，简称共缀，上图中的ABCAB就是一个共生串，其中的AB则是这个共生串的最大共生缀，也是唯一共生缀
2. 对于一个字符串ABCD，它会拥有几个子串，也就是A，AB和ABC，它们连同ABCD呈现出一种成长性（如下图），在这里我们称A为AB的前驱字符串，AB为ABC的前驱字符串（注意前趋串本身也是一个前缀串）
<img src="/images/algorithm/kmp/字符串的成长性.png" title="字符串的成长性" alt="字符串的成长性" style="max-width:70%;margin:auto;" />
3. 我们都知道字符串本质是一个字符数组，那么对于字符串```S = "ABCD"```其实等同于```S = {'A','B','C','D'}```，所以S\[0\]=='A'，同时有一种切片描述，S\[0.\.2\]表示S\[0\]到S\[2\]之间的所有字符组成的串，也就是说S\[0.\.2\]=="AB"

#### 共生缀的对称性

观察这样一个共生串ABACABA，它有两个共生缀A和ABA，在这里可以看出，当一个共生串拥有一个以上的共生缀的时候，其内部就会展现出一种对称性，在此不必要深究其数学证明，只要在视觉上对其有一个概念即可

下面是ABACABA的示意图，其中的4个被涂红的A，展现出了很明显的对称性。之后我们会看到，这几个A在**实际意义**上，指代的是同一个字符：
<img src="/images/algorithm/kmp/ABACABA的4个A.png" title="ABACABA的4个A" alt="ABACABA的4个A" style="max-width:60%;margin:auto;" />

#### 问题分析

一开始看见这个问题，想到的方法自然是万能的暴力for循环啦，不多bb，还是拿ABACABA这个字符串开刀：

###### 1. 暴力for循环

基本流程如下：

1. 考虑共缀长度为1，那我们直接比较首尾字符就行了，也就是S\[0\]和S\[6\]，我们发现都是A，所以有共缀成立，为A，长度为1，如下所示：
<img src="/images/algorithm/kmp/for1.png" title="for1" alt="for1" style="max-width:60%;margin:auto;" />
2. 考虑是否有更长的共缀长度，于是我们将考量长度+1，开始考虑S\[0.\.2\]和S\[5.\.7\]，发现并不匹配，所以不存在长度为2的共缀，如下所示（黄色表示失败）：
<img src="/images/algorithm/kmp/for2.png" title="for2" alt="for2" style="max-width:60%;margin:auto;" />
3. 我们不甘心，只能继续查找更长的字符串，看是否有奇迹发生，于是在长度为3的共缀串中，发现匹配了，如下图所示：
<img src="/images/algorithm/kmp/for3.png" title="for3" alt="for3" style="max-width:60%;margin:auto;" />
4. 接下来继续尝试4和5和6，但是均为失败，所以最大共缀就是之前测到的ABA，长度为3，下面是完整的一览（3以后我涂色分层了，为了直观一点，黄色失败，红色成功）： 
<img src="/images/algorithm/kmp/for5.png" title="for5" alt="for5" style="max-width:80%;margin:auto;" />

示例代码如下，我用Java实现的，随便看看就行了：
```java
public class MaxPrefix {

    public static void main(String[] args) {

        String s = "abacaba";
        int len = s.length();

        for (int m = 1; m < len; m++) {
            for (int i = 0, j = len - m; i < m && j < len; i++, j++) {
                if (s.charAt(i) != s.charAt(j)) {
                    break;
                }
                if (i == m - 1) {
                    // 如果存在共缀则输出共缀长度
                    System.out.println(m);
                }
            }
        }
    }
}
// 最终输出
// 1
// 3
```
> 时间复杂度O(N^2)，效率不是很高，毕竟是暴力双重for循环

###### 2. 递推数组

上面的例子只是为了方便理解，其实由于效率低等原因，我们一般更愿意采用本节的方案，使用递归关系求解，这个算法很有趣，而且是KMP算法的核心。对比上面的只能算一个字符串，递推数组的方案不仅能求出我们的字符串本体的共缀，甚至能连同求出其子串的共缀

这里我们使用字符串ABACABAB作为示例，我们在这里建立一个max[]数组，数组元素代表当前长度下，字符串最长共缀，你们可以看下图感受一下：
<img src="/images/algorithm/kmp/next1.png" title="next1" alt="next1" style="max-width:60%;margin:auto;" />

在正式开始构建之前，观察这么一个有趣的现象，还是看我们上面的ABACABAB，但是我稍微涂了一点颜色，如下所示：
<img src="/images/algorithm/kmp/next2.png" title="next2" alt="next2" style="max-width:60%;margin:auto;" />
观察上图，我们可以发现，对于字符串ABACABAB，它是一个共生串，且共生缀长度为2（也就是满足大于1），那其实很清晰可以看到，它的前驱串ABACABA也是一个共生串且共生缀长为1，于是我们可以得到一个有趣的结论，也就是**共生缀长度超过1的共生串的前驱串也必然是一个共生串**，我称之为“有爸爸的前提是先有爷爷定律”，这个结论是递推数组的核心，也就是说，我们在max\[k]的数据受到max\[k-1]的影响，在考虑在某个位置（本例中为S\[7]=B）是否构成共缀的时候只要考虑其之前的字符串（前缀或前趋）是否是个共生串（本例中为S\[0.\.7]="ABACABA"，其为共生串且共缀为ABA，ABA本身也是一个共生串，共缀为A）即可，然后我们只要校验尾位即可，不需要像暴力for里跟二胡卵子一样每一位都单独计算了。借由这个性质，我们使用递推法构造数组成为可能

基于以上事实，那其实我们构建递推数组max[]的核心流程也已经很明确了，示例依旧是待检字符串```S = "ABACABAB""```，有以下步骤：

1. 如果位置S\[k]的前趋串S\[0.\.k]是一个共生串，且共缀长度为j（也就是max\[k-1]=j），那么直接比较S\[j]和S\[k]，若匹配，则j+1就是max\[k]的值，如示例字符串ABACABAB的S\[6]位置，按照我们的“**有爸爸的前提是先有爷爷定律**”，其前趋串ABACAB拥有共缀AB，且S\[j]=S\[2]=A和S\[k]=S\[6]=A匹配，所以max\[6]顺理成章喜加一，有max\[6]=max\[5]+1=2+1=3，如下图所示：
<img src="/images/algorithm/kmp/next3.png" title="next3" alt="next3" style="max-width:65%;margin:auto;" />
2. 如果不匹配，说明max\[k]<=max\[k-1]=j，如示例字符串ABACABAB的S\[7]位置，有S\[3]=C!=S\[7]=B，按照**有爸爸的前提是先有爷爷定律**，我们继续考虑前趋串来找这个“爷爷”，幸运的是ABAC尽管和ABAB不匹配，但是ABA本身也是一个共生串，其共缀为A，在第二次迭代后，S\[0.\.2]=AB和S\[6.\.8]=AB匹配，所以max\[7]=max\[2]+1=1+1=2，如下图所示：
<img src="/images/algorithm/kmp/next4.png" title="next4" alt="next4" style="max-width:70%;margin:auto;" />
3. 如果运气不太好，无论怎么迭代前趋串，以及前趋串的前趋串，一直找不到这个“爷爷”，那没办法了，没“爷爷”自然没“爸爸”，那也自然没有“儿子”了，按照**有爸爸的前提是先有爷爷定律**，前趋串不是共生串，且本身单字符匹配也不成立，max\[k]就只能置零，如S\[3]位置，找不到“爷爷”，本身也不匹配（指S\[0]!=S\[3]），最后只能置零，也有稍微幸运一点的，如S\[4]，虽然找不到“爷爷”，但是本身单字符匹配成立了（指S\[0]!=S\[3]=A），所以max\[4]=0+1=1，如下图所示（黄色失败红色成功）：
<img src="/images/algorithm/kmp/next5.png" title="next5" alt="next5" style="max-width:80%;margin:auto;" />

bb了这么久，估计不少人看得也云里雾里的，对于理解这种含递推过程的问题来说很正常，多看几遍就有感觉了，自然而然就看懂了，这里直接给出相关的Java代码：
```java
public class Kmp {
    
    // 其实next[]数组在KMP算法中实际应用时会有一点点小变化，但是这里是为了计算共缀，依旧采用next的命名
    private static int[] getNext(String pat) {

        int len = pat.length();
        if (len < 2) return new int[]{0};   // 字符串长度0或1直接返回
        int[] next = new int[len];
        next[0] = 0;

        int i = 0;  // 表示当前最大共缀长度的候选值
        int j = 1;  // 从第二位开始遍历

        while (j < len) {

            if (pat.charAt(i) == pat.charAt(j)) {
                next[j++] = ++i;    // 如果第j位直接匹配，则最大值顺延。且j进入下一位
            } else if (i == 0) {
                next[j++] = 0;      // 找不到“爷爷”，本身又不匹配，那就只能置0
            } else {
                i = next[i - 1];    // 递推核心，寻找下一层的最大前缀
            }
        }
        return next;
    }

    public static void main(String[] args) {

        System.out.println(Arrays.toString(getNext("ABACABAB")));
        // 输出结果
        // [0, 0, 1, 0, 1, 2, 3, 2]
        // 对应有txt <-> max[]
        // A B A C A B A B
        // 0 0 1 0 1 2 3 2
    }
}
```
看完了代码，我们在针对字符串```S = "ABACABAB""```来就进行一次完整的计算，建议结合上面的源码一起看：

1. S\[0]=A，完整字串A，长度1,不存在前后缀和匹配问题，直接置0，最终结果max\[0]=0
<img src="/images/algorithm/kmp/full1.png" title="full1" alt="full1" style="max-width:60%;margin:auto;" />
2. S\[1]=B，完整字串AB，本体单字符S\[0]=A!=S\[1]=B，且没有前趋（因为max\[0]=0，不是一个合法的共生串）给它找“爷爷”，最终置0，最终结果max\[1]=0
<img src="/images/algorithm/kmp/full2.png" title="full2" alt="full2" style="max-width:60%;margin:auto;" />
3. S\[2]=A，完整字串ABA，依旧没有前趋串给它“找爷爷”，所以直接比较本体的S\[2]，本体单字符S\[0]=A==S\[2]=A，匹配成立，最终结果为max\[2]=max\[1]+1=0+1=1
<img src="/images/algorithm/kmp/full3.png" title="full3" alt="full3" style="max-width:60%;margin:auto;" />
4. S\[3]=C，完整字串ABAC，有前趋串ABA，按照我们顺延的做法，比较AB和AC，失败了，同时迭代ABA的共缀A无果，所以最终悲惨置0，最终结果max\[3]=max\[0]+0=0+0=0
<img src="/images/algorithm/kmp/full4.png" title="full4" alt="full4" style="max-width:60%;margin:auto;" />
5. S\[4]=A，完整字串ABACA，无前趋共生串，但本体单字符S\[0]=A==S\[4]=A，匹配成立，所以最终结果max\[4]=max\[0]+1=0+1=1
<img src="/images/algorithm/kmp/full5.png" title="full5" alt="full5" style="max-width:60%;margin:auto;" />
6. S\[5]=B，完整字串ABACAB，有前趋共生串ABACA且共生缀A，匹配单体S\[1]=B==S\[5]=B，匹配成立，结果顺延，最终结果max\[5]=max\[4]+1=1+1=2
<img src="/images/algorithm/kmp/full6.png" title="full6" alt="full6" style="max-width:60%;margin:auto;" />
7. S\[6]=A，完整字串ABACABA，有前趋共生串ABACAB且共生缀AB，匹配单体S\[2]=A==S\[6]=A，匹配成立，结果顺延，最终结果max\[6]=max\[5]+1=2+1=3
<img src="/images/algorithm/kmp/full7.png" title="full7" alt="full7" style="max-width:60%;margin:auto;" />
8. S\[7]=B，完整字串ABACABAB，有前趋共生串ABACABA且共生缀ABA，但是匹配单体S\[3]=C!=S\[7]=B失败，所以按照**有爸爸的前提是先有爷爷定律/共生缀长度超过1的共生串的前驱串也必然是一个共生串定律**开始“找爷爷（有效共缀）”，其前趋缀ABACABA的共生缀本身也是共缀为A的共生缀，最终S\[0.\.2]=A+B匹配S\[6.\.8]=A+B，最终结果max\[7]=max\[2]+1=1+1=2
<img src="/images/algorithm/kmp/full8.png" title="full8" alt="full8" style="max-width:60%;margin:auto;" />
> 注意，在这里，我额外用绿色标出了4个A的位置，可以返回前面，看一看我说的对称性，你就知道，这个图到底什么意思了
> 同时观察S\[7]=B指出的箭头，这个其实代表了算法实现中的一个目的，找到共生缀，其实就是当前位的S\[k]的字符X是否在之前的共生串中出现过，所谓的“找爷爷”，其实就是在借由递推不同层级的前缀来找这个字符X

最终得到的max[]数组为：
<img src="/images/algorithm/kmp/full10.png" title="full9" alt="full9" style="max-width:60%;margin:auto;" />

#### 总结

到此为止，就完整地完成了字符串的最大相同前后缀问题，我们求出来的max[]数组其实是KMP算法中next[]数组的基础，可以说理解了最大相同前后缀问题就是理解了KMP算法（这个算法是出了名的难理解）。这个问题的本质是是一个关于有限状态自动机的算法，但是在这里体现得不明显，在另一篇关于KMP算法的有限自动机问题的博文里，我会详细表述一下。本文的问题解答，因为涉及递推，一开始不是很好理解，没什么捷径，自己多看代码，多画图，来几遍有感觉了，自然就会理解的。如果你发现了bug，或者有自己的想法和优化方案，请给博主发邮件，或者在评论区戳我，感谢阅读(′▽`〃)

#### 参考

[编程之法 面试和算法心得](https://www.ptpress.com.cn/shopping/buy?bookId=d7ee2bb8-dcb8-4029-8156-0b65d962f18a)
