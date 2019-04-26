# 0868 - Binary Gap

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/binary-gap) | [solution](https://leetcode.com/problems/binary-gap/solution/)


-----------

<p>Given a positive&nbsp;integer <code>N</code>, find and return the longest distance between two consecutive 1&#39;s in the binary representation of <code>N</code>.</p>

<p>If there aren&#39;t two consecutive 1&#39;s, return <font face="monospace">0</font>.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<ul>
</ul>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">22</span>
<strong>Output: </strong>2
<strong>Explanation: </strong>
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1&#39;s.
The first consecutive pair of 1&#39;s have distance 2.
The second consecutive pair of 1&#39;s have distance 1.
The answer is the largest of these two distances, which is 2.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">5</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>
5 in binary is 0b101.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">6</span>
<strong>Output: </strong><span id="example-output-3">1</span>
<strong>Explanation: </strong>
6 in binary is 0b110.
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">8</span>
<strong>Output: </strong><span id="example-output-4">0</span>
<strong>Explanation: </strong>
8 in binary is 0b1000.
There aren&#39;t any consecutive pairs of 1&#39;s in the binary representation of 8, so we return 0.
</pre>

<p>&nbsp;</p>

<div>
<div>
<div>
<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ul>
</div>
</div>
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
#### Approach 1: Store Indexes

**Intuition**

Since we wanted to inspect the distance between consecutive 1s in the binary representation of `N`, let's write down the index of each `1` in that binary representation.  For example, if `N = 22 = 0b10110`, then we'll write `A = [1, 2, 4]`.  This makes it easier to proceed, as now we have a problem about adjacent values in an array.

**Algorithm**

Let's make a list `A` of indices `i` such that `N` has the `i`th bit set.

With this array `A`, finding the maximum distance between consecutive `1`s is much easier: it's the maximum distance between adjacent values of this array.

<iframe src="https://leetcode.com/playground/vjdm4iZG/shared" frameBorder="0" width="100%" height="293" name="vjdm4iZG"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log N)$$.  Note that $$\log N$$ is the number of digits in the binary representation of $$N$$.

* Space Complexity:  $$O(\log N)$$, the space used by `A`.
<br />
<br />


---
#### Approach 2: One Pass

**Intuition**

In *Approach 1*, we created an array `A` of indices `i` for which `N` had the `i`th bit set.

Since we only care about consecutive values of this array `A`, we don't need to store the whole array.  We only need to remember the last value seen.

**Algorithm**

We'll store `last`, the last value added to the *virtual* array `A`.  If `N` has the `i`th bit set, a candidate answer is `i - last`, and then the new last value added to `A` would be `last = i`.

<iframe src="https://leetcode.com/playground/Pae8eWML/shared" frameBorder="0" width="100%" height="276" name="Pae8eWML"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log N)$$.  Note that $$\log N$$ is the number of digits in the binary representation of $$N$$.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
