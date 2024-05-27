def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def longest_path(node):

            if node is None:
                return 0

            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        
        return diameter