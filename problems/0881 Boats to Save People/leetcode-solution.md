# 0881 - Boats to Save People

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers, Greedy | [Leetcode](https://leetcode.com/problems/boats-to-save-people) | [solution](https://leetcode.com/problems/boats-to-save-people/solution/)


-----------

<p>The <code>i</code>-th person has weight <code>people[i]</code>, and each boat can carry a maximum weight of <code>limit</code>.</p>

<p>Each boat carries at most 2 people at the same time, provided the sum of the&nbsp;weight of those people is at most <code>limit</code>.</p>

<p>Return the minimum number of boats to carry every given person.&nbsp; (It is guaranteed each person can be carried by a boat.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>people = <span id="example-input-1-1">[1,2]</span>, limit = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>1 boat (1, 2)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>people = <span id="example-input-2-1">[3,2,2,1]</span>, limit = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation</strong>: 3 boats (1, 2), (2) and (3)
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>people = <span id="example-input-3-1">[3,5,3,4]</span>, limit = <span id="example-input-3-2">5</span>
<strong>Output: </strong><span id="example-output-3">4</span>
<strong>Explanation</strong>: 4 boats (3), (3), (4), (5)</pre>

<p><strong>Note</strong>:</p>

<ul>
	<li><code>1 &lt;=&nbsp;people.length &lt;= 50000</code></li>
	<li><code>1 &lt;= people[i] &lt;=&nbsp;limit &lt;= 30000</code></li>
</ul>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Greedy (Two Pointer)

**Intuition**

If the heaviest person can share a boat with the lightest person, then do so.  Otherwise, the heaviest person can't pair with anyone, so they get their own boat.

The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.

**Algorithm**

Let `people[i]` to the currently lightest person, and `people[j]` to the heaviest.

Then, as described above, if the heaviest person can share a boat with the lightest person (if `people[j] + people[i] <= limit`) then do so; otherwise, the heaviest person sits in their own boat.

<iframe src="https://leetcode.com/playground/Vy4ovfs7/shared" frameBorder="0" width="100%" height="344" name="Vy4ovfs7"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `people`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
