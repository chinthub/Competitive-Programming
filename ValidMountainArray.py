"""
Leetcode #941 : Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
-> arr.length >= 3
-> There exists some i with 0 < i < arr.length - 1 such that:
	arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
	arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
	https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        else:
            i=0
            while i+1 < n and arr[i] < arr[i+1]:
                i += 1

            if i == n-1 or i == 0:
                return False

            while i+1 < n and arr[i] > arr[i+1]:
                i += 1

            return (i == n-1)