# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        result = []

        def find_paths(node, path):
            if node is None:
                return

            path += str(node.val)

            # If it is a leaf node
            if node.left is None and node.right is None:
                result.append(path)
                return

            path += "->"

            find_paths(node.left, path)
            find_paths(node.right, path)

        find_paths(root, "")

        return result
       
        