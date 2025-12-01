# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# 530. Minimum Absolute Difference in BST

def getMinimumDifference(root):
    
    values = []

    def inorder(node):

        if not node:
            return
        
        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)

    min_diff = float('inf')
    for i in range(1, len(values)):
        min_diff = min(min_diff, values[i] - values[i-1])

    return min_diff
