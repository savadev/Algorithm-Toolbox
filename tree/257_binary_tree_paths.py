import Tree
treeVals = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):

    def binaryTreePaths(self, root):
        """
        九章算法模版：Divide & Conquer
        """
        def divide(root):
            if not root:
                # needed for missing child
                return []

            if not root.left and not root.right:
                # leaf node, pay attention to nested bracket!
                return [[str(root.val)]]

            paths = divide(root.left) + divide(root.right)
            return [[str(root.val)] + path for path in paths]

        return ["->".join(path) for path in divide(root)]

    ans = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        def dfs(node, tmp):
            if not node:
                return

            # for IDE
            val = node.val

            tmp.append(node.val)
            if not node.left and not node.right:
                self.ans.append(list(tmp))

            for child in [node.left, node.right]:
                dfs(child, tmp)

            tmp.pop()
        dfs(root, [])
        return ["->".join([str(i) for i in l]) for l in self.ans]

    def binaryTreePaths2(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        def dfs(node, tmp):
            # it a node doesn't exist it doesn't mean a leaf node
            if not node:
                return

            # for IDE
            val = node.val

            # is leaf node if has neither left nor right child
            tmp.append(node.val)
            if not node.left and not node.right:
                # use list() method to create a copy
                self.ans.append(list(tmp))
                return # optional
            dfs(node.left, tmp)
            dfs(node.right, tmp)

            # remove current node before backtrack
            # the list is passed by reference, and changes will be reflected in earlier call
            tmp.pop()

        dfs(root, [])
        return ["->".join([str(i) for i in l]) for l in self.ans]

    # arm-length recursion
    def binaryTreePaths3(self, root: TreeNode) -> List[str]:
        self.ans = []
        def dfs(node, tmp):
            # by adding the following line, the base case is never reached
            if not node:
                # still need to handle edge case, root = None
                print("Reached None")
                return

            # is leaf node if has neither left nor right child
            tmp.append(node.val)
            if not node.left and not node.right:
                # use list() method to create a copy
                self.ans.append(list(tmp))
                tmp.pop() # arm-length recursion
                return # arm-length recursion

            if node.left: dfs(node.left, tmp) # arm-length recursion
            if node.right: dfs(node.right, tmp) # arm-length recursion

            # remove current node before backtrack
            # the list is passed by reference, and changes will be reflected in earlier call
            tmp.pop()

        dfs(root, [])
        return ["->".join([str(i) for i in l]) for l in self.ans]

#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
solver = Solution()
print(solver.binaryTreePaths2(root))
