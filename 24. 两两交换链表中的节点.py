'''给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapnodes(self,node:ListNode):
        if node == None or node.next == None:
            return node
        next_node = node.next
        tmp_node = next_node.next
        node.next = tmp_node
        next_node.next = node         
        return next_node

    def swapPairs(self, head: ListNode) -> ListNode:
        cnt = 0
        res = ListNode(2019)
        res.next = head
        pre = res
        while head != None:
            if cnt%2 == 0:
                head = self.swapnodes(head)
                pre.next = head
                pre = head.next
            head = head.next
            cnt += 1
        return res.next

if __name__ == "__main__":
    while(True):
        inputs_1 = input('inputs:').split(',')
        #inputs_2 = input('inputs:').split(',')
        if inputs_1 == 'quit':
            break
        solution = Solution()
        # l1,l2 = ListNode(2019), ListNode(2019)
        # t_l1,t_l2 = l1,l2
        # for i,j in zip(inputs_1,inputs_2):
        #     t_l1.next = ListNode(i)
        #     t_l2.next = ListNode(j)
        #     t_l1 = t_l1.next
        #     t_l2 = t_l2.next
        l1 = ListNode(2019)
        t_l1 = l1
        for i in inputs_1:
            t_l1.next = ListNode(i)
            t_l1 = t_l1.next
        res = solution.swapPairs(head = l1.next)
