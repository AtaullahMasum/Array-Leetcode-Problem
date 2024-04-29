#Better Solution using Hashing
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        threshold =len(nums)//3
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        for key, freq in hashMap.items():
            if freq > threshold:
                result.append(key)
        return result
# Optimal Solution using Modified Moore Voting Algorithm
# Time Complexity is O(n)+O(n)
# Space Compelxity is O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        cnt1 , cnt2, elem1, elem2 = 0,0, None, None
        for num in nums:
            if cnt1 == 0 and elem2 != num:
                cnt1  = 1
                elem1 = num
            elif cnt2 == 0 and elem1 != num:
                cnt2 = 1
                elem2 = num
            elif elem1 == num:
                cnt1 += 1
            elif elem2 == num:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        #return [elem1, elem2]
        count1, count2 = 0,0
        for num in nums:
            if num == elem1:
                count1 += 1
            if num == elem2:
                count2 += 1
        threshold = len(nums)//3
       
        if count1 > threshold:
            result.append(elem1)
        if count2 > threshold:
            result.append(elem2)
        return result
        