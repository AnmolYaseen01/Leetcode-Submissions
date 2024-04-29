class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
        
        return prefix

# Test cases
solution = Solution()
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  

strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  
