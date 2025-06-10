class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() #ListNode의 시작점
        current = dummy #결과 리스트 순회하며 노드를 추가할 포인터
        carry = 0 #자리 올림수

        while l1 or l2 or carry: #l1,l2,carry가 남아 있으면 계속 덧셈 수행
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10 #10 이상일때 carry 발생*자리올림수
 
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next