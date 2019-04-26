# 0820 - Short Encoding of Words

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/short-encoding-of-words) | [solution](https://leetcode.com/problems/short-encoding-of-words/solution/)


-----------

<p>Given a list of words, we may encode it by writing a reference string <code>S</code> and a list of indexes <code>A</code>.</p>

<p>For example, if the list of words is <code>[&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]</code>, we can write it as <code>S = &quot;time#bell#&quot;</code>&nbsp;and <code>indexes = [0, 2, 5]</code>.</p>

<p>Then for each index, we will recover the word by reading from the reference string from that index until we reach a <code>&quot;#&quot;</code> character.</p>

<p>What is the length of the shortest reference string S possible that encodes the given words?</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> words = <code>[&quot;time&quot;, &quot;me&quot;, &quot;bell&quot;]</code>
<strong>Output:</strong> 10
<strong>Explanation:</strong> S = <code>&quot;time#bell#&quot; and indexes = [0, 2, 5</code>].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= words.length&nbsp;&lt;= 2000</code>.</li>
	<li><code>1 &lt;=&nbsp;words[i].length&nbsp;&lt;= 7</code>.</li>
	<li>Each word&nbsp;has only&nbsp;lowercase letters.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Store Prefixes [Accepted]

**Intuition**

If a word `X` is a suffix of `Y`, then it does not need to be considered, as the encoding of `Y` in the reference string will also encode `X`.  For example, if `"me"` and `"time"` is in `words`, we can throw out `"me"` without changing the answer.

If a word `Y` does not have any other word `X` (in the list of `words`) that is a suffix of `Y`, then `Y` must be part of the reference string.

Thus, the goal is to remove words from the list such that no word is a suffix of another.  The final answer would be `sum(word.length + 1 for word in words)`.

**Algorithm**

Since a word only has up to 7 suffixes (as `words[i].length <= 7`), let's iterate over all of them.  For each suffix, we'll try to remove it from our `words` list.  For efficiency, we'll make `words` a set.

<iframe src="https://leetcode.com/playground/gV8UXxb3/shared" frameBorder="0" width="100%" height="293" name="gV8UXxb3"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\sum w_i^2)$$, where $$w_i$$ is the length of `words[i]`.

* Space Complexity: $$O(\sum w_i)$$, the space used in storing suffixes.

---
#### Approach #2: Trie [Accepted]

**Intuition**

As in *Approach #1*, the goal is to remove words that are suffixes of another word in the list.

**Algorithm**

To find whether different words have the same suffix, let's put them backwards into a trie (prefix tree).  For example, if we have `"time"` and `"me"`, we will put `"emit"` and `"em"` into our trie.

After, the leaves of this trie (nodes with no children) represent words that have no suffix, and we will count `sum(word.length + 1 for word in words)`.

<iframe src="https://leetcode.com/playground/whsBS94T/shared" frameBorder="0" width="100%" height="500" name="whsBS94T"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\sum w_i)$$, where $$w_i$$ is the length of `words[i]`.

* Space Complexity: $$O(\sum w_i)$$, the space used by the trie.

---

Analysis written by: [@awice](https://leetcode.com/awice).
