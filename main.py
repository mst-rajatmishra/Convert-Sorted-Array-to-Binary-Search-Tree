from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert_to_bst(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if the current subarray is empty
            if left > right:
                return None
            
            # Find the middle index
            mid = (left + right) // 2
            
            # Create the root node with the middle element
            root = TreeNode(nums[mid])
            
            # Recursively construct the left and right subtrees
            root.left = convert_to_bst(left, mid - 1)
            root.right = convert_to_bst(mid + 1, right)
            
            return root
        
        # Start the recursion with the full range of the array
        return convert_to_bst(0, len(nums) - 1)
