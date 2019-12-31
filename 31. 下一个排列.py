'''实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_num = -65535
        sort_ind = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=max_num:
                max_num = nums[i]
            else:
                min_num,min_ind = 65535, -1
                for j in range(i+1,len(nums)):
                    if nums[j]<=nums[i]: continue
                    if nums[j] <min_num:
                        min_num = nums[j]
                        min_ind = j
                tmp = nums[i]
                nums[i] = nums[min_ind]
                nums[min_ind] = tmp
                sort_ind = i
                break
        if sort_ind==-1:
            nums.sort()
            return nums
        tmp_nums = nums[sort_ind+1 :]
        tmp_nums.sort()
        nums[sort_ind+1:] = tmp_nums
        return nums

if __name__ == "__main__":
  while True:
    #s = input('Inputs :').split(',')
    s=[1,5,1]
    if s =='quit':
      break
    solution = Solution()
    solution.nextPermutation(nums = s)




