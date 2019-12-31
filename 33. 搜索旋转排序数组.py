'''假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums)== 0: return -1
        left,right,mid = 0,len(nums),len(nums)//2
        rotated_ind = right-1
        while left < right:
            if mid-1>=0 and (nums[mid] <= nums[mid-1]) and mid+1<len(nums) and (nums[mid] <= nums[mid+1]):
                rotated_ind = mid
                break
            if nums[mid] > nums[0]: left = mid+1
            else : right = mid
            mid = (left+right)//2
        l1,l2,r1,r2,m1,m2 = 0,rotated_ind,rotated_ind,len(nums),rotated_ind//2,(rotated_ind+len(nums))//2
        while l1<r1:
            if nums[m1] < target: l1 = m1+1
            elif nums[m1] > target: r1 = m1
            else: return m1
            m1 = (l1+r1)//2
        while l2<r2:
            if nums[m2] < target: l2 = m2+1
            elif nums[m2] > target: r2 = m2
            else: return m2       
            m2 = (l2+r2)//2
        return -1
            
if __name__  == "__main__":
    inputs = [4,5,6,7,8,9,1,2,3]
    target = 1
    solution = Solution()
    solution.search(nums=inputs,target=target)