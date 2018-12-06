#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (37.34%)
# Total Accepted:    362.5K
# Total Submissions: 970.8K
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = []
        if x < 0:
            return False
        while x:
            last_digit = x % 10
            num.append(last_digit)
            left_num = x // 10
            if left_num:
                x = left_num
            else:
                break
        length = len(num)
        l = length // 2
        for i in range(l):
            if num[i] != num[length - i -1]:
                return False
        return True

