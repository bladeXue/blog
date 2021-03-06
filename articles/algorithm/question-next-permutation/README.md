# “下一个全排列”问题

> 全排列问题和字典序算法的融合问题
> 帮助理解序理论的重要材料
<!-- more -->
#### 问题描述

排列问题是组合数学中的基本问题之一，给定数组```{1,2,3}```，对其中的元素进行重新排列，会有6种不同的序列，分别是```{1,2,3}```，```{1,3,2}```，```{2,1,3}```，```{2,3,1}```，```{3,1,2}```和```{3,2,1}```

将这6个排列按照数字从小到大排个前后，有下表：

|序号|排列|
|-|-|
|1|{1,2,3}|
|2|{1,3,2}|
|3|{2,1,3}|
|4|{2,3,1}|
|5|{3,1,2}|
|6|{3,2,1}|

仔细观察一下，这其中其实是一种类似英语词典中，单词的排序，也就是a-开头的单词在b-开头单词的前面，ab-开头的单词在am-开头的单词的前面，这种排序法则就是**字典序**，详细定义如下：

> 给定两个偏序集A和B，(a,b)和(a′,b′)属于笛卡尔积A×B，则字典序定义为：(a,b)≤(a′,b′)，当且仅当a<a′或(a=a′且b≤b′)
> 结果是偏序（如果A和B是全序, 那么结果也是全序）

这里的[偏序关系](https://zh.wikipedia.org/wiki/偏序关系)是离散数学的序理论中的概念，有些生疏的可以把《离散数学》的书翻出来看看

到这里我们的问题就可以提出来了：从当前排列生成字典序刚好比它大的下一个排列

#### 问题分析

在这里我们先来观察一种现象，我称之为“地板天花板”现象，现在给定```{1,2,3,4}```四个数字，可以排列出P(4,4)=24个四位数，其中有：

- 天花板：也就是最大的数字排列4321，也称**降序列**（从第一个数字到最后一个数字都在减少）
- 地板：也就是最小的数字序列1234，也称**升序列**（从第一个数字到最后一个数字都在变大）

观察上面的两个数，可以很容易看出，天花板和地板是正好反过来的，我们这个时候再来看另一个例子，这个例子里，我们使用```{1,3,4,5}```四个数字，并且固定首位为4，那我们可以得到天花板和地板：

- 天花板：4531，531是一个3位降序
- 地板：4135，135是一个3位升序

现在我们的重点来了，我们都知道一层楼的天花板肯定比地板高，就像上面的531比135大一样，我称之为做“同1层的天花板比地板高”原理，在这之外还有一个“5楼的地板比4楼的天花板高”原理。还是上面的两个数字4531和4135，我们把4531看作“4楼的天花板531”，4135看作“4楼的地板135”，如果我们把首位的4换成5，那就有“4楼的地板135”变成“5楼的地板134”，也就是5134，这个5134其实就是4531的“下一个字典序排列”

到此为止，我们的算法流程就算是出来了，有4步：

1. 找到排列中最右侧的一个升序，记录其首地址i（找到这层楼的地板），并记录x=a\[i]
2. 找到排列中i右侧最后一个比a\[i]大的位置j（找到下上层楼的层数），并记录y=a\[j]
3. 交换x和y
4. 将i之后的尾部整个反转

拿21543举个例子：

1. 从右到左找一个升序15，记录x=1
2. 在1右侧找到最后一个比1大的数字，也就是y=3
3. 交换1和3，21543->23541
4. 反转541，获得23145
> 自此23145就是21543的下一个“字典序排列”

#### 算法实现

这里给出我们的Java实现，其实C++的STL库里的next_permutation()函数也是类似的思路。这里是完整的代码：

```java
import java.util.Arrays;

public class GetPermutation {

    private static int count = 0;
    private static int[] nums = {0, 1, 2, 3, 4, 5, 6, 7};

    private static void swap(int a, int b) {
        if (a < nums.length && b < nums.length) {
            int tmp = nums[a];
            nums[a] = nums[b];
            nums[b] = tmp;
        }
    }

    // nums[from] <-> nums[to]
    // to < len
    private static void reserve(int from, int to) {
        int offset = 0;
        while (offset < (to - from + 1) / 2) {
            swap(from + offset, to - offset);
            offset++;
        }
    }

    // boolean -> 是否找到了新的排列
    private static boolean getNextPermutation() {

        // 1. 找到第一个升序
        int len = nums.length;
        int i = len - 2;

        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
            if (i < 0)
                // 小于零说明已经找到全部排列
                return false;
        }
        // 2. 在右侧的降序中找最接近i的那个大数
        int j = len - 1;
        while (i < j && nums[i] >= nums[j]) {
            j--;
        }
        // 3. 交换升序数和最小大数
        swap(i, j);
        // 4.反转尾部字符串
        reserve(i + 1, len - 1);
        return true;
    }

    public static void main(String[] args) {

        System.out.println("the " + ++count + "th permutation: " + Arrays.toString(nums));

        int count2 = 20;
        while (getNextPermutation() && count2-- > 0) {
            System.out.println("the " + ++count + "th permutation: " + Arrays.toString(nums));
        }
    }
}
```
> 复杂度为O(n!)，和使用递归法求全排列是一样的

#### 总结

好好体会其中的序列的理论

#### 参考

[编程之法 面试和算法心得](https://www.ptpress.com.cn/shopping/buy?bookId=d7ee2bb8-dcb8-4029-8156-0b65d962f18a)
