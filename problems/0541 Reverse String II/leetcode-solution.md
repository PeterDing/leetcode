# 0541 - Reverse String II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/reverse-string-ii) | [solution](https://leetcode.com/problems/reverse-string-ii/solution/)


-----------

</p>
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> s = "abcdefg", k = 2
<b>Output:</b> "bacdfeg"
</pre>
</p>

<b>Restrictions:</b> </b>
<ol>
<li> The string consists of lower English letters only.</li>
<li> Length of the given string and k will in the range [1, 10000]</li>
</ol>

-----------


## Similar Problems

- [Easy] [Reverse String](reverse-string)

- [Easy] [Reverse Words in a String III](reverse-words-in-a-string-iii)




## Solution:

[TOC]

---
#### Approach #1: Direct [Accepted]

**Intuition and Algorithm**

We will reverse each block of `2k` characters directly.

Each block starts at a multiple of `2k`: for example, `0, 2k, 4k, 6k, ...`.  One thing to be careful about is we may not reverse each block if there aren't enough characters.

To reverse a block of characters from `i` to `j`, we can swap characters in positions `i++` and `j--`.

<iframe src="https://leetcode.com/playground/2qnQN5xs/shared" frameBorder="0" width="100%" height="293" name="2qnQN5xs"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the size of `s`.  We build a helper array, plus reverse about half the characters in `s`.

* Space Complexity: $$O(N)$$, the size of `a`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
