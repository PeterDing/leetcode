# 0010 - Regular Expression Matching

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | String, Dynamic Programming, Backtracking | [Leetcode](https://leetcode.com/problems/regular-expression-matching) | [solution](https://leetcode.com/problems/regular-expression-matching/solution/)


-----------

<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement regular expression matching with support for <code>&#39;.&#39;</code> and <code>&#39;*&#39;</code>.</p>

<pre>
&#39;.&#39; Matches any single character.
&#39;*&#39; Matches zero or more of the preceding element.
</pre>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>s</code>&nbsp;could be empty and contains only lowercase letters <code>a-z</code>.</li>
	<li><code>p</code> could be empty and contains only lowercase letters <code>a-z</code>, and characters like&nbsp;<code>.</code>&nbsp;or&nbsp;<code>*</code>.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; means zero or more of the precedeng&nbsp;element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;ab&quot;
p = &quot;.*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aab&quot;
p = &quot;c*a*b&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;c can be repeated 0 times, a can be repeated 1 time. Therefore it matches &quot;aab&quot;.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;mississippi&quot;
p = &quot;mis*is*p*.&quot;
<strong>Output:</strong> false
</pre>


-----------


## Similar Problems

- [Hard] [Wildcard Matching](wildcard-matching)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Recursion

**Intuition**

If there were no Kleene stars (the `*` wildcard character for regular expressions), the problem would be easier - we simply check from left to right if each character of the text matches the pattern.

When a star is present, we may need to check many different suffixes of the text and see if they match the rest of the pattern.  A recursive solution is a straightforward way to represent this relationship.

**Algorithm**

Without a Kleene star, our solution would look like this:


<iframe src="https://leetcode.com/playground/Z2XSmAHG/shared" frameBorder="0" width="100%" height="123" name="Z2XSmAHG"></iframe>

If a star is present in the pattern, it will be in the second position $$\text{pattern[1]}$$.  Then, we may ignore this part of the pattern, or delete a matching character in the text.  If we have a match on the remaining strings after any of these operations, then the initial inputs matched.

<iframe src="https://leetcode.com/playground/EX8cYcs3/shared" frameBorder="0" width="100%" height="293" name="EX8cYcs3"></iframe>

**Complexity Analysis**

* Time Complexity: Let $$T, P$$ be the lengths of the text and the pattern respectively.  In the worst case, a call to `match(text[i:], pattern[2j:])` will be made $$\binom{i+j}{i}$$ times, and strings of the order $$O(T - i)$$ and $$O(P - 2*j)$$ will be made.  Thus, the complexity has the order $$\sum_{i = 0}^T \sum_{j = 0}^{P/2} \binom{i+j}{i} O(T+P-i-2j)$$.  With some effort outside the scope of this article, we can show this is bounded by $$O\big((T+P)2^{T + \frac{P}{2}}\big)$$.

* Space Complexity:  For every call to `match`, we will create those strings as described above, possibly creating duplicates.  If memory is not freed, this will also take a total of $$O\big((T+P)2^{T + \frac{P}{2}}\big)$$ space, even though there are only order $$O(T^2 + P^2)$$ unique suffixes of $$P$$ and  $$T$$ that are actually required.
<br />
<br />
---
#### Approach 2: Dynamic Programming

**Intuition**

As the problem has an **optimal substructure**, it is natural to cache intermediate results.  We ask the question $$\text{dp(i, j)}$$: does $$\text{text[i:]}$$ and $$\text{pattern[j:]}$$ match?  We can describe our answer in terms of answers to questions involving smaller strings.

**Algorithm**

We proceed with the same recursion as in [Approach 1](#approach-1-recursion), except because calls will only ever be made to `match(text[i:], pattern[j:])`, we use $$\text{dp(i, j)}$$ to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.


*Top-Down Variation*
<iframe src="https://leetcode.com/playground/Fpg6LXEX/shared" frameBorder="0" width="100%" height="500" name="Fpg6LXEX"></iframe>

*Bottom-Up Variation*

<iframe src="https://leetcode.com/playground/dmAyPDG3/shared" frameBorder="0" width="100%" height="395" name="dmAyPDG3"></iframe>

**Complexity Analysis**

* Time Complexity: Let $$T, P$$ be the lengths of the text and the pattern respectively.  The work for every call to `dp(i, j)` for $$i=0, ... ,T$$; $$j=0, ... ,P$$ is done once, and it is $$O(1)$$ work.  Hence, the time complexity is $$O(TP)$$.

* Space Complexity:  The only memory we use is the $$O(TP)$$ boolean entries in our cache.  Hence, the space complexity is $$O(TP)$$.
