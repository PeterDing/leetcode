# 0959 - Regions Cut By Slashes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search, Union Find, Graph | [Leetcode](https://leetcode.com/problems/regions-cut-by-slashes) | [solution](https://leetcode.com/problems/regions-cut-by-slashes/solution/)


-----------

<p>In a N x N&nbsp;<code>grid</code> composed of 1 x 1 squares, each 1 x 1 square consists of a <code>/</code>, <code>\</code>, or blank space.&nbsp; These characters divide the square into contiguous regions.</p>

<p>(Note that backslash characters are escaped, so a <code>\</code>&nbsp;is represented as <code>&quot;\\&quot;</code>.)</p>

<p>Return the number of regions.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-1-1">[
&nbsp; &quot; /&quot;,
&nbsp; &quot;/ &quot;
]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-2-1">[
&nbsp; &quot; /&quot;,
&nbsp; &quot;  &quot;
]</span>
<strong>Output: </strong><span id="example-output-2">1</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-3-1">[
&nbsp; &quot;\\/&quot;,
&nbsp; &quot;/\\&quot;
]</span>
<strong>Output: </strong><span id="example-output-3">4</span>
<strong>Explanation: </strong>(Recall that because \ characters are escaped, &quot;\\/&quot; refers to \/, and &quot;/\\&quot; refers to /\.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/3.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-4-1">[
&nbsp; &quot;/\\&quot;,
&nbsp; &quot;\\/&quot;
]</span>
<strong>Output: </strong><span id="example-output-4">5</span>
<strong>Explanation: </strong>(Recall that because \ characters are escaped, &quot;/\\&quot; refers to /\, and &quot;\\/&quot; refers to \/.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-5-1">[
&nbsp; &quot;//&quot;,
&nbsp; &quot;/ &quot;
]</span>
<strong>Output: </strong><span id="example-output-5">3</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/5.png" style="width: 82px; height: 82px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;/&#39;</code>, <code>&#39;\&#39;</code>, or <code>&#39; &#39;</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Union-Find

**Intuition**

To find the number of components in a graph, we can use either depth-first search or union find.  The main difficulty with this problem is in specifying the graph.

One "brute force" way to specify the graph is to associate each grid square with 4 nodes (north, south, west, and east), representing 4 triangles inside the square if it were to have both slashes.  Then, we can connect all 4 nodes if the grid square is `" "`, and connect two pairs if the grid square is `"/"` or `"\"`.  Finally, we can connect all neighboring nodes (for example, the east node of the square at `grid[0][0]` connects with the west node of the square at `grid[0][1]`).

This is the most straightforward approach, but there are other approaches that use less nodes to represent the underlying information.

**Algorithm**

Create `4*N*N` nodes, one for each grid square, and connect them as described above.  After, we use a union find structure to find the number of connected components.

We will skip the explanation of how a DSU structure is implemented.  Please refer to [https://leetcode.com/problems/redundant-connection/solution/](https://leetcode.com/problems/redundant-connection/solution/) for a tutorial on DSU.

<iframe src="https://leetcode.com/playground/jdYrnNjc/shared" frameBorder="0" width="100%" height="500" name="jdYrnNjc"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * N * \alpha(N))$$, where $$N$$ is the length of the grid, and $$\alpha$$ is the Inverse-Ackermann function (if we were to use union-find by rank.)

* Space Complexity:  $$O(N * N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
