# 0911 - Online Election

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Binary Search | [Leetcode](https://leetcode.com/problems/online-election) | [solution](https://leetcode.com/problems/online-election/solution/)


-----------

<p>In an election, the <code>i</code>-th&nbsp;vote was cast for <code>persons[i]</code> at time <code>times[i]</code>.</p>

<p>Now, we would like to implement the following query function: <code>TopVotedCandidate.q(int t)</code> will return the number of the person that was leading the election at time <code>t</code>.&nbsp;&nbsp;</p>

<p>Votes cast at time <code>t</code> will count towards our query.&nbsp; In the case of a tie, the most recent vote (among tied candidates) wins.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;TopVotedCandidate&quot;,&quot;q&quot;,&quot;q&quot;,&quot;q&quot;,&quot;q&quot;,&quot;q&quot;,&quot;q&quot;]</span>, <span id="example-input-1-2">[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]</span>
<strong>Output: </strong><span id="example-output-1">[null,0,1,1,0,0,1]</span>
<strong>Explanation: </strong>
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= persons.length = times.length &lt;= 5000</code></li>
	<li><code>0 &lt;= persons[i] &lt;= persons.length</code></li>
	<li><code>times</code>&nbsp;is a strictly increasing array with all elements in <code>[0, 10^9]</code>.</li>
	<li><code>TopVotedCandidate.q</code> is called at most <code>10000</code> times per test case.</li>
	<li><code>TopVotedCandidate.q(int t)</code> is always called with <code>t &gt;= times[0]</code>.</li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: List of Lists + Binary Search

**Intuition and Algorithm**

We can store the votes in a list `A` of lists of votes.  Each vote has a person and a timestamp, and `A[count]` is a list of the `count`-th votes received for that person.

Then, `A[i][0]` and `A[i]` are monotone increasing, so we can binary search on them to find the most recent vote by time.

<iframe src="https://leetcode.com/playground/vXWSxDmZ/shared" frameBorder="0" width="100%" height="500" name="vXWSxDmZ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + Q \log^2 N)$$, where $$N$$ is the number of votes, and $$Q$$ is the number of queries.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Precomputed Answer + Binary Search

**Intuition and Algorithm**

As the votes come in, we can remember every event `(winner, time)` when the winner changes.  After, we have a sorted list of these events that we can binary search for the answer.

<iframe src="https://leetcode.com/playground/fWa6yR8V/shared" frameBorder="0" width="100%" height="500" name="fWa6yR8V"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + Q \log N)$$, where $$N$$ is the number of votes, and $$Q$$ is the number of queries.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
