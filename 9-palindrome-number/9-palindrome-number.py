class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        result = 0
        s = x
        while s > 0:
            result = (result*10)
            result += (s%10)
            i += 1
            s = s//10
        return x == result



    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     rev = s[::-1]
    #     return s == rev