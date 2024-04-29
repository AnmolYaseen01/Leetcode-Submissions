class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])

# Test cases
solution = Solution()

s1 = "Hello World"
print(solution.lengthOfLastWord(s1))  

s2 = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s2))  

s3 = "luffy is still joyboy"
print(solution.lengthOfLastWord(s3))  

        