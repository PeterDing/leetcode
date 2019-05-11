# 0916 - Word Subsets

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/word-subsets) | [solution](https://leetcode.com/problems/word-subsets/solution/)


-----------

<p>We are given two arrays <code>A</code> and <code>B</code> of words.&nbsp; Each word is a string of lowercase letters.</p>

<p>Now, say that&nbsp;word <code>b</code> is a subset of word <code>a</code><strong>&nbsp;</strong>if every letter in <code>b</code> occurs in <code>a</code>, <strong>including multiplicity</strong>.&nbsp; For example, <code>&quot;wrr&quot;</code> is a subset of <code>&quot;warrior&quot;</code>, but is not a subset of <code>&quot;world&quot;</code>.</p>

<p>Now say a word <code>a</code> from <code>A</code> is <em>universal</em> if for every <code>b</code> in <code>B</code>, <code>b</code>&nbsp;is a subset of <code>a</code>.&nbsp;</p>

<p>Return a list of all universal words in <code>A</code>.&nbsp; You can return the words in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-1-2">[&quot;e&quot;,&quot;o&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-2-2">[&quot;l&quot;,&quot;e&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[&quot;apple&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-3-2">[&quot;e&quot;,&quot;oo&quot;]</span>
<strong>Output: </strong><span id="example-output-3">[&quot;facebook&quot;,&quot;google&quot;]</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-4-2">[&quot;lo&quot;,&quot;eo&quot;]</span>
<strong>Output: </strong><span id="example-output-4">[&quot;google&quot;,&quot;leetcode&quot;]</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-5-1">[&quot;amazon&quot;,&quot;apple&quot;,&quot;facebook&quot;,&quot;google&quot;,&quot;leetcode&quot;]</span>, B = <span id="example-input-5-2">[&quot;ec&quot;,&quot;oc&quot;,&quot;ceo&quot;]</span>
<strong>Output: </strong><span id="example-output-5">[&quot;facebook&quot;,&quot;leetcode&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length, B.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i].length, B[i].length&nbsp;&lt;= 10</code></li>
	<li><code>A[i]</code> and <code>B[i]</code> consist only of lowercase letters.</li>
	<li>All words in <code>A[i]</code> are unique: there isn&#39;t <code>i != j</code> with <code>A[i] == A[j]</code>.</li>
</ol>
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
#### Approach 1: Reduce to Single Word in B

**Intuition**

If `b` is a subset of `a`, then say `a` is a superset of `b`.  Also, say $$N_{\text{"a"}}(\text{word})$$ is the count of the number of $$\text{"a"}$$'s in the word.

When we check whether a word `wordA` in `A` is a superset of `wordB`, we are individually checking the counts of letters: that for each $$\text{letter}$$, we have $$N_{\text{letter}}(\text{wordA}) \geq N_{\text{letter}}(\text{wordB})$$.

Now, if we check whether a word `wordA` is a superset of all words $$\text{wordB}_i$$, we will check for each letter and each $$i$$, that $$N_{\text{letter}}(\text{wordA}) \geq N_{\text{letter}}(\text{wordB}_i)$$.  This is the same as checking $$N_{\text{letter}}(\text{wordA}) \geq \max\limits_i(N_{\text{letter}}(\text{wordB}_i))$$.

For example, when checking whether `"warrior"` is a superset of words `B = ["wrr", "wa", "or"]`,  we can combine these words in `B` to form a "maximum" word `"arrow"`, that has the maximum count of every letter in each word in `B`.

**Algorithm**

Reduce `B` to a single word `bmax` as described above, then compare the counts of letters between words `a` in `A`, and `bmax`.

<iframe src="https://leetcode.com/playground/arU2pN5v/shared" frameBorder="0" width="100%" height="500" name="arU2pN5v"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\mathcal{A} + \mathcal{B})$$, where $$\mathcal{A}$$ and $$\mathcal{B}$$ is the total amount of information in `A` and `B` respectively.

* Space Complexity:  $$O(A\text{.length} + B\text{.length})$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).