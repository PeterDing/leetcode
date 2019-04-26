# 0799 - Champagne Tower

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/champagne-tower) | [solution](https://leetcode.com/problems/champagne-tower/solution/)


-----------

<p>We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.&nbsp; Each glass holds one cup (250ml) of champagne.</p>

<p>Then, some champagne is poured in the first glass at the top.&nbsp; When the top most glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.&nbsp; When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.&nbsp; (A glass at the bottom row has it&#39;s excess champagne fall on the floor.)</p>

<p>For example, after one cup of champagne is poured, the top most glass is full.&nbsp; After two cups of champagne are poured, the two glasses on the second row are half full.&nbsp; After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.&nbsp; After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height:200px; width:290px" /></p>

<p>Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)</p>

<p>&nbsp;</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> poured = 1, query_glass = 1, query_row = 1
<strong>Output:</strong> 0.0
<strong>Explanation:</strong> We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

<strong>Example 2:</strong>
<strong>Input:</strong> poured = 2, query_glass = 1, query_row = 1
<strong>Output:</strong> 0.5
<strong>Explanation:</strong> We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>poured</code>&nbsp;will&nbsp;be&nbsp;in the range of <code>[0, 10 ^ 9]</code>.</li>
	<li><code>query_glass</code> and <code>query_row</code> will be in the range of <code>[0, 99]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Simulation [Accepted]

**Intuition**

Instead of keeping track of how much champagne should end up in a glass, keep track of the total amount of champagne that flows through a glass.  For example, if `poured = 10` cups are poured at the top, then the total flow-through of the top glass is `10`; the total flow-through of each glass in the second row is `4.5`, and so on.

**Algorithm**

In general, if a glass has flow-through `X`, then `Q = (X - 1.0) / 2.0` quantity of champagne will equally flow left and right.  We can simulate the entire pour for 100 rows of glasses.  A glass at `(r, c)` will have excess champagne flow towards `(r+1, c)` and `(r+1, c+1)`.

<iframe src="https://leetcode.com/playground/GbytuGmq/shared" frameBorder="0" width="100%" height="344" name="GbytuGmq"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(R^2)$$, where $$R$$ is the number of rows.  As this is fixed, we can consider this complexity to be $$O(1)$$.

* Space Complexity: $$O(R^2)$$, or $$O(1)$$ by the reasoning above.

---

Analysis written by: [@awice](https://leetcode.com/awice).
