# 0890 - Find and Replace Pattern

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/find-and-replace-pattern) | [solution](https://leetcode.com/problems/find-and-replace-pattern/solution/)


-----------

<p>You have a list of&nbsp;<code>words</code> and a <code>pattern</code>, and you want to know which words in <code>words</code> matches the pattern.</p>

<p>A word matches the pattern if there exists a permutation of letters <code>p</code> so that after replacing every letter <code>x</code> in the pattern with <code>p(x)</code>, we get the desired word.</p>

<p>(<em>Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.</em>)</p>

<p>Return a list of the words in <code>words</code>&nbsp;that match the given pattern.&nbsp;</p>

<p>You may return the answer in any order.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>words = <span id="example-input-1-1">[&quot;abc&quot;,&quot;deq&quot;,&quot;mee&quot;,&quot;aqq&quot;,&quot;dkd&quot;,&quot;ccc&quot;]</span>, pattern = <span id="example-input-1-2">&quot;abb&quot;</span>
<strong>Output: </strong><span id="example-output-1">[&quot;mee&quot;,&quot;aqq&quot;]</span>
<strong><span>Explanation: </span></strong>&quot;mee&quot; matches the pattern because there is a permutation {a -&gt; m, b -&gt; e, ...}. 
&quot;ccc&quot; does not match the pattern because {a -&gt; c, b -&gt; c, ...} is not a permutation,
since a and b map to the same letter.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>1 &lt;= pattern.length = words[i].length&nbsp;&lt;= 20</code></li>
</ul>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Two Maps

**Intuition and Algorithm**

If say, the first letter of the pattern is `"a"`, and the first letter of the word is `"x"`, then in the permutation, `"a"` must map to `"x"`.

We can write this bijection using two maps: a forward map $$\text{m1}$$ and a backwards map $$\text{m2}$$.

$$
\text{m1} : \text{"a"} \rightarrow \text{"x"}
$$
$$
\text{m2} : \text{"x"} \rightarrow \text{"a"}
$$

Then, if there is a contradiction later, we can catch it via one of the two maps.  For example, if the `(word, pattern)` is `("aa", "xy")`, we will catch the mistake in $$\text{m1}$$ (namely, $$\text{m1}(\text{"a"}) = \text{"x"} = \text{"y"}$$).  Similarly, with `(word, pattern) = ("ab", "xx")`, we will catch the mistake in $$\text{m2}$$.

<iframe src="https://leetcode.com/playground/9TL6xVWm/shared" frameBorder="0" width="100%" height="480" name="9TL6xVWm"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * K)$$, where $$N$$ is the number of words, and $$K$$ is the length of each word.

* Space Complexity:  $$O(N * K)$$, the space used by the answer.
<br />
<br />


---
#### Approach 2: One Map

**Intuition and Algorithm**

As in *Approach 1*, we can have some forward map $$\text{m1} : \mathbb{L} \rightarrow \mathbb{L}$$, where $$\mathbb{L}$$ is the set of letters.  

However, instead of keeping track of the reverse map $$\text{m2}$$, we could simply make sure that every value $$\text{m1}(x)$$ in the codomain is reached at most once.  This would guarantee the desired permutation exists.

So our algorithm is this: after defining $$\text{m1}(x)$$ in the same way as *Approach 1* (the forward map of the permutation), afterwards we make sure it reaches distinct values.

<iframe src="https://leetcode.com/playground/3vbeWuoq/shared" frameBorder="0" width="100%" height="497" name="3vbeWuoq"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * K)$$, where $$N$$ is the number of words, and $$K$$ is the length of each word.

* Space Complexity:  $$O(N * K)$$, the space used by the answer.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
