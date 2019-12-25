'''合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''130/131'''
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         res = ListNode(2019)
#         result = res
#         no_nan_index = [i for i in range(0, len(lists)) if lists[i]!=None]
#         lists = [lists[i] for i in no_nan_index]
#         while len(lists)>1:
#             index = -1
#             minimum = 65535
#             for i in range(len(lists)):
#                 l = lists[i]
#                 if l.val<minimum:
#                     minimum = l.val
#                     index = i
#             result.next = ListNode(minimum)
#             result = result.next
#             lists[index] = lists[index].next
#             if (lists[index]==None):
#                 del lists[index]
#         if (len(lists)==1):
#             result.next = lists[0]
#         return res.next

'''130/131'''
# class Solution:
#     def Merge_sort(self,lists_1: ListNode , lists_2: ListNode) -> ListNode:   
#         lists = ListNode(2019)
#         tmp_lists = lists
#         while lists_1!=None and lists_2!=None:
#             if lists_1.val < lists_2.val: 
#                 tmp_lists.next = ListNode(lists_1.val)
#                 tmp_lists = tmp_lists.next
#                 lists_1 = lists_1.next
#             else:
#                 tmp_lists.next = ListNode(lists_2.val)
#                 tmp_lists = tmp_lists.next
#                 lists_2 = lists_2.next
#         if lists_1!=None: tmp_lists.next = lists_1
#         if lists_2!=None: tmp_lists.next = lists_2
#         return  lists.next

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
#         if(len(lists)==0): return None
#         result = lists[0]
#         for i in range(1,len(lists)):
#             result = self.Merge_sort(result,lists[i])
#         return result

'''131/131'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        data = []
        for i in range(len(lists)):
            node = lists[i]
            while node!=None:
                data.append(node.val)
                node = node.next
        data.sort()
        res = ListNode(2019)
        tmp_res = res 
        for i in data:
            tmp_res.next = ListNode(i)
            tmp_res = tmp_res.next
        return res.next