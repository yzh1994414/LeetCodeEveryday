'''将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(2019)
        res = result
        while l1!=None and l2!=None:
            node_1, node_2 = l1.val,l2.val
            if node_1>node_2:
                res.next = ListNode(node_2)
                res = res.next
                l2 = l2.next
            else:
                res.next = ListNode(node_1)
                res = res.next
                l1 = l1.next
        
        if l1!=None:
            res.next = l1
        if l2!=None:
            res.next = l2
        return result.next
        
if __name__ == "__main__":
    while(True):
        inputs_1 = input('inputs:').split(',')
        inputs_2 = input('inputs:').split(',')
        if inputs_1 == 'quit':
            break
        solution = Solution()
        l1,l2 = ListNode(2019), ListNode(2019)
        t_l1,t_l2 = l1,l2
        for i,j in zip(inputs_1,inputs_2):
            t_l1.next = ListNode(i)
            t_l2.next = ListNode(j)
            t_l1 = t_l1.next
            t_l2 = t_l2.next
        print(solution.mergeTwoLists(l1 = l1.next,l2=l2.next))