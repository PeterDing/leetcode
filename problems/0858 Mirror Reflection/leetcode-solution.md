# 0858 - Mirror Reflection

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math | [Leetcode](https://leetcode.com/problems/mirror-reflection) | [solution](https://leetcode.com/problems/mirror-reflection/solution/)


-----------

<p>There is&nbsp;a special square room with mirrors on each of the four&nbsp;walls.&nbsp; Except for the southwest&nbsp;corner, there are receptors on each of the remaining corners, numbered <code>0</code>, <code>1</code>, and <code>2</code>.</p>

<p>The square room has walls of length <code>p</code>, and a laser ray from the southwest corner&nbsp;first meets the east wall at a distance <code>q</code>&nbsp;from the <code>0</code>th receptor.</p>

<p>Return the number of the receptor that the ray meets first.&nbsp; (It is guaranteed that the ray will meet&nbsp;a receptor eventually.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>p = <span id="example-input-1-1">2</span>, q = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>The ray meets receptor 2 the first time it gets reflected back to the left wall.
<p><img alt="" src="https://ibb.co/mYSFJT" /><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/18/reflection.png" style="width: 218px; height: 217px;" /></p>
</pre>


<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= p &lt;= 1000</code></li>
	<li><code>0 &lt;= q &lt;= p</code></li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Simulation

**Intuition**

The initial ray can be described as going from an origin `(x, y) = (0, 0)` in the direction `(rx, ry) = (p, q)`.  From this, we can figure out which wall it will meet and where, and what the appropriate new ray will be (based on reflection.)  We keep simulating the ray until it finds it's destination.

**Algorithm**

The parameterized position of the laser after time `t` will be `(x + rx * t, y + ry * t)`.  From there, we know when it will meet the east wall (if `x + rx * t == p`), and so on.  For a positive (and nonnegligible) time `t`, it meets the next wall.

We can then calculate how the ray reflects.  If it hits an east or west wall, then `rx *= -1`, else `ry *= -1`.

In Java, care must be taken with floating point operations.

<iframe src="https://leetcode.com/playground/Ds4FZeYo/shared" frameBorder="0" width="100%" height="500" name="Ds4FZeYo"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(p)$$.  We can prove (using *Approach #2*) that the number of bounces is bounded by this.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
#### Approach 2: Mathematical

**Intuition and Algorithm**

Instead of modelling the ray as a bouncing line, model it as a straight line through reflections of the room.

For example, if `p = 2, q = 1`, then we can reflect the room horizontally, and draw a straight line from `(0, 0)` to `(4, 2)`.  The ray meets the receptor `2`, which was reflected from `(0, 2)` to `(4, 2)`.

In general, the ray goes to the first integer point `(kp, kq)` where `k` is an integer, and `kp` and `kq` are multiples of `p`.  Thus, the goal is just to find the smallest `k` for which `kq` is a multiple of `p`.

The mathematical answer is `k = p / gcd(p, q)`.

<iframe src="https://leetcode.com/playground/srjkydcW/shared" frameBorder="0" width="100%" height="327" name="srjkydcW"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log P)$$, the complexity of the `gcd` operation.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
