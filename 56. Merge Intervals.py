# Brute Force Solution 
# Time Complexity is : O(nlogn + 2n)
# Space Complexity is : O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if ans and end <= ans[-1][1]:
                continue
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans 
# Optimal Solution 
# Time COmplexity is O(nlog + n)
# Space Complexity is O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for i in range(len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][-1])
        return ans 
        