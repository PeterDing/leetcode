# 0637 - Average of Levels in Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/average-of-levels-in-binary-tree) | [solution](https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/)


-----------

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
    3
   / \
  9  20
    /  \
   15   7
<b>Output:</b> [3, 14.5, 11]
<b>Explanation:</b>
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The range of node's value is in the range of 32-bit signed integer.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Binary Tree Level Order Traversal](binary-tree-level-order-traversal)

- [Easy] [Binary Tree Level Order Traversal II](binary-tree-level-order-traversal-ii)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Using Depth First Search [Accepted]

**Algorithm**

One of the methods to solve the given problem is to make use of Depth First Search. In DFS, we try to exhaust each branch of the given tree during the tree traversal before moving onto the next branch.

To make use of DFS to solve the given problem, we make use of two lists $$count$$ and $$res$$. Here, $$count[i]$$ refers to the total number of nodes found at the $$i^{th}$$ level(counting from root at level 0) till now, and $$res[i]$$ refers to the sum of the nodes at the $$i^{th}$$ level encountered till now during the Depth First Search.

We make use of a function `average(t, i, res, count)`, which is used to fill the $$res$$ and $$count$$ array if we start the DFS from the node $$t$$ at the $$i^{th}$$ level in the given tree. We start by making the function call `average(root, 0, res, count)`. After this, we do the following at every step:

1. Add the value of the current node to the $$res$$(or $$sum$$) at the index corresponding to the current level. Also, increment the $$count$$ at the index corresponding to the current level. 

2. Call the same function, `average`, with the left and the right child of the current node. Also, update the current level used in making the function call.

3. Repeat the above steps till all the nodes in the given tree have been considered once.

4. Populate the averages in the resultant array to be returned.


The following animation illustrates the process.

!?!../Documents/637_Avg_of_Levels_DFS.json:1000,563!?!


<iframe src="https://leetcode.com/playground/eyx7WogA/shared" frameBorder="0" name="eyx7WogA" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. The whole tree is traversed once only. Here, $$n$$ refers to the total number of nodes in the given binary tree.

* Space complexity : $$O(h)$$. $$res$$ and $$count$$ array of size $$h$$ are used. Here, $$h$$ refers to the height(maximum number of levels) of the given binary tree. Further, the depth of the recursive tree could go upto $$h$$ only.

---
#### Approach #2 Breadth First Search [Accepted]

**Algorithm**

Another method to solve the given problem is to make use of a Breadth First Search. In BFS, we start by pushing the root node into a $$queue$$. Then, we remove an element(node) from the front of the $$queue$$. For every node removed from the $$queue$$, we add all its children to the back of the same $$queue$$. We keep on continuing this process till the $$queue$$ becomes empty. In this way, we can traverse the given tree on a level-by-level basis.

But, in the current implementation, we need to do a slight modification, since we need to separate the nodes on one level from that of the other. 

The steps to be performed are listed below:

1. Put the root node into the $$queue$$.

2. Initialize $$sum$$ and $$count$$ as 0 and $$temp$$ as an empty queue.

3. Pop a node from the front of the $$queue$$. Add this node's value to the $$sum$$ corresponding to the current level. Also, update the $$count$$ corresponding to the current level.

4. Put the children nodes of the node last popped into the a $$temp$$ queue(instead of $$queue$$).

5. Continue steps 3 and 4 till $$queue$$ becomes empty. (An empty $$queue$$ indicates that one level of the tree has been considered).

6. Reinitialize $$queue$$ with its value as $$temp$$.

7. Populate the $$res$$ array with the average corresponding to the current level.

8. Repeat steps 2 to 7 till the $$queue$$ and $$temp$$ become empty.


At the end, $$res$$ is the required result.

The following animation illustrates the process.

!?!../Documents/637_Average_Of_Levels.json:1000,563!?!


<iframe src="https://leetcode.com/playground/92XSTJqk/shared" frameBorder="0" name="92XSTJqk" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. The whole tree is traversed atmost once. Here, $$n$$ refers to the number of nodes in the given binary tree.

* Space complexity : $$O(m)$$. The size of $$queue$$ or $$temp$$ can grow upto atmost the maximum number of nodes at any level in the given binary tree. Here, $$m$$ refers to the maximum mumber of nodes at any level in the input tree.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
