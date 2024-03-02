"""
* Review
- 1st : 2/27/24 ~ 2/28/24
"""


# Solution 1)
# TC : O(N)
# MC : O(LogN)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def _insert_recursive(nums, start, end):

            if start > end:
                return None

            mid = (start + end) // 2
            new_node = TreeNode(nums[mid])

            new_node.left = _insert_recursive(nums, start, mid - 1)
            new_node.right = _insert_recursive(nums, mid + 1, end)

            return new_node

        return _insert_recursive(nums, 0, len(nums) - 1)
