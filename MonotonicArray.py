#An array is monotonic if it is either monotone increasing or monotone decreasing.
#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#Given an integer array nums, return true if the given array is monotonic, or false otherwise.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0 : return True
        first = nums[0]
        last = nums[n-1]

        if first > last:
            for i in range(n-1):
                if nums[i] < nums[i+1]: return False
        elif first == last:
            for i in range(n-1):
                if nums[i] != nums[i+1]: return False
        else:
            for i in range(n-1):
                if nums[i] > nums[i+1]: return False

        return True
