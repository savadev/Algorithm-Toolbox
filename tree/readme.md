### 二叉树

#### 时间
用O(N)的时间把规模拆成2个T(N/2):

T(N) = O(N) + 2 T(N/2) = O(N) + 2 O(N/2) + 4 T(N/4) = ... = logN * O(N) + N * T(1) = O(NlogN)


用O(1)的时间把规模拆成2个T(N/2):
T(N) = O(1) + 2T(N/2) = 2 O(1) + 4T(N/4) = ... = logN O(1) + N * T(1) = O(N)

#### Iterative Traversal
* Pre-order: [[Link](https://leetcode.com/problems/binary-tree-preorder-traversal)][[Code](144_binary_tree_preorder_traversal.py)].
* In-order: [[Link](https://leetcode.com/problems/binary-tree-inorder-traversal)][[Code](94_binary_tree_inorder_traversal.py)].
* Post-order: [[Link](https://leetcode.com/problems/binary-tree-postorder-traversal)][[Code](145_binary_tree_postorder_traversal.py)].

```Python
def preorderTraversal(self, root):
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()

        # do something --------
        ans.append(node.val)
        # ---------------------

        # add right child first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans

def inorderTraversal(self, root):
    # if root is None:
    #     return []

    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()

        # do something --------
        result.append(cur.val)
        # ---------------------

        cur = cur.right
    return result

def postorderTraversal(self, root):
    """
    Do not insert.
    Flip array in the end instead.
    """
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        u = stack.pop()

        ans.append(u.val)

        # add left child first
        if u.left:
            stack.append(u.left)
        if u.right:
            stack.append(u.right)
    return ans[::-1]
```

```Python
# simpler iterative algorithm, with extra space cost O(N) for flag
def traverse(self, root: TreeNode) -> List[int]:
    """
    Edge case:
        when input is null
        when child node is null
    """
    ans = []
    if not root: return ans
    stack = [(root, False)]
    while stack:
        node, ready = stack.pop()
        if ready:
            ans.append(node.val)
        else:
            # preorder
            if node.right: stack.append((node.right, False))
            if node.left: stack.append((node.left, False))
            stack.append((node, True))

            # in-order
            # if node.right: stack.append((node.right, False))
            # stack.append((node, True))
            # if node.left: stack.append((node.left, False))

            # post-order
            # stack.append((node, True))
            # if node.right: stack.append((node.right, False))
            # if node.left: stack.append((node.left, False))
    return ans
```



#### Recursion Traversal

```Python
def preorderTraversal(root):
    ans = []
    def traverse(node):
        if node is None: return
        ans.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse(root, ans)
    return ans

def inorderTraversal(root):
    ans = []
    def traverse(node):
        if node is None: return
        traverse(node.left)
        ans.append(node.val)
        traverse(node.right)
    traverse(root, ans)
    return ans

def postorderTraversal(root):
    ans = []
    def traverse(node):
        if node is None: return
        traverse(node.left)
        traverse(node.right)
        ans.append(node.val)
    traverse(root, ans)
    return ans
```

#### Recursion Divide & Conquer

```Python
def divideConquerTraversal(self, root):
  def traverse(node):
    if node is None: return []
    l = traverse(node.left)
    r = traverse(node.right)

    # preorder
    # return [node.val] + l + r

    # inorder
    # return l + [node.val] + r

    # post-order
    return l + r + [node.val]
  return traverse(root)
```

#### Primer 基础题
* Binary tree path (DC, DFS) [[Link](https://leetcode.com/problems/binary-tree-paths)][[Code](257_binary_tree_paths.py)].
* Minimum subtree (DC) [[Link](https://starllap.space/2017/05/30/LintCode-596-Minimum-Subtree/)][[Code](minimum_subtree.py)].

#### Application 经典题
* Balanced binary tree [[Link](https://leetcode.com/problems/balanced-binary-tree/)][[Code](110_balanced_binary_tree.py)].
* Tuple return: binary tree maximum average [[Link](https://www.lintcode.com/problem/subtree-with-maximum-average/description)][[Code](binary_tree_maximum_average.py)].
* Flatten binary tree to linked list [[Link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/)][[Code](114_flatten_binary_tree_to_linked_list.py)]
* **Lowest common ancestor** [[Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)][[Code](236_lowest_common_ancestor_of_a_binary_tree.py)]
* **Lowest common ancestor III** [[Link](https://www.lintcode.com/problem/lowest-common-ancestor-iii/)][[Code](lowest_common_ancestor_of_a_binary_tree_iii.py)]
  - Return null if LCA does not exist.
  - Return tuple
* Longest consecutive sequence in tree [[Link](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/)][[Code](298_binary_tree_longest_consecutive_sequencee.py)]
* Binary Tree Longest Consecutive Sequence [[Link](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/)][[Code](298_binary_tree_longest_consecutive_sequencee.py)].
* Binary Tree Longest Consecutive Sequence II [[Link](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/)][[Code](549_binary_tree_longest_consecutive_sequence_ii.py)]
* Path Sum [[Link](https://leetcode.com/problems/path-sum/)][[Code](112_path_sum.py)]
* Path Sum II [[Link](https://leetcode.com/problems/path-sum-ii)][[Code](113_path_sum_ii.py)]
* Binary Tree Path Sum II [[Screenshot](https://github.com/shawlu95/Algorithm-Toolbox/blob/master/tree/assets/binary_tree_path_sum_ii.png)] (no access to LintCode)
  - Must go straight down
  - Every node can be start or end of path
  - At every node, treat it as end note, and loop through every node in the path as possible start node.
  - There are N choose 2 possible paths
* Binary Tree Path Sum III [[Screenshot](https://github.com/shawlu95/Algorithm-Toolbox/blob/master/tree/assets/binary_tree_path_sum_iii.png)] (no access to LintCode)
  - May not go straight down
  - Every node can be turning point. Combine every left path to every right path.
