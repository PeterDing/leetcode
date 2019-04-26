# 0655 - Print Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/print-binary-tree) | [solution](https://leetcode.com/problems/print-binary-tree/solution/)


-----------

<p>Print a binary tree in an m*n 2D string array following these rules: </p>

<ol>
<li>The row number <code>m</code> should be equal to the height of the given binary tree.</li>
<li>The column number <code>n</code> should always be an odd number.</li>
<li>The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (<b>left-bottom part and right-bottom part</b>). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them. </li>
<li>Each unused space should contain an empty string <code>""</code>.</li>
<li>Print the subtrees following the same rules.</li>
</ol>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
     1
    /
   2
<b>Output:</b>
[["", "1", ""],
 ["2", "", ""]]
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>
     1
    / \
   2   3
    \
     4
<b>Output:</b>
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b>
      1
     / \
    2   5
   / 
  3 
 / 
4 
<b>Output:</b>

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
</pre>
</p>

<p><b>Note:</b>
The height of binary tree is in the range of [1, 10].
</p>

-----------


## Similar Problems




## Solution:

[TOC]


## Solution

---
#### Approach #1 Recursive Solution[Accepted]

We start by initializing a $$res$$ array with the dimensions being $$height$$x$$2^{height}-1$$. Here, $$height$$ refers to the number of levels in the given tree. In order to fill this $$res$$ array with the required elements, initially, we fill the complete array with `""` .  After this we make use of a recursive function `fill(res, root, i, l, r)` which fills the $$res$$ array such that the current element has to be filled in $$i^{th}$$ row, and the column being the middle of the indices $$l$$ and $$r$$, where $$l$$ and $$r$$ refer to the left and the right boundaries of the columns in which the current element can be filled.

In every recursive call, we do as follows:

1. If we've reached the end of the tree, i.e. if root==null, return.

2. Determine the column in which the current element($$root$$) needs to be filled, which is the middle of $$l$$ and $$r$$, given by say, $$j$$. The row number is same as $$i$$. Put the current element at $$res[i][j]$$.

3. Make the recursive call for the left child of the $$root$$ using `fill(res, root.left, i + 1, l, (l + r) / 2)`.

4. Make the recursive call for the right child of the $$root$$ using `fill(res, root.right, i + 1, (l + r + 1) / 2, r)`.

Note, that in the last two recursive calls, we update the row number(level of the tree). This ensures that the child nodes fit into the correct row. We also update the column boundaries appropriately based on the $$l$$ and $$r$$ values.

Further, to determine the $$height$$ also, we make use of recursive funtion `getHeight(root)`, which returns the height of the tree starting from the $$root$$ node. We traverse into all the branches possible in the tree recursively and find the depth of the longest branch.

At the end, we convert the $$res$$ array into the required list format, before returning the results.

<iframe src="https://leetcode.com/playground/ncTFx4nd/shared" frameBorder="0" name="ncTFx4nd" width="100%" height="479"></iframe>

**Complexity Analysis**

* Time complexity : $$O(h*2^h)$$. We need to fill the $$res$$ array of size $$h$$x$$2^h - 1$$. Here, $$h$$ refers to the height of the given tree.

* Space complexity : $$O(h*2^h)$$.  $$res$$ array of size $$h$$x$$2^h - 1$$ is used.

---
#### Approach #2 Using queue(BFS)[Accepted]

**Algorithm**

We can also solve the problem by making use of Breadth First Search's idea. For this, we make use of a class $$Params$$ which stores the parameters of a $$node$$ of  the tree, including its value, its level in the tree($$i$$), and the left($$l$$) and right($$r$$) boundaries of the columns in which this element can be filled in the result to be returned.

We start by initializing a $$res$$ array as in the previous approach. After this, we add the parametrized $$root$$ of the tree into a $$queue$$. After this, we do the following at every step.

1. Remove an element, $$p$,  from the front of the $$queue$$. 

2. Add this element at its correct position in the $$res$$ array given by $$res[p.i][(p.l + p.r) / 2]$$. Here, the values $$i$$, $$l$$ and $$r$$ refer to the column/level number, and the left and right boundaries permissible for putting the current node into $$res$$. These are obtained from the node's parameters, which have been associated with it before putting it into the $$queue$$.

3. If the left child of $$p$$ exists, put it at the back of the $$queue$$, in a parametized form, by appropriately updating the level as the next level and the boundaries permissible as well.

4. If the right child of $$p$$ exists, put it at the back of the $$queue$$, in a parametized form, by appropriately updating the level as the next level and the boundaries permissible as well.

5. Continue steps 1. to 4. till the $$queue$$ becomes empty. 

At the end, we again convert the $$res$$ array into the required list format, before returning the results.


<iframe src="https://leetcode.com/playground/jb3EALV4/shared" frameBorder="0" name="jb3EALV4" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(h*2^h)$$. We need to fill the $$res$$ array of size $$h$$x$$2^h - 1$$. Here, $$h$$ refers to the height of the given tree.

* Space complexity : $$O(h*2^h)$$.  $$res$$ array of size $$h$$x$$2^h - 1$$ is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
