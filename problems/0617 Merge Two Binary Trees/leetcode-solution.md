# 0617 - Merge Two Binary Trees

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/merge-two-binary-trees) | [solution](https://leetcode.com/problems/merge-two-binary-trees/solution/)


-----------

<p>Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.</p>

<p>You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
<b>Output:</b> 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> The merging process must start from the root nodes of both trees.</p>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1 Using Recursion [Accepted]

We can traverse both the given trees in a preorder fashion. At every step, we check if the current node exists(isn't null) for both the trees. If so, we add the values in the current nodes of both the trees and update the value in the current node of the first tree to reflect this sum obtained. At every step, we also call the original function `mergeTrees()` with the left children and then with the right children of the current nodes of the two trees. If at any step, one of these children happens to be null, we return the child of the other tree(representing the corresponding child subtree) to be added as a child subtree to the calling parent node in the first tree. At the end, the first tree will represent the required resultant merged binary tree.

The following animation illustrates the process.

!?!../Documents/617_Merge_Trees_Recursion.json:1000,563!?!

<iframe src="https://leetcode.com/playground/d9nZDPEJ/shared" frameBorder="0" name="d9nZDPEJ" width="100%" height="428"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m)$$. A total of $$m$$ nodes need to be traversed. Here, $$m$$ represents the minimum number of nodes from the two given trees.

* Space complexity : $$O(m)$$. The depth of the recursion tree can go upto $$m$$ in the case of a skewed tree. In average case, depth will be $$O(logm)$$.

---
#### Approach #2 Iterative Method [Accepted]

**Algorithm**

In the current approach, we again traverse the two trees, but this time we make use of a $$stack$$ to do so instead of making use of recursion. Each entry in the $$stack$$ strores data in the form $$[node_{tree1}, node_{tree2}]$$. Here, $$node_{tree1}$$ and $$node_{tree2}$$ are the nodes of the first tree and the second tree respectively.

We start off by pushing the root nodes of both the trees onto the $$stack$$. Then, at every step, we remove a node pair from the top of the stack. For every node pair removed, we add the values corresponding to the two nodes and update the value of the corresponding node in the first tree. Then, if the left child of the first tree exists, we push the left child(pair) of both the trees onto the stack. If the left child of the first tree doesn't exist, we append the left child(subtree) of the second tree to the current node of the first tree. We do the same for the right child pair as well. 

If, at any step, both the current nodes are null, we continue with popping the next nodes from the $$stack$$.

The following animation depicts the process.

!?!../Documents/617_Merge_Trees_Stack.json:1000,563!?!

<iframe src="https://leetcode.com/playground/v2TK7i2x/shared" frameBorder="0" name="v2TK7i2x" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. We traverse over a total of $$n$$ nodes. Here, $$n$$ refers to the smaller of the number of nodes in the two trees.

* Space complexity : $$O(n)$$. The depth of stack can grow upto $$n$$ in case of a skewed tree.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
