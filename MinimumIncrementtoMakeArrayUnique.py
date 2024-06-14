#You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
#Return the minimum number of moves to make every value in nums unique.
#The test cases are generated so that the answer fits in a 32-bit integer.
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        arr = sorted(nums)
        min_moves = 0 
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                min_moves += arr[i-1] - arr[i] + 1
                arr[i] = arr[i-1] + 1
        return min_moves 
