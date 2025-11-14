class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l, r = 0, 0
        while r<len(nums):
            if nums[r] == val:
                nums.pop(r)
            else:
                r += 1
        print(r, nums)
Solution().removeElement([0,1,2,2,3,0,4,2], 2)