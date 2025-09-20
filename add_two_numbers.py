class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(nums):
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

if __name__ == "__main__":
    l1 = build_list([2,4,3])
    l2 = build_list([5,6,4])
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print(print_list(result))  # [7,0,8]

