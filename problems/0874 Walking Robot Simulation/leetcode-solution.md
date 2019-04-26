# 0874 - Walking Robot Simulation

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Greedy | [Leetcode](https://leetcode.com/problems/walking-robot-simulation) | [solution](https://leetcode.com/problems/walking-robot-simulation/solution/)


-----------

<p>A robot on an infinite grid starts at point (0, 0) and faces north.&nbsp; The robot can receive one of three possible types of commands:</p>

<ul>
	<li><code>-2</code>: turn left 90 degrees</li>
	<li><code>-1</code>: turn right 90 degrees</li>
	<li><code>1 &lt;= x &lt;= 9</code>: move forward <code>x</code> units</li>
</ul>

<p>Some of the grid squares are obstacles.&nbsp;</p>

<p>The <code>i</code>-th obstacle is at grid point <code>(obstacles[i][0], obstacles[i][1])</code></p>

<p>If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)</p>

<p>Return the <strong>square</strong> of the maximum Euclidean distance that the robot will be from the origin.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>commands = <span id="example-input-1-1">[4,-1,3]</span>, obstacles = <span id="example-input-1-2">[]</span>
<strong>Output: </strong><span id="example-output-1">25</span>
<span>Explanation: </span>robot will go to (3, 4)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>commands = <span id="example-input-2-1">[4,-1,4,-2,4]</span>, obstacles = <span id="example-input-2-2">[[2,4]]</span>
<strong>Output: </strong><span id="example-output-2">65</span>
<strong>Explanation</strong>: robot will be stuck at (1, 4) before turning left and going to (1, 8)
</pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= commands.length &lt;= 10000</code></li>
	<li><code>0 &lt;= obstacles.length &lt;= 10000</code></li>
	<li><code>-30000 &lt;= obstacle[i][0] &lt;= 30000</code></li>
	<li><code>-30000 &lt;= obstacle[i][1] &lt;= 30000</code></li>
	<li>The answer is guaranteed to be less than <code>2 ^ 31</code>.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Simulation

**Intuition**

We simulate the path of the robot step by step.  Since there are at most 90000 steps, this is efficient enough to pass the given input limits.

**Algorithm**

We store the robot's position and direction.  If we get a turning command, we update the direction; otherwise we walk the specified number of steps in the given direction.

Care must be made to use a `Set` data structure for the obstacles, so that we can check efficiently if our next step is obstructed.  If we don't, our check `is point in obstacles` could be ~10,000 times slower.

In some languages, we need to encode the coordinates of each obstacle as a `long` integer so that it is a hashable key that we can put into a `Set` data structure.  Alternatively, we could also encode the coordinates as a `string`.

<iframe src="https://leetcode.com/playground/BzLAA5NV/shared" frameBorder="0" width="100%" height="500" name="BzLAA5NV"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + K)$$, where $$N, K$$ are the lengths of `commands` and `obstacles` respectively.

* Space Complexity:  $$O(K)$$, the space used in storing the `obstacleSet`.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
