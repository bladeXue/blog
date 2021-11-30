# 理解补码

基本上工科的在大一时都修过C语言，国内普遍用的的谭浩强的课本，开篇就讲了一大堆的原码反码，但都是流水账，基本上大家都学得迷迷糊糊的，跟着老师背了一堆“反补诀窍”，但始终没明白补码到底是个什么东西。

## 补码和整数减法

首先我们都知道计算机的核心是CPU，而且电路属性是建立在二进制代数上的，所以CPU只认识二进制，我们平时用的十进制和十六进制数，在执行层面也是转换成二进制后进行计算的。但是，这里面有一个问题，为了保证数字电路工程的纯粹，那就是CPU很大程度上，只会做整数加法，乘法则是通过一个标记数，多次调用加法得来的。

那减法怎么办？CPU实现减法的策略也很简单，想要减去某个数字A，那就加上A的相反数就行了。

我们这样定义一个相反数：

1. 对于数字A和数字B。
2. 如果存在![](https://latex.codecogs.com/gif.latex?\small&space;A&plus;B=0)成立，则称A和B互为相反数，记作![](https://latex.codecogs.com/gif.latex?\small&space;B=-A)，以上。

你可能会觉得这两者没有区别，但是对CPU来说，这是实现减法的关键。

## 位数溢出

假设我们拥有一个8位CPU，给定一个数字A，十进制表示为15，其8位二进制表示为00001111，又给定一个数字B，其8位二进制表示为11110001，A和B相加为9位二进制100000000，但是我们的CPU是8位的，所以第9位被进位丢弃，结果是00000000，把流程写下来：

1. 有![ ](https://latex.codecogs.com/gif.latex?\small&space;A=[00001111]_{8})和![ ](https://latex.codecogs.com/gif.latex?\small&space;B=[11110001]_{8})。
2. 等式![](https://latex.codecogs.com/gif.latex?\small&space;[00001111]_{8}&plus;[11110001]_{8}=[00000000]_{8})成立。
3. 根据相反数定义，A和B相加为零，互为相反数。

数字B其实就是A的补码，其十进制表示为-15，通过巧妙地运用进位溢出，就变相通过相反数来完成了一次减法，15-15=0是这样，通过补码就完成CPU的减法。

## 补码的求法

其实你只要观察一下![ ](https://latex.codecogs.com/gif.latex?\small&space;A=[00001111]_{8})和![ ](https://latex.codecogs.com/gif.latex?\small&space;B=[11110001]_{8})，其实很轻易就能看出来补码是怎么算的：为了构造加法完成后能触发满值溢出1个数，补码就是取反后加上一个溢出补位数字。

## 什么时候用补码

补码这个问题其实不需要我们思考，这个部分也不是由CPU完成的，CPU只认识二进制，获得输入电路后直接计算，所以CPU也不认识补码，补码过程是编译器确认并完成的，通常我们在源代码中会编写带有符号十进制数的可读性源码，而编译器（其实主要是汇编器）的工作就是确认这个数字是否需要翻译成对应的补码（比如正整数就是不需要的，而汇编器遇到一个负整数就会确认其补码），操作系统回头执行二进制文件时会直接把补码后的数字提交给CPU计算。

这里编写一个简单的C文件，命名为`foo.c`：

```C
#include <stdio.h>

int main()
{

    int fifteen = 15;
    int mfifteen = -15;
    printf("%d\n", fifteen + mfifteen);
    return 0;
}
```

通过GCC命令`gcc -c -Wa,-L foo.c; objdump -d foo.o > dump.txt`我们可以提取其二进制文件：

```log
foo.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <main>:
   0:	f3 0f 1e fa          	endbr64 
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	48 83 ec 10          	sub    $0x10,%rsp
   c:	c7 45 f8 0f 00 00 00 	movl   $0xf,-0x8(%rbp)              ;; fifteen = 15
  13:	c7 45 fc f1 ff ff ff 	movl   $0xfffffff1,-0x4(%rbp)       ;; mfifteen = -15
  1a:	8b 55 f8             	mov    -0x8(%rbp),%edx
  1d:	8b 45 fc             	mov    -0x4(%rbp),%eax
  20:	01 d0                	add    %edx,%eax
  22:	89 c6                	mov    %eax,%esi
  24:	48 8d 3d 00 00 00 00 	lea    0x0(%rip),%rdi        # 2b <main+0x2b>
  2b:	b8 00 00 00 00       	mov    $0x0,%eax
  30:	e8 00 00 00 00       	callq  35 <main+0x35>
  35:	b8 00 00 00 00       	mov    $0x0,%eax
  3a:	c9                   	leaveq 
  3b:	c3                   	retq   
```

观察`<main>`的c行和13行就可以看到我们的数字15和-15已经被转换成了对应的编码（我的处理器是64位的，所以-15的补码很长），当操作系统执行该文件时，可以直接将其提交给CPU。

## 总结

补码是通过合理溢出来让计算机实现减法操作，整数减法和浮点数减法略有区别，但是原理是相似的。
