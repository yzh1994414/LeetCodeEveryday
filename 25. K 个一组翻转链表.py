'''给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        data = []
        while head != None:
            data.append(head.val)
            head = head.next
        ind , length = 0,len(data)
        while ind < length:
            r_ind = ind + k
            if r_ind >length: break
            tmp_list = data[ind:r_ind]
            tmp_list.reverse()
            data[ind:r_ind] = tmp_list
            ind = r_ind
        result = ListNode(2019)
        tmp_res = result
        for num in data:
            tmp_res.next=ListNode(num)
            tmp_res = tmp_res.next
        return result.next

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
        l = ListNode(2019)
        t_l = l
        for i in inputs_1:
            t_l.next = ListNode(i)
            t_l = t_l.next
        print(solution.reverseKGroup(head = l.next,k=3))

    