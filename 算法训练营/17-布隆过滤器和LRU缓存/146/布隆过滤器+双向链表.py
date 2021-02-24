#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start

class ListNode(object):
    def __init__(self, val, key=None) -> None:
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self._max_capacity = capacity
        self._cur_capacity = 0

        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        # 存放数据
        self._m = {}

    def get(self, key: int) -> int:
        node = self._m.get(key)
        if node is None:
            return -1
        
        node.prev.next = node.next
        node.next.prev = node.prev

        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self._m.get(key)
        # 如果存在，更新 value，更新节点位置
        if node is not None:
            node.val = value
            self._m[key] = node
            self.get(key)
            return
        # 如果不存在
        node = ListNode(value, key)
        self._m[key] = node
        # 插入链表头
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        # 如果没有达到最大容量限制, 直接退出
        if self._cur_capacity + 1 <= self._max_capacity:
            self._cur_capacity += 1
            return
        # 否则，删除链表尾节点
        del_node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        # 删除数据
        del self._m[del_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end