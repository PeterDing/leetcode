# 0849 - Maximize Distance to Closest Person

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/maximize-distance-to-closest-person) | [solution](https://leetcode.com/problems/maximize-distance-to-closest-person/solution/)


-----------

<p>In a row of <code>seats</code>, <code>1</code> represents a person sitting in that seat, and <code>0</code> represents that the seat is empty.&nbsp;</p>

<p>There is at least one empty seat, and at least one person sitting.</p>

<p>Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.&nbsp;</p>

<p>Return that maximum distance to closest person.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,0,0,1,0,1]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,0,0,0]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= seats.length &lt;= 20000</code></li>
	<li><code>seats</code>&nbsp;contains only 0s or 1s, at least one <code>0</code>, and at least one <code>1</code>.</li>
</ol>
</div>
</div>


-----------


## Similar Problems

- [Medium] [Exam Room](exam-room)




## Solution:

[TOC]

---
#### Approach #1: Next Array [Accepted]

**Intuition**

Let `left[i]` be the distance from seat `i` to the closest person sitting to the left of `i`.  Similarly, let `right[i]` be the distance to the closest person sitting to the right of `i`.  This is motivated by the idea that the closest person in seat `i` sits a distance `min(left[i], right[i])` away.

**Algorithm**

To construct `left[i]`, notice it is either `left[i-1] + 1` if the seat is empty, or `0` if it is full.  `right[i]` is constructed in a similar way.

<iframe src="https://leetcode.com/playground/Mdkek4gh/shared" frameBorder="0" width="100%" height="480" name="Mdkek4gh"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `seats`.

* Space Complexity:  $$O(N)$$, the space used by `left` and `right`.


---
#### Approach #2: Two Pointer [Accepted]

**Intuition**

As we iterate through seats, we'll update the closest person sitting to our left, and closest person sitting to our right.

**Algorithm**

Keep track of `prev`, the filled seat at or to the left of `i`, and `future`, the filled seat at or to the right of `i`.

Then at seat `i`, the closest person is `min(i - prev, future - i)`, with one exception.  `i - prev` should be considered infinite if there is no person to the left of seat `i`, and similarly `future - i` is infinite if there is no one to the right of seat `i`.

<iframe src="https://leetcode.com/playground/VSP6cs27/shared" frameBorder="0" width="100%" height="429" name="VSP6cs27"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `seats`.

* Space Complexity:  $$O(1)$$.



---
#### Approach #3: Group by Zero [Accepted]

**Intuition**

In a group of `K` adjacent empty seats between two people, the answer is `(K+1) / 2`.

**Algorithm**

For each group of `K` empty seats between two people, we can take into account the candidate answer `(K+1) / 2`.

For groups of empty seats between the edge of the row and one other person, the answer is `K`, and we should take into account those answers too.

<iframe src="https://leetcode.com/playground/wKJwsWbr/shared" frameBorder="0" width="100%" height="500" name="wKJwsWbr"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `seats`.

* Space Complexity:  $$O(1)$$.  (In Python, `seats[::-1]` uses $$O(N)$$ space, but this can be remedied.)


---

Analysis written by: [@awice](https://leetcode.com/awice).
