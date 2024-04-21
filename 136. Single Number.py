class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missing_number = 0
        for num in nums:
            missing_number ^= num
        return missing_number
        