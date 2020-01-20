'''给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = True
    def traverse(self,left: TreeNode, right: TreeNode):
        if left==None and right==None:
            return
        if left==None or right==None:
            self.res = False
            return 
        if  left.val!=right.val:
            self.res = False
            return 
        self.traverse(left.left,right.right)
        self.traverse(left.right,right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None: return True
        self.traverse(root.left,root.right)
        return self.res