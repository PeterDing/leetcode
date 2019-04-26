# 0572 - Subtree of Another Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/subtree-of-another-tree) | [solution](https://leetcode.com/problems/subtree-of-another-tree/solution/)


-----------

<p>
Given two non-empty binary trees <b>s</b> and <b>t</b>, check whether tree <b>t</b> has exactly the same structure and node values with a subtree of <b>s</b>. A subtree of <b>s</b> is a tree consists of a node in <b>s</b> and all of this node's descendants. The tree <b>s</b> could also be considered as a subtree of itself.
</p>

<p><b>Example 1:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
</pre>
Given tree t:
<pre>
   4 
  / \
 1   2
</pre>
Return <b>true</b>, because t has the same structure and node values with a subtree of s.
</p>

<p><b>Example 2:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
    /
   0
</pre>
Given tree t:
<pre>
   4
  / \
 1   2
</pre>
Return <b>false</b>.
</p>

-----------


## Similar Problems

- [Medium] [Count Univalue Subtrees](count-univalue-subtrees)

- [Medium] [Most Frequent Subtree Sum](most-frequent-subtree-sum)




## Solution:

[TOC]


## Solution

---
#### Approach #1 Using Preorder Traversal [Accepted]

**Algorithm**

We can find the preorder traversal of the given tree $$s$$ and $$t$$, given by, say $$s_{preorder}$$ and $$t_{preorder}$$ respectively(represented in the form of a string). Now, we can check if $$t_{preorder}$$ is a substring of $$s_{preorder}$$. 

But, in order to use this approach, we need to treat the given tree in a different manner. Rather than assuming a $$null$$ value for the childern of the leaf nodes, we need to treat the left and right child as a $$lnull$$ and $$rnull$$ value respectively. This is done to ensure that the $$t_{preorder}$$ doesn't become a substring of $$s_{preorder}$$ even in cases when $$t$$ isn't a subtree of $$s$$. 

You can also note that we've added a '#' before every considering every value. If this isn't done, the trees of the form `s:[23, 4, 5]` and `t:[3, 4, 5]` will also give a true result since the preorder string of the `t("23 4 lnull rull 5 lnull rnull")` will be a substring of the preorder string of `s("3 4 lnull rull 5 lnull rnull")`. Adding a '#' before the node's value solves this problem.

![Preorder_null](../Figures/572_Subtree_1.PNG)
{:align="center"}

![Preorder_lnull_rnull](../Figures/572_Subtree_2.PNG)
{:align="center"}


<iframe src="https://leetcode.com/playground/cagXWqSv/shared" frameBorder="0" name="cagXWqSv" width="100%" height="513"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m^2+n^2+m*n)$$. A total of $$n$$ nodes of the tree $$s$$ and $$m$$ nodes of tree $$t$$ are traversed. Assuming string concatenation takes $$O(k)$$ time for strings of length $$k$$ and `indexOf` takes $$O(m*n)$$.

* Space complexity : $$O(max(m,n))$$. The depth of the recursion tree can go upto $$n$$ for tree $$t$$ and $$m$$ for tree $$s$$ in worst case.

---
#### Approach #2 By Comparison of Nodes  [Accepted]

**Algorithm**

Instead of creating an inorder traversal, we can treat every node of the given tree $$t$$ as the root, treat it as a subtree and compare the corresponding subtree with the given subtree $$s$$ for equality. For checking the equality, we can compare the all the nodes of the two subtrees. 

For doing this, we make use a function `traverse(s,t)` which traverses over the given tree $$s$$ and treats every node as the root of the subtree currently being considered. It also checks the two subtrees currently being considered for their equality. In order to check the equality of the two subtrees, we make use of `equals(x,y)` function, which takes $$x$$ and $$y$$, which are the roots of the two subtrees to be compared as the inputs and returns True or False depending on whether the two are equal or not. It compares all the nodes of the two subtrees for equality. Firstly, it checks whether the roots of the two trees for equality and then calls itself recursively for the left subtree and the right subtree.

The follwowing animation depicts an abstracted view of the process:

!?!../Documents/572_Subtree.json:1000,563!?!

<iframe src="https://leetcode.com/playground/A6ipy4aH/shared" frameBorder="0" name="A6ipy4aH" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m*n)$$. In worst case(skewed tree) `traverse` function takes $$O(m*n)$$ time. 

* Space complexity : $$O(n)$$. The depth of the recursion tree can go upto $$n$$. $$n$$ refers to the number of nodes in $$s$$.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
