# 0623 - Add One Row to Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/add-one-row-to-tree) | [solution](https://leetcode.com/problems/add-one-row-to-tree/solution/)


-----------

<p>Given the root of a binary tree, then value <code>v</code> and depth <code>d</code>, you need to add a row of nodes with value <code>v</code> at the given depth <code>d</code>. The root node is at depth 1. </p>

<p>The adding rule is: given a positive integer depth <code>d</code>, for each NOT null tree nodes <code>N</code> in depth <code>d-1</code>, create two tree nodes with value <code>v</code> as <code>N's</code> left subtree root and right subtree root. And <code>N's</code> <b>original left subtree</b> should be the left subtree of the new left subtree root, its <b>original right subtree</b> should be the right subtree of the new right subtree root. If depth <code>d</code> is 1 that means there is no depth d-1 at all, then create a tree node with value <b>v</b> as the new root of the whole original tree, and the original tree is the new root's left subtree.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

<b>v = 1</b>

<b>d = 2</b>

<b>Output:</b> 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

<b>v = 1</b>

<b>d = 3</b>

<b>Output:</b> 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The given d is in range [1, maximum depth of the given tree + 1].</li>
<li>The given binary tree has at least one tree node.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1 Using Recursion(DFS) [Accepted]

If the given depth $$d$$ happens to be equal to 1, we can directly put the whole current tree as a left child of the newly added node. Otherwise, we need to put the new node at appropriate levels. 

To do so, we make use of a recursive function `insert(val,node,depth,n)`. Here, $$val$$ refers to the value of the new node to be inserted, $$depth$$ refers to the depth of the node currently considered, $$node$$ refers to the node calling the current function for its child subtrees and $$n$$ refers to the height at which the new node needs to be inserted. 

For inserting the new node at appropriate level, we can start by making a call to `insert` with the root node and 1 as the current level. Inside every such call, we check if we've reached one level prior to the level where the new node needs to be inserted. 

From this level, we can store the roots of the left and right subtrees of the current node temporarily, and insert the new node as the new left and right subchild of the current node, with the temporarily stored left and right subtrees as the left and right subtrees of the newly inserted left or right subchildren appropriately.

But, if we haven't reached the destined level, we keep on continuing the recursive calling process with the left and right children of the current node respectively. At every such call, we also incrmenet the depth of the current level to reflect the depth change appropriately.

The animation below illustrates the process:

!?!../Documents/623_Add_One_Row_Recursion_New.json:1000,563!?!

<iframe src="https://leetcode.com/playground/mqAnMFzQ/shared" frameBorder="0" name="mqAnMFzQ" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. A total of $$n$$ nodes of the given tree will be considered.

* Space complexity : $$O(n)$$. The depth of the recursion tree can go upto $$n$$ in the worst case(skewed tree).

---
#### Approach #2 Using stack(DFS) [Accepted]

**Algorithm**

We can do the same task as discussed in the last approach by making use of a $$stack$$ as well. But, we need to make use of a new data structure, $$Node$$ here, to keep a track of the depth of the current node along with its value. 

We start by pushing the root $$Node$$ onto the $$stack$$. Then, at every step we do as follows:

* Pop an element from the $$stack$$. 

* For every Node popped, check if its depth corresponds to one prior to the depth at which the new node needs to be inserted. 

* If yes, insert the new nodes appropriately as in the last approach. 

* If no, we push both the left and the right child Node(value+depth) of the current node onto the $$stack$$. 

* Continue the popping and pushing process till the $$stack$$ becomes empty.

Look at the animation below for a better understanding.

!?!../Documents/623_Add_One_Row_Stack_new.json:1000,563!?!

<iframe src="https://leetcode.com/playground/6Gut8kVG/shared" frameBorder="0" name="6Gut8kVG" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. A total of $$n$$ nodes of the given tree will be considered.

* Space complexity : $$O(n)$$. The depth of the $$stack$$ can go upto $$n$$ in the worst case(skewed tree).

---

#### Approach #3 Using queue(BFS) [Accepted]

**Algorithm**

The idea of traversal in the last approach is similar to Depth First Search. In that case, we need to traverse through all the nodes of the given tree in the order of branches. Firstly we explored one branch to as much depth as possible and then continued with the other ones. 

If, instead, we go for Breadth First Search, along with keeping track of the depth of the nodes being considered at any moment during the Breadth First Search, we can stop the search process as soon as all the nodes at the depth $$d - 1$$ have been considered once. 

To implement this BFS, we make use of a $$queue$$. We start off by pushing the root node of the given tree at the back of the $$queue$$ and with the depth of the current level set as 1. Then, at every step, we do the following:

* Remove an element from the front of the $$queue$$ and add all its children to the back of another temporary queue, $$temp$$. 

* Keep on adding the elements to the back of the $$temp$$ till $$queue$$ becomes empty. (Once $$queue$$ becomes empty, it indicates that all the nodes at the current level have been considered and now $$temp$$ contains all the nodes lying at the next level).

* Reinitialize $$queue$$  with its value as $$temp$$. Update the current value of the $$depth$$ to reflect the level of nodes currently being considered. 

* Repeat the process till we reach the depth $$d - 1$$. 

* On hitting this depth level($$d-1$$), add the new nodes appropriately to all the nodes in the $$queue$$ currently, as done in the previous approaches.

The following animation illustrates the process.

!?!../Documents/623_Add_One_Row_queue_new.json:1000,563!?!

<iframe src="https://leetcode.com/playground/EC8ne3QM/shared" frameBorder="0" name="EC8ne3QM" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. A total of $$n$$ nodes of the given tree will be considered in the worst case.

* Space complexity : $$O(x)$$. The size of the $$queue$$ or $$temp$$ queue can grow upto $$x$$ only. Here, $$x$$ refers to the number of maximum number of nodes at any level in the given tree.

---


Analysis written by: [@vinod23](https://leetcode.com/vinod23)
