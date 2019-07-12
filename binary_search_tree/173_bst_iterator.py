# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dumb
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        Use in-order traversal to serialize tree
        """
        self.cur = 0
        arr = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            # do something
            arr.append(node)

            node = node.right

        self.arr = arr

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            idx = self.cur
            self.cur += 1
            return self.arr[idx].val
        return

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.cur < len(self.arr)


# smart
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        node = root
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        smallest = self.stack.pop()

        # if the node that's popped has a right node
        # it means all right children are greater than the popped node and smaller than its parent
        # need to repopulate the stack by left traverssal
        cur = smallest.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return smallest.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
