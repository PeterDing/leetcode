# 0855 - Exam Room

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Ordered Map | [Leetcode](https://leetcode.com/problems/exam-room) | [solution](https://leetcode.com/problems/exam-room/solution/)


-----------

<p>In an exam room, there are <code>N</code> seats in a single row, numbered <code>0, 1, 2, ..., N-1</code>.</p>

<p>When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.&nbsp; If there are multiple such seats, they sit in the seat with the lowest number.&nbsp; (Also, if no one is in the room, then the student sits at seat number 0.)</p>

<p>Return a class <code>ExamRoom(int N)</code>&nbsp;that exposes two functions: <code>ExamRoom.seat()</code>&nbsp;returning an <code>int</code>&nbsp;representing what seat the student sat in, and <code>ExamRoom.leave(int p)</code>&nbsp;representing that the student in seat number <code>p</code>&nbsp;now leaves the room.&nbsp; It is guaranteed that any calls to <code>ExamRoom.leave(p)</code> have a student sitting in seat <code>p</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;ExamRoom&quot;,&quot;seat&quot;,&quot;seat&quot;,&quot;seat&quot;,&quot;seat&quot;,&quot;leave&quot;,&quot;seat&quot;]</span>, <span id="example-input-1-2">[[10],[],[],[],[],[4],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,0,9,4,2,null,5]</span>
<span><strong>Explanation</strong>:
ExamRoom(10) -&gt; null
seat() -&gt; 0, no one is in the room, then the student sits at seat number 0.
seat() -&gt; 9, the student sits at the last seat number 9.
seat() -&gt; 4, the student sits at the last seat number 4.
seat() -&gt; 2, the student sits at the last seat number 2.
leave(4) -&gt; null
seat() -&gt; 5, the student sits at the last seat number 5.</span>
</pre>

<p><span>​​​​​​​</span></p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
	<li><code>ExamRoom.seat()</code> and <code>ExamRoom.leave()</code> will be called at most <code>10^4</code> times across all test cases.</li>
	<li>Calls to <code>ExamRoom.leave(p)</code> are guaranteed to have a student currently sitting in seat number <code>p</code>.</li>
</ol>


-----------


## Similar Problems

- [Easy] [Maximize Distance to Closest Person](maximize-distance-to-closest-person)




## Solution:

[TOC]

---
#### Approach 1: Maintain Sorted Positions

**Intuition**

We'll maintain `ExamRoom.students`, a sorted `list` (or `TreeSet` in Java) of positions the students are currently seated in.

**Algorithm**

The `ExamRoom.leave(p)` operation is clear - we will just `list.remove` (or `TreeSet.remove`) the student from `ExamRoom.students`.

Let's focus on the `ExamRoom.seat() : int` operation.  For each pair of adjacent students `i` and `j`, the maximum distance to the closest student is `d = (j - i) / 2`, achieved in the left-most seat `i + d`.  Otherwise, we could also sit in the left-most seat, or the right-most seat.

Finally, we should handle the case when there are no students separately.

For more details, please review the comments made in the implementations.

<iframe src="https://leetcode.com/playground/9bZc2mLh/shared" frameBorder="0" width="100%" height="500" name="9bZc2mLh"></iframe>

**Complexity Analysis**

* Time Complexity:  Each `seat` operation is $$O(P)$$, (where $$P$$ is the number of students sitting), as we iterate through every student.  Each `leave` operation is $$O(P)$$ ($$\log P$$ in Java).

* Space Complexity:  $$O(P)$$, the space used to store the positions of each student sitting.

---

Analysis written by: [@awice](https://leetcode.com/awice).
