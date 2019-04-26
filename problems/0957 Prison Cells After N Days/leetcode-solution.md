# 0957 - Prison Cells After N Days

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table | [Leetcode](https://leetcode.com/problems/prison-cells-after-n-days) | [solution](https://leetcode.com/problems/prison-cells-after-n-days/solution/)


-----------

<p>There are 8 prison cells in a row, and each cell is either occupied or vacant.</p>

<p>Each day, whether the cell is occupied or vacant changes according to the following rules:</p>

<ul>
	<li>If a cell has two adjacent neighbors that are both occupied or both vacant,&nbsp;then the cell becomes occupied.</li>
	<li>Otherwise, it becomes vacant.</li>
</ul>

<p>(Note that because the prison is a row, the first and the last cells in the row can&#39;t have two adjacent neighbors.)</p>

<p>We describe the current state of the prison&nbsp;in the following way:&nbsp;<code>cells[i] == 1</code> if the <code>i</code>-th cell is occupied, else <code>cells[i] == 0</code>.</p>

<p>Given the initial state of the prison, return the state of the prison after <code>N</code> days (and <code>N</code> such changes described above.)</p>

<p>&nbsp;</p>

<div>
<ol>
</ol>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>cells = <span id="example-input-1-1">[0,1,0,1,1,0,0,1]</span>, N = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">[0,0,1,1,0,0,0,0]</span>
<strong>Explanation: 
</strong><span id="example-output-1">The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]</span>

</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>cells = <span id="example-input-2-1">[1,0,0,1,0,0,1,0]</span>, N = <span id="example-input-2-2">1000000000</span>
<strong>Output: </strong><span id="example-output-2">[0,0,1,1,1,1,1,0]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>cells.length == 8</code></li>
	<li><code>cells[i]</code> is in <code>{0, 1}</code></li>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ol>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Simulation

**Intuition**

We simulate each day of the prison.

Because there are at most 256 possible states for the prison, eventually the states repeat into a cycle rather quickly.  We can keep track of when the states repeat to find the period `t` of this cycle, and skip days in multiples of `t`.

**Algorithm**

Let's do a naive simulation, iterating one day at a time.  For each day, we will decrement `N`, the number of days remaining, and transform the state of the prison forward (`state -> nextDay(state)`).

If we reach a state we have seen before, we know how many days ago it occurred, say `t`.  Then, because of this cycle, we can do `N %= t`.  This ensures that our algorithm only needs $$O(2**{\text{cells.length}})$$ steps.

<iframe src="https://leetcode.com/playground/HKcoATQ8/shared" frameBorder="0" width="100%" height="500" name="HKcoATQ8"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^N)$$, where $$N$$ is the number of cells in the prison.

* Space Complexity:  $$O(2^N * N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
