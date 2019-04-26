# 0558 - Quad Tree Intersection

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/quad-tree-intersection) | [solution](https://leetcode.com/problems/quad-tree-intersection/solution/)


-----------

<p>A quadtree is a tree data in which each internal node has exactly four children: <code>topLeft</code>, <code>topRight</code>, <code>bottomLeft</code> and <code>bottomRight</code>. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.</p>

<p>We want to store True/False information in our quad tree. The quad tree is used to represent a <code>N * N</code> boolean grid. For each node, it will be subdivided into four children nodes <strong>until the values in the region it represents are all the same</strong>. Each node has another two boolean attributes : <code>isLeaf</code> and <code>val</code>. <code>isLeaf</code> is true if and only if the node is a leaf node. The <code>val</code> attribute for a leaf node contains the value of the region it represents.</p>

<p>For example, below are two quad trees A and B:</p>

<pre>
A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

B:               
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   T   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight:
     topLeft: F
     topRight: F
     bottomLeft: T
     bottomRight: T
bottomLeft: T
bottomRight: F
</pre>

<p>&nbsp;</p>

<p>Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.</p>

<pre>
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>Both <code>A</code> and <code>B</code>&nbsp;represent grids of size <code>N * N</code>.</li>
	<li><code>N</code> is guaranteed to be a power of 2.</li>
	<li>If you want to know more about the quad tree, you can refer to its <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a>.</li>
	<li>The logic OR operation is defined as this: &quot;A or B&quot; is true if <code>A is true</code>, or if <code>B is true</code>, or if <code>both A and B are true</code>.</li>
</ol>


-----------


## Similar Problems




## Thought:
