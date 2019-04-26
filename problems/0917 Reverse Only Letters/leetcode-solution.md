# 0917 - Reverse Only Letters

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/reverse-only-letters) | [solution](https://leetcode.com/problems/reverse-only-letters/solution/)


-----------

<p>Given a string <code>S</code>, return the &quot;reversed&quot; string where all characters that are not a letter&nbsp;stay in the same place, and all letters reverse their positions.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;ab-cd&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;dc-ba&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;a-bC-dEf-ghIj&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;j-Ih-gfE-dCba&quot;</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;Test1ng-Leet=code-Q!&quot;</span>
<strong>Output: </strong><span id="example-output-3">&quot;Qedo1ct-eeLg=ntse-T!&quot;</span>
</pre>

<p>&nbsp;</p>

<div>
<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>S.length &lt;= 100</code></li>
	<li><code>33 &lt;= S[i].ASCIIcode &lt;= 122</code>&nbsp;</li>
	<li><code>S</code> doesn&#39;t contain <code>\</code> or <code>&quot;</code></li>
</ol>
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
#### Approach 1: Stack of Letters

**Intuition and Algorithm**

Collect the letters of `S` separately into a stack, so that popping the stack reverses the letters.  (Alternatively, we could have collected the letters into an array and reversed the array.)

Then, when writing the characters of `S`, any time we need a letter, we use the one we have prepared instead.

<iframe src="https://leetcode.com/playground/2S2yvnpZ/shared" frameBorder="0" width="100%" height="361" name="2S2yvnpZ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Reverse Pointer

**Intuition**

Write the characters of `S` one by one.  When we encounter a letter, we want to write the next letter that occurs if we iterated through the string backwards.

So we do just that: keep track of a pointer `j` that iterates through the string backwards.  When we need to write a letter, we use it.

<iframe src="https://leetcode.com/playground/2RFgNCou/shared" frameBorder="0" width="100%" height="344" name="2RFgNCou"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
