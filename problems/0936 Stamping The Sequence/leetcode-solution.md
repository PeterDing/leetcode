# 0936 - Stamping The Sequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | String, Greedy | [Leetcode](https://leetcode.com/problems/stamping-the-sequence) | [solution](https://leetcode.com/problems/stamping-the-sequence/solution/)


-----------

<p>You want to form a <code>target</code>&nbsp;string of <strong>lowercase letters</strong>.</p>

<p>At the beginning, your sequence is <code>target.length</code>&nbsp;<code>&#39;?&#39;</code> marks.&nbsp; You also have a <code>stamp</code>&nbsp;of lowercase letters.</p>

<p>On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.&nbsp; You can make up to <code>10 * target.length</code> turns.</p>

<p>For example, if the initial sequence is <font face="monospace">&quot;?????&quot;</font>, and your stamp is <code>&quot;abc&quot;</code>,&nbsp; then you may make <font face="monospace">&quot;abc??&quot;, &quot;?abc?&quot;, &quot;??abc&quot;&nbsp;</font>in the first turn.&nbsp; (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)</p>

<p>If the sequence is possible to stamp, then return an array of&nbsp;the index of the left-most letter being stamped at each turn.&nbsp; If the sequence is not possible to stamp, return an empty array.</p>

<p>For example, if the sequence is <font face="monospace">&quot;ababc&quot;</font>, and the stamp is <code>&quot;abc&quot;</code>, then we could return the answer <code>[0, 2]</code>, corresponding to the moves <font face="monospace">&quot;?????&quot; -&gt; &quot;abc??&quot; -&gt; &quot;ababc&quot;</font>.</p>

<p>Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within <code>10 * target.length</code>&nbsp;moves.&nbsp; Any answers specifying more than this number of moves&nbsp;will not be accepted.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>stamp = <span id="example-input-1-1">&quot;abc&quot;</span>, target = <span id="example-input-1-2">&quot;ababc&quot;</span>
<strong>Output: </strong><span id="example-output-1">[0,2]</span>
([1,0,2] would also be accepted as an answer, as well as some other answers.)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>stamp = <span id="example-input-2-1">&quot;</span><span id="example-input-2-2">abca</span><span>&quot;</span>, target = <span id="example-input-2-2">&quot;</span><span>aabcaca&quot;</span>
<strong>Output: </strong><span id="example-output-2">[3,0,1]</span>
</pre>

<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>
</div>
</div>

<ol>
	<li><code>1 &lt;= stamp.length &lt;= target.length &lt;= 1000</code></li>
	<li><code>stamp</code> and <code>target</code> only contain lowercase letters.</li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Work Backwards

**Intuition**

Imagine we stamped the sequence with moves $$m_1, m_2, \cdots$$.  Now, from the final position `target`, we will make those moves in reverse order.  

Let's call the `i`th *window*, a subarray of `target` of length `stamp.length` that starts at `i`.  Each move at position `i` is possible if the `i`th window matches the stamp.  After, every character in the window becomes a wildcard that can match any character in the stamp.

For example, say we have `stamp = "abca"` and `target = "aabcaca"`.  Working backwards, we will reverse stamp at window `1` to get `"a????ca"`, then reverse stamp at window `3` to get `"a??????"`, and finally reverse stamp at position `0` to get `"???????"`.

**Algorithm**

Let's keep track of every window.  We want to know how many cells initially match the stamp (our "`made`" list), and which ones don't (our `"todo"` list).  Any windows that are ready (ie. have no todo list), get enqueued.

Specifically, we enqueue the positions of each character.  (To save time, we enqueue by character, not by window.)  This represents that the character is ready to turn into a `"?"` in our working `target` string.

Now, how to process characters in our queue?  For each character, let's look at all the windows that intersect it, and update their todo lists.  If any todo lists become empty in this manner `(window.todo is empty)`, then we enqueue the characters in `window.made` that we haven't processed yet.

<iframe src="https://leetcode.com/playground/fePTAdQw/shared" frameBorder="0" width="100%" height="500" name="fePTAdQw"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N(N-M))$$, where $$M, N$$ are the lengths of `stamp`, `target`.

* Space Complexity:  $$O(N(N-M))$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
