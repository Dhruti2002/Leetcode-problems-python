/*Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.*/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start,mid=0,0
        end = len(nums)-1

        while mid <= end:
            match nums[mid]:
                case 0:
                    self.swap(nums, start, mid)
                    start += 1
                    mid += 1
                case 1:
                    mid += 1
                case 2:
                    self.swap(nums, mid, end)
                    end -= 1
    
    def swap(self, nums: List[int], pos1: int, pos2: int) -> None:
        temp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = temp
