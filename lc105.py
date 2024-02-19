"""
* Review 
1st (1/27/24)
2nd (2/19/24)

* Questions
트리 출력하는 부분은 코드에 안 넣어도 되는건가?

* Concepts
preorder : root -> left -> right
postorder : left -> right -> root
inorder : left -> root -> right

"""

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left =left
        self. right = right

def print_tree_preorder(root):
    
    if not root:
        return
    
    print(root.val)
    print_tree_preorder(root.left)
    print_tree_preorder(root.right)


    
        
# def print_tree(root):
#     if not root:
#         return
    
#     queue = deque([root])

#     while queue:
#         node = queue.popleft()
#         print(node.val, end=" ")

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

class Solution:
    def buildTree(self, preorder : List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
    
        root = TreeNode(preorder[0])
        # print(root.val)
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid +1], inorder[:mid])
        root.right = self.buildTree(preorder[mid +1:], inorder[mid+1:])
    
        return root
    
# Solution 클래스의 인스턴스 생성 및 트리 생성
sol = Solution()
result_tree = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# 생성된 트리 출력
print_tree_preorder(result_tree)