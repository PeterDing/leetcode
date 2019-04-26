# 0662 - Maximum Width of Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/maximum-width-of-binary-tree) | [solution](https://leetcode.com/problems/maximum-width-of-binary-tree/solution/)


-----------

<p>Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a <b>full binary tree</b>, but some nodes are null.</p>

<p>The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the <code>null</code> nodes between the end-nodes are also counted into the length calculation.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

<b>Output:</b> 4
<b>Explanation:</b> The maximum width existing in the third level with the length 4 (5,3,null,9).
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 

          1
         /  
        3    
       / \       
      5   3     

<b>Output:</b> 2
<b>Explanation:</b> The maximum width existing in the third level with the length 2 (5,3).
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> 

          1
         / \
        3   2 
       /        
      5      

<b>Output:</b> 2
<b>Explanation:</b> The maximum width existing in the second level with the length 2 (3,2).
</pre>

<p><b>Example 4:</b></p>

<pre>
<b>Input:</b> 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
<b>Output:</b> 8
<b>Explanation:</b>The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


</pre>

<p><b>Note:</b> Answer will in the range of 32-bit signed integer.</p>


-----------


## Similar Problems




## Solution:

[TOC]

#### Approach Framework

**Explanation**

As we need to reach every node in the given tree, we will have to traverse the tree, either with a depth-first search, or with a breadth-first search.

The main idea in this question is to give each node a `position` value. If we go down the left neighbor, then `position -> position * 2`; and if we go down the right neighbor, then `position -> position * 2 + 1`. This makes it so that when we look at the position values `L` and `R` of two nodes with the same depth, the width will be `R - L + 1`.

---
#### Approach #1: Breadth-First Search [Accepted]

**Intuition and Algorithm**

Traverse each node in breadth-first order, keeping track of that node's position.  For each depth, the first node reached is the left-most, while the last node reached is the right-most.

<iframe src="https://leetcode.com/playground/GsZid6zn/shared" frameBorder="0" width="100%" height="500" name="GsZid6zn"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the number of nodes in the input tree.  We traverse every node.

* Space Complexity: $$O(N)$$, the size of our `queue`.

---
#### Approach #2: Depth-First Search [Accepted]

**Intuition and Algorithm**

Traverse each node in depth-first order, keeping track of that node's position.  For each depth, the position of the first node reached of that depth will be kept in `left[depth]`.

Then, for each node, a candidate width is `pos - left[depth] + 1`.  We take the maximum of the candidate answers.

<iframe src="https://leetcode.com/playground/A9iKAcsQ/shared" frameBorder="0" width="100%" height="344" name="A9iKAcsQ"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the number of nodes in the input tree.  We traverse every node.

* Space Complexity: $$O(N)$$, the size of the implicit call stack in our DFS.

---

Analysis written by: [@awice](https://leetcode.com/awice).
