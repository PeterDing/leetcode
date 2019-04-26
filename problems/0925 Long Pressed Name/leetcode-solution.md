# 0925 - Long Pressed Name

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Two Pointers, String | [Leetcode](https://leetcode.com/problems/long-pressed-name) | [solution](https://leetcode.com/problems/long-pressed-name/solution/)


-----------

<p>Your friend is typing his <code>name</code>&nbsp;into a keyboard.&nbsp; Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code>&nbsp;characters of the keyboard.&nbsp; Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-1-1">&quot;alex&quot;</span>, typed = <span id="example-input-1-2">&quot;aaleex&quot;</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-2-1">&quot;saeed&quot;</span>, typed = <span id="example-input-2-2">&quot;ssaaedd&quot;</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>'e' must have been pressed twice, but it wasn't in the typed output.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-3-1">&quot;leelee&quot;</span>, typed = <span id="example-input-3-2">&quot;lleeelee&quot;</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-4-1">&quot;laiden&quot;</span>, typed = <span id="example-input-4-2">&quot;laiden&quot;</span>
<strong>Output: </strong><span id="example-output-4">true</span>
<strong>Explanation: </strong>It's not necessary to long press any character.
</pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>name.length &lt;= 1000</code></li>
	<li><code>typed.length &lt;= 1000</code></li>
	<li>The characters of <code>name</code> and <code>typed</code> are lowercase letters.</li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Group into Blocks

**Intuition and Algorithm**

For a string like `S = 'aabbbbccc'`, we can group it into blocks `groupify(S) = [('a', 2), ('b', 4), ('c', 3)]`, that consist of a *key* `'abc'` and a *count* `[2, 4, 3]`.

Then, the necessary and sufficient condition for `typed` to be a long-pressed version of `name` is that the keys are the same, and each entry of the count of `typed` is at least the entry for the count of `name`.

For example, `'aaleex'` is a long-pressed version of `'alex'`: because when considering the groups `[('a', 2), ('l', 1), ('e', 2), ('x', 1)]` and `[('a', 1), ('l', 1), ('e', 1), ('x', 1)]`, they both have the key `'alex'`, and the count `[2,1,2,1]` is at least `[1,1,1,1]` when making an element-by-element comparison `(2 >= 1, 1 >= 1, 2 >= 1, 1 >= 1)`.

<iframe src="https://leetcode.com/playground/TfwwqxiQ/shared" frameBorder="0" width="100%" height="500" name="TfwwqxiQ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N+T)$$, where $$N, T$$ are the lengths of `name` and `typed`.

* Space Complexity:  $$O(N+T)$$.
<br />
<br />


---
#### Approach 2: Two Pointer

**Intuition**

As in *Approach 1*, we want to check the key and the count.  We can do this on the fly.

Suppose we read through the characters `name`, and eventually it doesn't match `typed`.

There are some cases for when we are allowed to skip characters of `typed`. Let's use a tuple to denote the case (`name`, `typed`):

* In a case like `('aab', 'aaaaab')`, we can skip the 3rd, 4th, and 5th `'a'` in `typed` because we have already processed an `'a'` in this block.

* In a case like `('a', 'b')`, we can't skip the 1st `'b'` in `typed` because we haven't processed anything in the current block yet.

**Algorithm**

This leads to the following algorithm:

* For each character in `name`, if there's a mismatch with the next character in `typed`:
    * If it's the first character of the block in `typed`, the answer is `False`.
    * Else, discard all similar characers of `typed` coming up.  The next (different) character coming must match.

Also, we'll keep track on the side of whether we are at the first character of the block.

<iframe src="https://leetcode.com/playground/Wv6ufLEV/shared" frameBorder="0" width="100%" height="500" name="Wv6ufLEV"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N+T)$$, where $$N, T$$ are the lengths of `name` and `typed`.

* Space Complexity:  $$O(1)$$ in additional space complexity.  (In Java, `.toCharArray` makes this $$O(N)$$, but this can be easily remedied.)
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
