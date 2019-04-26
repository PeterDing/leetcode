# 0101 - Symmetric Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree, Depth-first Search, Breadth-first Search | [Leetcode](https://leetcode.com/problems/symmetric-tree) | [solution](https://leetcode.com/problems/symmetric-tree/solution/)


-----------

<p>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).</p>

<p>
For example, this binary tree <code>[1,2,2,3,4,4,3]</code> is symmetric:
<pre>
    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>
</p>
<p>
But the following <code>[1,2,2,null,3,null,3]</code>  is not:<br />
<pre>
    1
   / \
  2   2
   \   \
   3    3
</pre>
</p>

<p>
<b>Note:</b><br />
Bonus points if you could solve it both recursively and iteratively.
</p>

-----------


## Similar Problems




## Solution:

## Solution
---

#### Approach 1: Recursive

A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

![Push an element in stack](https://leetcode.com/media/original_images/101_Symmetric.png){:width="200px"}
{:align="center"}

Therefore, the question is: when are two trees a mirror reflection of each other?

Two trees are a mirror reflection of each other if:

1. Their two roots have the same value.
2. The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

![Push an element in stack](https://leetcode.com/media/original_images/101_Symmetric_Mirror.png){:width="400px"}
{:align="center"}

This is like a person looking at a mirror. The reflection in the mirror has the same head, but the reflection's right arm corresponds to the actual person's left arm, and vice versa.

The explanation above translates naturally to a recursive function as follows.

<iframe src="https://leetcode.com/playground/bQ9ZjXvv/shared" frameBorder="0" width="100%" height="242" name="bQ9ZjXvv"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Because we traverse the entire input tree once, the total run time is $$O(n)$$, where $$n$$ is the total number of nodes in the tree.


* Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in $$O(n)$$. Therefore, space complexity due to recursive calls on the stack is $$O(n)$$ in the worst case.
<br />
<br />
---
#### Approach 2: Iterative

Instead of recursion, we can also use iteration with the aid of a queue. Each two consecutive nodes in the queue should be equal, and their subtrees a mirror of each other. Initially, the queue contains `````root````` and `````root`````. Then the algorithm works similarly to BFS, with some key differences. Each time, two nodes are extracted and their values compared. Then, the right and left children of the two nodes are inserted in the queue in opposite order. The algorithm is done when either the queue is empty, or we detect that the tree is not symmetric (i.e. we pull out two consecutive nodes from the queue that are unequal).

<iframe src="https://leetcode.com/playground/n5mXkUjQ/shared" frameBorder="0" width="100%" height="344" name="n5mXkUjQ"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Because we traverse the entire input tree once, the total run time is $$O(n)$$, where $$n$$ is the total number of nodes in the tree.


* Space complexity : There is additional space required for the search queue. In the worst case, we have to insert $$O(n)$$ nodes in the queue. Therefore, space complexity is $$O(n)$$.
