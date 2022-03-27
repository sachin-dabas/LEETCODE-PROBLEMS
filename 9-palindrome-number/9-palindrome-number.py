class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev = s[::-1]
        print(rev)
        return s == rev