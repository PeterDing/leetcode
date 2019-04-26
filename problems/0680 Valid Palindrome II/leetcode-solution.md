# 0680 - Valid Palindrome II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/valid-palindrome-ii) | [solution](https://leetcode.com/problems/valid-palindrome-ii/solution/)


-----------

<p>
Given a non-empty string <code>s</code>, you may delete <b>at most</b> one character.  Judge whether you can make it a palindrome.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aba"
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "abca"
<b>Output:</b> True
<b>Explanation:</b> You could delete the character 'c'.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.</li>
</ol>
</p>

-----------


## Similar Problems

- [Easy] [Valid Palindrome](valid-palindrome)




## Solution:

[TOC]

#### Approach #1: Brute Force [Time Limit Exceeded]

**Intuition and Algorithm**

For each index `i` in the given string, let's remove that character, then check if the resulting string is a palindrome.  If it is, (or if the original string was a palindrome), then we'll return `true`

<iframe src="https://leetcode.com/playground/F8rXiMNb/shared" frameBorder="0" name="F8rXiMNb" width="100%" height="394"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$ where $$N$$ is the length of the string.  We do the following $$N$$ times: create a string of length $$N$$ and iterate over it.

* Space Complexity: $$O(N)$$, the space used by our candidate answer.

---
#### Approach #2: Greedy [Accepted]

**Intuition**

If the beginning and end characters of a string are the same (ie. `s[0] == s[s.length - 1]`), then whether the inner characters are a palindrome (`s[1], s[2], ..., s[s.length - 2]`) uniquely determines whether the entire string is a palindrome.

**Algorithm**

Suppose we want to know whether `s[i], s[i+1], ..., s[j]` form a palindrome.  If `i >= j` then we are done.  If `s[i] == s[j]` then we may take `i++; j--`.  Otherwise, the palindrome must be either `s[i+1], s[i+2],  ..., s[j]` or `s[i], s[i+1], ..., s[j-1]`, and we should check both cases.

<iframe src="https://leetcode.com/playground/46SiEhrv/shared" frameBorder="0" name="46SiEhrv" width="100%" height="360"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the length of the string.  Each of two checks of whether some substring is a palindrome is $$O(N)$$.

* Space Complexity: $$O(1)$$ additional complexity.  Only pointers were stored in memory.

---

Analysis written by: [@awice](https://leetcode.com/awice)
