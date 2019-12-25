'''给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 65535
        res_gap = 65535
        for i in range(len(nums)):
            if res_gap == 0:
                break  
            num = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                sum_3 = num+nums[l]+nums[r]
                if abs(sum_3-target) < res_gap:
                    res_gap = abs(sum_3 - target)
                    res = sum_3
                if res_gap == 0:
                    break            
                if sum_3 > target:
                    r-=1
                    while (l<r) and nums[r] == nums[r+1]:
                        r-=1                    
                else :
                    l+=1
                    while (l<r) and nums[l] == nums[l-1]:
                        l+=1
        return res  