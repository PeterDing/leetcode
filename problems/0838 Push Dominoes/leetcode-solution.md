# 0838 - Push Dominoes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers, Dynamic Programming | [Leetcode](https://leetcode.com/problems/push-dominoes) | [solution](https://leetcode.com/problems/push-dominoes/solution/)


-----------

<p>There are<font face="monospace">&nbsp;<code>N</code></font> dominoes in a line, and we place each domino vertically upright.</p>

<p>In the beginning, we simultaneously push&nbsp;some of the dominoes either to the left or to the right.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png" style="height: 160px;" /></p>

<p>After each second, each domino that is falling to the left pushes the adjacent domino on the left.</p>

<p>Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.</p>

<p>When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.</p>

<p>For the purposes of this question, we will consider that a falling domino&nbsp;expends no additional force to a falling or already fallen domino.</p>

<p>Given a string &quot;S&quot; representing the initial state.&nbsp;<code>S[i] = &#39;L&#39;</code>, if the i-th domino has been pushed to the left; <code>S[i] = &#39;R&#39;</code>, if the i-th domino has been pushed to the right; <code>S[i] = &#39;.&#39;</code>,&nbsp;if the <code>i</code>-th domino has not been pushed.</p>

<p>Return a string representing the final state.&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;.L.R...LR..L..&quot;
<strong>Output: </strong>&quot;LL.RR.LLRRLL..&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;RR.L&quot;
<strong>Output: </strong>&quot;RR.L&quot;
<strong>Explanation: </strong>The first domino expends no additional force on the second domino.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= N&nbsp;&lt;= 10^5</code></li>
	<li>String&nbsp;<code>dominoes</code> contains only&nbsp;<code>&#39;L</code>&#39;, <code>&#39;R&#39;</code> and <code>&#39;.&#39;</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Adjacent Symbols [Accepted]

**Intuition**

Between every group of vertical dominoes (`'.'`), we have up to two non-vertical dominoes bordering this group.  Since additional dominoes outside this group do not affect the outcome, we can analyze these situations individually: there are 9 of them (as the border could be empty). Actually, if we border the dominoes by `'L'` and `'R'`, there are only 4 cases.  We'll write new letters between these symbols depending on each case.

**Algorithm**

Continuing our explanation, we analyze cases:

* If we have say `"A....B"`, where A = B, then we should write `"AAAAAA"`.

* If we have `"R....L"`, then we will write `"RRRLLL"`, or `"RRR.LLL"` if we have an odd number of dots.  If the initial symbols are at positions `i` and `j`, we can check our distance `k-i` and `j-k` to decide at position `k` whether to write `'L'`, `'R'`, or `'.'`.

* (If we have `"L....R"` we don't do anything.  We can skip this case.)

<iframe src="https://leetcode.com/playground/X63wt96u/shared" frameBorder="0" width="100%" height="500" name="X63wt96u"></iframe>

**Complexity Analysis**

* Time and Space Complexity:  $$O(N)$$, where $$N$$ is the length of `dominoes`.

---
#### Approach #2: Calculate Force [Accepted]

**Intuition**

We can calculate the net force applied on every domino.  The forces we care about are how close a domino is to a leftward `'R'`, and to a rightward `'L'`: the closer we are, the stronger the force.

**Algorithm**

Scanning from left to right, our force decays by 1 every iteration, and resets to `N` if we meet an `'R'`, so that `force[i]` is higher (than `force[j]`) if and only if `dominoes[i]` is closer (looking leftward) to `'R'` (than `dominoes[j]`).

Similarly, scanning from right to left, we can find the force going rightward (closeness to `'L'`).

For some domino `answer[i]`, if the forces are equal, then the answer is `'.'`.  Otherwise, the answer is implied by whichever force is stronger.

**Example**

Here is a worked example on the string `S = 'R.R...L'`:  We find the force going from left to right is `[7, 6, 7, 6, 5, 4, 0]`.  The force going from right to left is `[0, 0, 0, -4, -5, -6, -7]`.  Combining them (taking their vector addition), the combined force is `[7, 6, 7, 2, 0, -2, -7]`, for a final answer of `RRRR.LL`.

<iframe src="https://leetcode.com/playground/xrAD5knD/shared" frameBorder="0" width="100%" height="500" name="xrAD5knD"></iframe>

**Complexity Analysis**

* Time and Space Complexity:  $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
