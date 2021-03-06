# 缓存淘汰策略

LRU, LFU, FIFO。

# 数组与链表的区别

数组是一块**连续的内存空间**；链表是一组**零散的内存块**。

数组连续内存，可借助 CPU 的缓存机制，预读数组中的数据，所以访问效率高；链表内存不连续，不能借助 CPU 缓存机制。

- 链表：插入，删除 O(1); 随机访问 O(n)
- 数组：插入，删除 O(n); 随机访问 O(1)

# 常见链表分类

- 单向
- 双向
- 循环
- 双向循环

# 链表缺点

对链表进行频繁的插入、删除操作，会导致频繁的内存申请和释放，容易造成内存碎片。

# 题型

- [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)
- [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
- [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
- [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
- [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)
