class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha = []
        answer = True
        for i in s:
            if i.isalpha() or i.isnumeric():
                alpha.append(i)
        for j in range(len(alpha)//2):
            if alpha[j] != alpha[len(alpha)-1-j]:
                return False
        return answer


test = Solution()
print(test.isPalindrome("0P"))



