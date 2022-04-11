# 弹性布局

## 概念

弹性布局是目前最成熟，支持最好的，开发体验最友好的布局方案。传统的**定位布局**和**浮动布局**需要编写冗长的栅格系统来达到布局需求，但是2009年，W3C提出弹性布局，很多旧的样式，用弹性布局代码几行就写完了。

弹性布局可以轻松实现垂直居中。

## 浏览器支持

2009年的时候，W3C就提出了**弹性布局**这个概念，但是当时不叫这个名字，当时使用的样式是`display: box`。2011年之后，谷歌一众浏览器厂商采用`display: flexbox`的兼容写法来实现弹性布局，2016年最终由W3C敲定为`display: flex`的Flex布局规范标准。所以弹性布局到今天经历了十多年，已经非常成熟了，且浏览器支持非常好。[CAN I USE](https://caniuse.com/?search=flex)的结果如下：

![caniuse_flex](./images/caniuse_flex.png "caniuse_flex")

兼容性非常棒，基本全是绿的，也就当考虑IE10的时候要加个前缀。如果你不考虑兼容蛋疼的IE8，那么光速使用Flex改写布局系统是个很不错的方案。

> Grid布局的效果比Flex更强，但是Grid的浏览器支持目前还差点意思。

## 弹性容器和弹性盒子

弹性布局是CSS3中的一种布局方式，和传统的布局方式不同的是，弹性布局不再指定一个元素具体的尺寸，而是描述这个元素该如何去填充空间。这样做会把布局变得简单，我们只需要在样式中提出布局的需求，然后由浏览器计算具体的数值。

一个Flex布局由**弹性容器**和**弹性盒子**构成，将一个父盒子指定成弹性容器后，其子项自动变成弹性盒子，随后会有：

1. 弹性容器默认宽度100%。
2. 横向布局的块级盒子不再占用单行。
3. 弹性盒子的尺寸可以随着容器大小而伸展或压缩，盒子原本的`float`，`clear`和`vertical-align`将会失效，相关效果由弹性容器接管。
4. 可以控制多个弹性盒子的排列顺序，对齐等等。

## 弹性轴

弹性容器默认存在两根轴：主轴和交叉轴。横向布局中，主轴默认是水平轴，弹性元素按该轴排列。

![flex_desc](./images/flex_desc.png "flex_desc")

## 属性

设置元素的`display: flex`生成**块级Flex容器**，设置`display: inline-flex`可以生成**内联Flex容器**。一个典型的弹性布局结构如下：

![display_html](./images/display_html.png "display_html")

```HTML
<!-- HTML -->
<div class="flex-container">
    <div class="flex-item box">A</div>
    <div class="flex-item box">B</div>
    <div class="flex-item box">C</div>
</div>
<style>
    .flex-container {
        /* 设置弹性容器 */
        display: flex;
    }
    .flex-item {
        /* 弹性盒子样式 */
        flex: 1;
    }
    .box {
        /* 让盒子长好看点 */
        margin: 10px;
        height: 200px;
        background-color: lightcoral;
        text-align: center;
        color: white;
        font-size: 8em;
        line-height: 200px;
    }
</style>
```

有6个属性可以设置在


## 案例






## 总结

## 参考

[Flexbox Froggy - 一个用来学CSS flexbox的游戏](https://flexboxfroggy.com/#zh-cn)
