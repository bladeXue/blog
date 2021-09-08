---
title: 图的搜索算法
date: 2020-09-04 14:10:24
tags:
- 算法
- 数据结构
- 图论
categories:
- [算法, 数据结构, 图论专栏]
---

# 图的深度优先搜索和广度优先搜索

> 搜索问题是图的众多算法中最核心最重要的，几乎所有图论算法都依赖图的搜索
> 图的搜索算法是判定连通性的重要工具
<!-- more -->
> 本文是系列文章的其中一篇，关于前后文请参见[图论专栏-导读](https://bladexue.github.io/2020/08/25/algorithm/data-structure/graph-theory-guide/)
#### 图的搜索问题

图的搜索问题是图论的**最基本问题**，如果不能有效访问数据，那么数据结构将毫无意义，所谓的算法也会成为空谈，所以必须有一种有效的算法来搜索图所持有的数据。给定一个图，按照某种搜索方法，**沿着图中的边对图中的所有顶点访问一次且仅访问一次**，称为图的**遍历**

图的搜索算法主要有两种：**深度优先搜索**（Depth-First-Search，简称**DFS**）和**广度优先搜索**（Breadth-First-Search，简称**BFS**）

无论是深度优先搜索还是广度优先搜索，几乎所有的图论搜索算法都属于一种叫做**优先级搜索**的抽象策略。在[图的存储结构及封装](https://bladexue.github.io/2020/08/19/algorithm/data-structure/graph-theory/graph-theory-storage-structure/)一文中，我们通过检查当前顶点的所有连通边（也就是```adj()```方法），来获取各类性质，在搜索算法中，我们的想法是沿着某顶点的连通边，过渡到下一个顶点，从而达到搜索整个图的目的。对BFS来说，其优先考虑最早发现的顶点（先扫描离起点近的），而DFS则关注最后发现的顶点

> 注意树其实是一种特殊的图，所以图的搜索和树的搜索很相似，DFS类似树的先序遍历，BFS类似树的中序遍历

> 从辅助结构的选型上讲，DFS和BFS其实是记录型结构（栈）和缓冲型结构（队列）的不同实现

#### 深度优先搜索

深度优先是一种回溯性算法，其本质结构是栈构成的记录型结构，常规实现是通过递归，在给出代码之前，我们可以看一个小故事

###### 迷宫问题

迷宫问题是一个希腊神话的古老遗产，讲的是米诺斯国王为了囚禁儿子，一个半人半牛怪物的弥诺陶洛斯所建造的一座无法逃出的监牢。假设把你丢进了迷宫，那么摆在你面前只有两个下场，被迷宫困住，去见马克思，或者寻找一种方式，逃出生天。最经典的走迷宫方法是“绳子策略”：

1. 准备一根绳子，绳子的一端放在你的起点，另一端抓在你的手里
2. 准备一支粉笔，走过的路都做上标记
3. 遇到岔路时，挑选一个没有标记的路走进去
4. 如果继续遇到岔路，重复3；如果遇到死胡同，则顺着绳子回到上一个岔路，重复3
5. 如果返回的岔路口的所有路都做过了标记（全是死胡同），则顺着绳子继续回到上一个岔路

在这个策略里，绳子保证了遇到死胡同时可以找到回去的路，而标记保证了你不会重复进去一条已经走过的死胡同，于是在你不断地尝试各个路径，并在失败后使用绳子**回溯**的过程中，你尽可能尝试了尽可能多的路径，并最终**找到出口**逃出生天，或者尝试了**所有路径**，发现没有出口（太惨了）。

###### 深度优先搜索算法

到此为止，深度优先遍历的核心策略已经出来了，为了实现DFS，我们需要：

1. 一根绳子：一个记录型结构，这个FIFO很显然就是栈结构
2. 一支粉笔：一张表（数组或者散列），用来标记每条边是否已经访问。我们走迷宫时最担心的不是找不到出口，而是绕圈圈，走重复的路径，搜索图时一样，就怕加入了回路变成出不去的死循环，“粉笔”就是用来做这个的关键机构
3. 一点耐心：每次都尝试走尽可能远的路径，直到找到出口，或者碰壁回溯

因为我们采用递归结构来实现DFS，递归算法天然持有一个[栈](https://zh.wikipedia.org/wiki/调用栈)（函数调用和返回的机制和绳子回溯的作用类似），所以我们只需要一个**marked\[]数组**来标记，下来来看一个完整的例子：

1. 我们建立了一个简单的迷宫，我们将其连通模型，抽象成一个6个顶点和8条边的的无向图

<img src="/images/algorithm/map/search/dfs.png" title="dfs" alt="dfs" style="max-width:60%;margin:auto;" />

2. 我们的任务是从```顶点0```出发，使用DFS访问所有的顶点

<img src="/images/algorithm/map/search/dfs1.png" title="dfs1" alt="dfs1" style="max-width:30%;margin:auto;" />

3. 从```顶点0```出发，未访问边3条，通过```(0,2)```访问```顶点2```，访问过的顶点和边被我标记了赭红色（邻接点的访问是随机的）

<img src="/images/algorithm/map/search/dfs2.png" title="dfs2" alt="dfs2" style="max-width:30%;margin:auto;" />

4. 从```顶点2```出发，未访问边3条，通过```(1,2)```访问```顶点1```

<img src="/images/algorithm/map/search/dfs3.png" title="dfs3" alt="dfs3" style="max-width:30%;margin:auto;" />

5. 从```顶点1```出发，未访问边1条，通过```(0,1)```访问```顶点0```

<img src="/images/algorithm/map/search/dfs4.png" title="dfs4" alt="dfs4" style="max-width:30%;margin:auto;" />

> 此时发现```顶点0```已被标记，且```顶点1```已无可访问边，回退到```顶点2```

6. 从```顶点2```出发，未访问边2条，通过```(2,3)```访问```顶点3```

<img src="/images/algorithm/map/search/dfs5.png" title="dfs5" alt="dfs5" style="max-width:30%;margin:auto;" />

7. 从```顶点3```出发，未访问边2条，通过```(3,5)```访问```顶点5```

<img src="/images/algorithm/map/search/dfs6.png" title="dfs6" alt="dfs6" style="max-width:30%;margin:auto;" />

8. 从```顶点5```出发，未访问边1条，通过```(0,5)```访问```顶点0```

<img src="/images/algorithm/map/search/dfs7.png" title="dfs7" alt="dfs7" style="max-width:30%;margin:auto;" />

> 此时发现```顶点0```已被标记，且```顶点5```已无可访问边，回退到```顶点3```

9. 从```顶点3```出发，未访问边1条，通过```(3,4)```访问```顶点4```

<img src="/images/algorithm/map/search/dfs8.png" title="dfs8" alt="dfs8" style="max-width:30%;margin:auto;" />

> 所有顶点被访问，遍历结束

###### 生成树和生成森林

在DFS的过程中，我们会得到一棵遍历树，称为**深度优先生成树**（希望你还记得生成树的定义），图的DFS遍历树的先序遍历序列和其DFS序列是一致的，本例中的DFS生成树如下，它的遍历序列是```[0,2,1,3,5,4]```，和图的DFS序列一致：

<img src="/images/algorithm/map/search/dfs_tree.png" title="dfs_tree" alt="dfs_tree" style="max-width:60%;margin:auto;" />

值得一提的是，深度遍历生成树不是唯一的，其受存储结构的影响（邻接矩阵的生成树是唯一的，但邻接表不是，因为邻接表的邻接点无序），下面是本例的另一种DFS生成树：

<img src="/images/algorithm/map/search/dfs_tree2.png" title="dfs_tree2" alt="dfs_tree2" style="max-width:60%;margin:auto;" />
 
> 这里看到了经典的DFS轨迹图形，也就是所谓的“一棍子捅到底”，可以清晰看出，只要条件合适，DFS算法会尽可能深入地尝试一条路径

###### 在非连通图中的例子

上面的例子是一个无向的连通图，如果遇到非连通图，其实也是一样的，把它的几个连通分量抓出来，看作一个独立的连通图，使用DFS输出后，获得一个生成森林：

<img src="/images/algorithm/map/search/dfs_tree3.png" title="dfs_tree3" alt="dfs_tree3" style="max-width:95%;margin:auto;" />

###### 在有向图中的例子

有向图的DFS和无向图的DFS没有区别，只是有向图更容易遇到“死胡同”（因为强连通性可没那么好满足），从而很容易遍历到一半断片了，完了最后是一个生成森林。示例如下：

<img src="/images/algorithm/map/search/dfs_tree4.png" title="dfs_tree4" alt="dfs_tree4" style="max-width:70%;margin:auto;" />

> DFS本质是一样的，没有区别

###### 代码实现

代码已经上传[graph-algorithm-kit](https://github.com/bladeXue/graph-algorithm-kit/tree/master/code/graph-algorithm-kit)，用的存储结构的那套代码，方便和上一篇博客联系（其实是作者偷懒），可以配合本节阅读，为了节约篇幅，本篇只贴出核心部分

按照我们在[图结构的封装](https://bladexue.github.io/2020/08/19/algorithm/data-structure/graph-theory/graph-theory-storage-structure/#%E5%9B%BE%E7%9A%84%E5%B0%81%E8%A3%85%E5%92%8C%E5%AE%9E%E7%8E%B0)一节中的做法，依旧是采用```Graph```+```ListGraph```的分离式设计，应用代码都放在工具类```Graphs```里。这里是```Graphs```中关于DFS的两个主要方法：**深度优先搜索DepthFirstSearch**和**深度优先遍历DepthFirstTraverse**，主体代码如下：

```java
public abstract class Graphs {

    // 判定通路src->tar是否存在，可达则返回true
    public static boolean depthFirstSearch(Graph graph, Integer src, Integer tar) {
        
        // 判断顶点越界
        validateVertex(src,graph);
        validateVertex(tar,graph);

        // DFS
        List<Integer> marked = new ArrayList<>();
        dfs(graph,marked,src);
        return marked.contains(tar);
    }

    public static List<Integer[]> depthFirstTraverse(Graph graph, Integer src) {
        
        // 判断顶点越界
        validateVertex(src, graph);
        // 如果起点src为空，默认为顶点0出发
        int first = Objects.requireNonNullElse(src, 0);

        // 结果集（我们的结果很有可能是一个生成森林，所以使用二维表）
        List<Integer[]> results = new ArrayList<>();
        // 设置标记集
        List<Integer> marked = new ArrayList<>();

        // 优先访问起点，再访问其它顶点
        for (int i = first; i < first + graph.V(); i++) {

            int n = i % graph.V();
            if (!marked.contains(n)) {

                int boundary = marked.size();
                dfs(graph, marked, n);

                Integer[] buf = new Integer[marked.size() - boundary];
                marked.subList(boundary, marked.size()).toArray(buf);

                // 每次都只将新加入的结点写入数组，boundary就是标记新顶点用的
                results.add(buf);
            }
        }
        // 返回结果
        return results;
    }

    // 递归函数
    private static void dfs(Graph graph, List<Integer> marked, Integer v) {

        // 标记顶点
        marked.add(v);
        // 递归访问未标记顶点
        for (Integer i : graph.adj(v))
            if (!marked.contains(i))
                dfs(graph, marked, i);
    }

    // 判定顶点合法性的工具函数
    public static void validateVertex(int v, Graph graph) {
        if (v < 0 || v >= graph.V()) {
            throw new IllegalArgumentException("vertex " + v + " is not between 0 and " + (graph.V() - 1));
        }
    }
}
```

测试用例1，对一个无向图进行遍历和搜索：

```java
public class TestSearch {

    @Test
    public void testGraphDFS() {

        // 构造无向图
        Graph graph = new ListGraph(6);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(0, 5);
        graph.addEdge(2, 3);
        graph.addEdge(2, 4);
        graph.addEdge(4, 3);
        graph.addEdge(3, 5);
        graph.addEdge(1, 2);

        // 从顶点0出发
        List<Integer[]> res = Graphs.depthFirstTraverse(graph, 0);
        System.out.println("the forest from 0: ");
        for (Integer[] is : res) {
            System.out.println(Arrays.toString(is));
        }
        // 从顶点4出发
        List<Integer[]> res1 = Graphs.depthFirstTraverse(graph, 4);
        System.out.println("the forest from 4: ");
        for (Integer[] is : res1) {
            System.out.println(Arrays.toString(is));
        }
        // 验证可达路径<1,5>
        System.out.println("the path 1->5: " + Graphs.depthFirstSearch(graph, 1, 5));
        // 验证可达路径<2,4>
        System.out.println("the path 2->4: " + Graphs.depthFirstSearch(graph, 2, 4));
    }
}
```

> 输出结果：
> the forest from 0: 
> \[0, 1, 2, 3, 4, 5]
> the forest from 4: 
> \[4, 2, 0, 1, 5, 3]
> the path 1->5: true
> the path 2->4: true

这里用的图其实就是上文的迷宫，可以看到从不同顶点出发， 会有不同的结果，但是都获得了一棵生成树，而且我们的迷宫是一个连通图，无论是```1->5```还是```2->4```都是可达的：

<img src="/images/algorithm/map/search/dfs_code.png" title="dfs_code" alt="dfs_code" style="max-width:99%;margin:auto;" />

测试用例2，对一个非连通的有向图进行遍历和搜索：

```java
public class TestSearch {

    @Test
    public void testDigraphDFS() {

        // 构造有向图
        Digraph digraph = new ListDigraph(8);
        digraph.addEdge(4, 0);
        digraph.addEdge(1, 2);
        digraph.addEdge(1, 5);
        digraph.addEdge(5, 2);
        digraph.addEdge(2, 6);
        digraph.addEdge(3, 6);
        digraph.addEdge(3, 7);

        // 从顶点0出发
        List<Integer[]> res = Graphs.depthFirstTraverse(digraph, 0);
        System.out.println("the forest from 0: ");
        for (Integer[] is : res) {
            System.out.println(Arrays.toString(is));
        }
        // 从顶点1出发
        List<Integer[]> res1 = Graphs.depthFirstTraverse(digraph, 1);
        System.out.println("the forest from 1: ");
        for (Integer[] is : res1) {
            System.out.println(Arrays.toString(is));
        }
        // 验证可达路径<1,6>
        System.out.println("the path 1->6: " + Graphs.depthFirstSearch(digraph, 1, 6));
        // 验证可达路径<1,7>
        System.out.println("the path 1->7: " + Graphs.depthFirstSearch(digraph, 1, 7));
    }
}
```

> 输出结果：
> the forest from 0: 
> \[0]
> \[1, 2, 6, 5]
> \[3, 7]
> \[4]
> the forest from 1: 
> \[1, 2, 6, 5]
> \[3, 7]
> \[4, 0]
> the path 1->6: true
> the path 1->7: false

本测试的用例是一个不连通的有向图，有向图的遍历一般比无向图麻烦，因为它的连通条件比无向图苛刻，更容易产生“死胡同”，所以有向图一般都是生成森林，且起点不同对这个森林是有影响的：

<img src="/images/algorithm/map/search/dfs_code2.png" title="dfs_code2" alt="dfs_code2" style="max-width:99%;margin:auto;" />

> 以顶点0为起点和以顶点1为起点，是有区别的，这和我们的算法实现，以及存储结构有关

###### DFS的时空分析

在空间上，DFS虽然只创建了一个标记集，同时自己是一个递归算法，持有一个调用栈，所以空间复杂度为```O(|V|)```

在时间上，DFS算法的复杂度和其选用的存储结构有关，如果使用的是邻接矩阵，每次调用```adj()```方法时，需要访问```|V|```个顶点，所以整体空间复杂度为```O(|V|**2)```，如果是邻接表存储的图，每次调用```adj()```方法时，需要访问```|E|```个顶点，访问所有顶点的时间为```O(|V|)```，所以邻接表的整体时间消耗为```O(|V|+|E|)```

#### 广度优先搜索

看完DFS的例子，相比对图的搜索已经有了一个很好的概念，再来讲BFS（Breadth First Search，广度优先搜索）就很容易了。前文提过，DFS和BFS都采用的优先级策略，DFS关注的是**最后被发现的顶点**，而BFS则是考虑**最早被发现的顶点**

###### 广度优先搜索算法

BFS类似树的层次遍历模型，对于起点v，我们会先依次访问v的“儿子们”（也就是v的邻接点），再依次访问“孙子们”（v的邻接点的邻接点），这种分层次的查找过程，就是**广度优先**。与DFS展现出的“探索性”不一样，BFS更多的是一种**扩散性**（或者说**侵蚀性**），我们一起来看个例子：

1. 我们依旧构造一个无向图，我们这次从```顶点1```出发，第1层次为```1```：

<img src="/images/algorithm/map/search/bfs.png" title="bfs" alt="bfs" style="max-width:40%;margin:auto;" />

2. 第2层次为```0,5```：

<img src="/images/algorithm/map/search/bfs1.png" title="bfs1" alt="bfs1" style="max-width:40%;margin:auto;" />

3. 第3层次为```2,4,6```：

<img src="/images/algorithm/map/search/bfs2.png" title="bfs2" alt="bfs2" style="max-width:40%;margin:auto;" />

4. 第4层次为```3,7```：

<img src="/images/algorithm/map/search/bfs3.png" title="bfs3" alt="bfs3" style="max-width:40%;margin:auto;" />

5. 和DFS一样，在BFS中，我们最终可以获得一棵BFS生成树：

<img src="/images/algorithm/map/search/bfs_tree.png" title="bfs_tree" alt="bfs_tree" style="max-width:70%;margin:auto;" />

> BFS生成树的层次遍历和BFS序列是一致的

###### 代码实现

和DFS的代码类似，使用队列作为缓冲结构（这里的缓冲场景指，记忆正在访问的顶点的下一层顶点），而不是栈，所以这里没有递归结构，也没有回退，只有迭代队列，直到遍历整张表

```java
public abstract class Graphs {

    // 广度优先搜索
    public static boolean breadthFirstSearch(Graph graph, Integer src, Integer tar) {

        // 判断顶点越界
        validateVertex(src, graph);
        validateVertex(tar, graph);

        // BFS
        List<Integer> marked = new ArrayList<>();
        bfs(graph, marked, src);
        return marked.contains(tar);
    }

    // 广度优先遍历
    public static List<Integer[]> breadthFirstTraverse(Graph graph, Integer src) {

        // 判断顶点越界
        validateVertex(src,graph);
        // 设置起点
        int first = Objects.requireNonNullElse(src, 0);

        // 结果集
        List<Integer[]> results = new ArrayList<>();
        // 标记集        
        List<Integer> marked=new ArrayList<>(graph.V());

        // 优先访问起点，再访问其它顶点
        for (int i = first; i < first + graph.V(); i++) {

            int n = i % graph.V();
            if (!marked.contains(n)) {

                int boundary = marked.size();
                bfs(graph, marked, n);

                Integer[] buf = new Integer[marked.size() - boundary];
                marked.subList(boundary, marked.size()).toArray(buf);
                results.add(buf);
            }
        }
        // 返回结果
        return results;
    }

    private static void bfs(Graph graph, List<Integer> marked, Integer src) {
        
        // 直接访问起点，将其标记并置入队列
        Queue<Integer> queue = new ArrayDeque<>();
        marked.add(src);
        queue.add(src);

        // 迭代整张图
        while (!queue.isEmpty()) {
            for (Integer i:graph.adj(queue.poll())) {
                if (!marked.contains(i)) {
                    marked.add(i);
                    queue.add(i);
                }
            }
        }
    }

    // 判定顶点合法性的工具函数
    public static void validateVertex(int v, Graph graph) {
        if (v < 0 || v >= graph.V()) {
            throw new IllegalArgumentException("vertex " + v + " is not between 0 and " + (graph.V() - 1));
        }
    }
}
```

测试用例1，构造一个2个分量的无向图，分别从```顶点1```和```顶点2```开始遍历，下面是原图：

<img src="/images/algorithm/map/search/bfs_code.png" title="bfs_code" alt="bfs_code" style="max-width:70%;margin:auto;" />

完整用例代码：

```java
public class TestSearch {

    @Test
    public void testGraphBFS() {

        // 构造图
        Graph graph = new ListGraph(10);
        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 5);
        graph.addEdge(2, 5);
        graph.addEdge(6, 5);
        graph.addEdge(2, 6);
        graph.addEdge(3, 6);
        graph.addEdge(3, 2);
        graph.addEdge(3, 7);
        graph.addEdge(6, 7);
        graph.addEdge(9, 8);

        // 从顶点0出发
        List<Integer[]> res = Graphs.breadthFirstTraverse(graph, 1);
        System.out.println("the forest from 1: ");
        for (Integer[] is : res) {
            System.out.println(Arrays.toString(is));
        }
        // 从顶点4出发
        List<Integer[]> res1 = Graphs.breadthFirstTraverse(graph, 2);
        System.out.println("the forest from 2: ");
        for (Integer[] is : res1) {
            System.out.println(Arrays.toString(is));
        }
        // 验证可达路径<1,5>
        System.out.println("the path 4->5: " + Graphs.breadthFirstSearch(graph, 4, 5));
        // 验证可达路径<2,4>
        System.out.println("the path 1->9: " + Graphs.breadthFirstSearch(graph, 1, 9));
    }
}
```

> 输出结果：
> the forest from 1: 
> \[1, 0, 5, 4, 2, 6, 3, 7]
> \[8, 9]
> the forest from 2: 
> \[2, 5, 6, 3, 1, 7, 0, 4]
> \[8, 9]
> the path 4->5: true
> the path 1->9: false

> 看官可以像DFS那节的捕捉图一样，自己画一下BFS的生成森林，体验一下队列是怎么在BFS中起作用的

测试用例2，构造一个2个分量的有向图，分别从```顶点0```和```顶点1```开始遍历，下面是原图：

<img src="/images/algorithm/map/search/bfs_code2.png" title="bfs_code2" alt="bfs_code2" style="max-width:70%;margin:auto;" />

```java
public class TestSearch {
    
    @Test
    public void testDigraphBFS() {

        // 构造有向图
        Digraph digraph = new ListDigraph(8);
        digraph.addEdge(4, 0);
        digraph.addEdge(1, 2);
        digraph.addEdge(1, 5);
        digraph.addEdge(5, 2);
        digraph.addEdge(2, 6);
        digraph.addEdge(3, 6);
        digraph.addEdge(3, 7);

        // 从顶点0出发
        List<Integer[]> res = Graphs.breadthFirstTraverse(digraph, 0);
        System.out.println("the forest from 0: ");
        for (Integer[] is : res) {
            System.out.println(Arrays.toString(is));
        }
        // 从顶点1出发
        List<Integer[]> res1 = Graphs.breadthFirstTraverse(digraph, 1);
        System.out.println("the forest from 1: ");
        for (Integer[] is : res1) {
            System.out.println(Arrays.toString(is));
        }
        // 验证可达路径<1,6>
        System.out.println("the path 1->6: " + Graphs.breadthFirstSearch(digraph, 1, 6));
        // 验证可达路径<1,7>
        System.out.println("the path 1->7: " + Graphs.breadthFirstSearch(digraph, 1, 7));
    }
}
```

> 输出结果：
> the forest from 0: 
> \[0]
> \[1, 2, 5, 6]
> \[3, 7]
> \[4]
> the forest from 1: 
> \[1, 2, 5, 6]
> \[3, 7]
> \[4, 0]
> the path 1->6: true
> the path 1->7: false

可以看出，有向图的BFS也是具有差异性的

###### BFS的时空分析

BFS的时空复杂度和DFS的类似，不过是将辅助结构从栈换成了队列，具体如下：

- DFS的空间复杂度为```O(|V|)```
- 采用邻接矩阵的DFS的时间复杂度为```O(|V|**2)```
- 采用邻接表的DFS的时间复杂度为```O(|V|+|E|)```

###### BFS和单源最短路径问题

设一个非带权图```G=(V,E)```，其```顶点u```和```顶点v```的最短路径```d(u,v)```为从```顶点u```和```顶点v```的所有路径中**最少的边数**，若不存在通路则```d(u,v)```=```∞```

使用BFS可以很容易解决单源最短路径问题（单源表示只有一个确定起点和一个确定终点），因为BFS是层次模型，它会按照离起点**由近到远**的优先级来将顶点纳入访问集，观察下面的广度优先生成树：

<img src="/images/algorithm/map/search/bfs_tree.png" title="bfs_tree" alt="bfs_tree" style="max-width:70%;margin:auto;" />

从```顶点1```和```顶点2```有4条简单通路，分别是：

1. ```1,5,2```
2. ```1,5,6,2```
3. ```1,5,6,3,2```
4. ```1,5,6,7,3,2```

由于BFS的策略，```1,5,2```早于其它路径（比如```1,5,6,2```）被纳入访问集（也就是会尽可能靠近起点），所以可以在BFS生成树里看到，```顶点2```在树的第3层，只要简单给层次数做个减法就可以得到最短路径，即```d(1,2)```=```2```

#### 总结

DFS和BFS是几乎所有图论算法的基础，因为搜索算法讨论的是图的连通性问题，连通性是图的本质属性（个体产生相互作用，才能形成关系图），其本质区别其实是**栈**和**队列**在数据结构特性上的区别：

1. **栈**是一种**记录型结构**，适合需要回溯的递归算法，所以DFS更具**探索性**，使用DFS遍历图，可以快速体系其整体性质
2. **队列**是一种**缓冲型结构**，可以很好地保存顶点之间的前后顺序，所以BFS更具**层次性**，其遍历图也是“一圈一圈”地“层层递进”

图的搜索算法是典型的小巧却异常强大的强应用算法，需好好掌握

行文匆忙，如果看到错误或代码bug，还请issue或在评论区指出(\*/ω＼*)

#### 参考

[wiki-图论](https://zh.wikipedia.org/wiki/图论)
[Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/)
[离散数学](https://item.jd.com/11658913.html)
[数据结构](https://item.jd.com/12793968.html)
