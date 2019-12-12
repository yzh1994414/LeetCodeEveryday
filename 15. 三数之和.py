'''给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# import numpy as np

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         one_dim_dict = {}
#         one_dim_cnt_dict = {}
#         res = []
#         for i in nums:
#             one_dim_dict[-i] = i
#             if one_dim_cnt_dict.get(i) ==None:
#                 one_dim_cnt_dict[i]= 1
#             else :
#                 one_dim_cnt_dict[i]+=1
#         nums = np.sort(list(set(nums))).tolist()
#         max_nums = nums[len(nums)-1]
#         max
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 nums_1,nums_2 = nums[i],nums[j]
#                 if (nums_1 == nums_2) and one_dim_cnt_dict[nums_1]<2:
#                     continue
#                 tmp_num = nums_1 + nums_2
#                 if(tmp_num>max_nums):
#                     break
#                 sub_num = one_dim_dict.get(tmp_num)
#                 if sub_num!=None :
#                     cnt = one_dim_cnt_dict[sub_num]
#                     if (nums_1 == sub_num):
#                         cnt -= 1
#                     if (nums_2 == sub_num):
#                         cnt -= 1
#                     if cnt>= 1:
#                         tmp_res = np.sort([nums_1,nums_2,one_dim_dict.get(tmp_num)]).tolist()
#                         flag = True
#                         for arr in res:
#                             if arr == tmp_res:
#                                 flag = False
#                                 break
                
#                         if flag:
#                              res.append(tmp_res)
        
#         return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res