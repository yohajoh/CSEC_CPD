# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         l, r = 0, 0
#         while r<len(nums):
#             if nums[r] == val:
#                 nums.pop(r)
#             else:
#                 r += 1
#         print(r, nums)
# Solution().removeElement([0,1,2,2,3,0,4,2], 2)


# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         l, r = 0, len(s) - 1
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#         print(s)
# Solution().reverseString(["h","e","l","l","o"])

# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l, r = 0, 1
#         while r < len(nums):
#             if nums[r] != 0 and nums[l] == 0:
#                 nums[l], nums[r] = nums[r], nums[l]
#             if nums[l] != 0:
#                 l += 1
#             r += 1
#         print(nums)
# Solution().moveZeroes([1,2])

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            else: 
                r -= 1
        return []
print(Solution().twoSum([2,3,4], 6))
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         left = 0
#         right = len(height) - 1
#         best = 0
#         while left < right:
#             h = min(height[left], height[right])
#             w = right - left
#             area = h * w
#             if area > best:
#                 best = area
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return best              
# print(Solution().maxArea([1,1]))

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         l, r = 0, 1
#         while r<len(nums):
#             if len(nums) == 1:
#                 return 1, nums
#             if nums[l] == nums[r]:
#                 nums[r] = '_'
#                 r += 1
#             else:
#                 nums[l+1], nums[r] = nums[r], nums[l+1]
#                 r += 1
#                 l += 1
#         return l + 1
            
        
# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))