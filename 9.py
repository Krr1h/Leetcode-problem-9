class Solution(object):
    def isPalindrome(self, x):
        L = list(str(x))
        J = L[::-1]
        if L == J:
            return True
        else:
            return False