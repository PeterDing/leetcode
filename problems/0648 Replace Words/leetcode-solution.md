# 0648 - Replace Words

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, Trie | [Leetcode](https://leetcode.com/problems/replace-words) | [solution](https://leetcode.com/problems/replace-words/solution/)


-----------

<p>In English, we have a concept called <code>root</code>, which can be followed by some other words to form another longer word - let&#39;s call this word <code>successor</code>. For example, the root <code>an</code>, followed by <code>other</code>, which can form another word <code>another</code>.</p>

<p>Now, given a dictionary consisting of many roots and a sentence. You need to replace all the <code>successor</code> in the sentence with the <code>root</code> forming it. If a <code>successor</code> has many <code>roots</code> can form it, replace it with the root with the shortest length.</p>

<p>You need to output the sentence after the replacement.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> dict = [&quot;cat&quot;, &quot;bat&quot;, &quot;rat&quot;]
sentence = &quot;the cattle was rattled by the battery&quot;
<b>Output:</b> &quot;the cat was rat by the bat&quot;
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The input will only have lower-case letters.</li>
	<li>1 &lt;= dict words number &lt;= 1000</li>
	<li>1 &lt;= sentence words number &lt;= 1000</li>
	<li>1 &lt;= root length &lt;= 100</li>
	<li>1 &lt;= sentence words length &lt;= 1000</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Implement Trie (Prefix Tree)](implement-trie-prefix-tree)




## Solution:

[TOC]

---
#### Approach #1: Prefix Hash [Accepted]

**Intuition**

For each word in the sentence, we'll look at successive prefixes and see if we saw them before.

**Algorithm**

Store all the `roots` in a *Set* structure.  Then for each word, look at successive prefixes of that word.  If you find a prefix that is a root, replace the word with that prefix.  Otherwise, the prefix will just be the word itself, and we should add that to the final sentence answer.

<iframe src="https://leetcode.com/playground/tvjGGLzd/shared" frameBorder="0" width="100%" height="361" name="tvjGGLzd"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(\sum w_i^2)$$ where $$w_i$$ is the length of the $$i$$-th word.  We might check every prefix, the $$i$$-th of which is $$O(w_i^2)$$ work.

* Space Complexity: $$O(N)$$ where $$N$$ is the length of our sentence; the space used by `rootset`.

---
#### Approach #2: Trie [Accepted]

**Intuition and Algorithm**

Put all the roots in a trie (prefix tree).  Then for any query word, we can find the smallest root that was a prefix in linear time.

<iframe src="https://leetcode.com/playground/5Dt2dcFU/shared" frameBorder="0" width="100%" height="500" name="5Dt2dcFU"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the length of the `sentence`.  Every query of a word is in linear time.

* Space Complexity: $$O(N)$$, the size of our trie.

---

Analysis written by: [@awice](https://leetcode.com/awice).
