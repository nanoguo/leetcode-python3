#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (37.53%)
# Total Accepted:    826.5K
# Total Submissions: 2.2M
# Testcase Example:  '[3,2,4]\n6'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup={}
        for cnt, num in enumerate(nums):
            if target-num in lookup:
                return lookup[target-num], cnt
            lookup[num]=cnt

