# 0735 - Asteroid Collision

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack | [Leetcode](https://leetcode.com/problems/asteroid-collision) | [solution](https://leetcode.com/problems/asteroid-collision/solution/)


-----------

<p>
We are given an array <code>asteroids</code> of integers representing asteroids in a row.
</p><p>
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).  Each asteroid moves at the same speed.
</p><p>
Find out the state of the asteroids after all collisions.  If two asteroids meet, the smaller one will explode.  If both are the same size, both will explode.  Two asteroids moving in the same direction will never meet.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
asteroids = [5, 10, -5]
<b>Output:</b> [5, 10]
<b>Explanation:</b> 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
asteroids = [8, -8]
<b>Output:</b> []
<b>Explanation:</b> 
The 8 and -8 collide exploding each other.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> 
asteroids = [10, 2, -5]
<b>Output:</b> [10]
<b>Explanation:</b> 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
</pre>
</p>

<p><b>Example 4:</b><br />
<pre>
<b>Input:</b> 
asteroids = [-2, -1, 1, 2]
<b>Output:</b> [-2, -1, 1, 2]
<b>Explanation:</b> 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>asteroids</code> will be at most <code>10000</code>.</li>
<li>Each asteroid will be a non-zero integer in the range <code>[-1000, 1000].</code>.</li>
</p>

-----------


## Similar Problems

- [Easy] [Can Place Flowers](can-place-flowers)




## Solution:

[TOC]

#### Approach #1: Stack [Accepted]

**Intuition**

A row of asteroids is stable if no further collisions will occur.  After adding a new asteroid to the right, some more collisions may happen before it becomes stable again, and all of those collisions (if they happen) must occur right to left.  This is the perfect situation for using a *stack*.

**Algorithm**

Say we have our answer as a stack with rightmost asteroid `top`, and a `new` asteroid comes in.  If `new` is moving right (`new > 0`), or if `top` is moving left (`top < 0`), no collision occurs.

Otherwise, if `abs(new) < abs(top)`, then the `new` asteroid will blow up; if `abs(new) == abs(top)` then both asteroids will blow up; and if `abs(new) > abs(top)`, then the `top` asteroid will blow up (and possibly more asteroids will, so we should continue checking.)

<iframe src="https://leetcode.com/playground/CyN24YU5/shared" frameBorder="0" width="100%" height="480" name="CyN24YU5"></iframe>


**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of asteroids.  Our stack pushes and pops each asteroid at most once.

* Space Complexity: $$O(N)$$, the size of `ans`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
