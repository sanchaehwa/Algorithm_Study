import sys

class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Cards:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:  # 리스트가 비어있는 경우
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head == self.tail:  # 하나만 남은 경우
            val = self.head.val
            self.head = self.tail = None
            return val
        val = self.head.val
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        return val

    def move_front_to_back(self):
        if self.head != self.tail:
            self.head = self.head.next
            self.tail = self.tail.next

    def get_only_node_value(self):
        return self.head.val if self.head else None

class Solution:
    def card2(self):
        n = int(sys.stdin.readline())
        dq = Cards()
        for i in range(1, n + 1):
            dq.append(i)

        while dq.head != dq.tail:
            dq.pop_front()
            dq.move_front_to_back()

        print(dq.get_only_node_value())

solution = Solution()
solution.card2()