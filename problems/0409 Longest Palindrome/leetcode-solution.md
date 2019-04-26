# 0409 - Longest Palindrome

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table | [Leetcode](https://leetcode.com/problems/longest-palindrome) | [solution](https://leetcode.com/problems/longest-palindrome/solution/)


-----------

<p>Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.</p>

<p>This is case sensitive, for example <code>"Aa"</code> is not considered a palindrome here.</p>

<p><b>Note:</b><br />
Assume the length of given string will not exceed 1,010.
</p>

<p><b>Example: </b>
<pre>
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
</pre>
</p>

-----------


## Similar Problems

- [Easy] [Palindrome Permutation](palindrome-permutation)




## Solution:

[TOC]

#### Approach #1: Greedy [Accepted]

**Intuition**

A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner).  The letter `i` from the left has its partner `i` from the right.  For example in `'abcba'`, `'aa'` and `'bb'` are partners, and `'c'` is a unique center.

Imagine we built our palindrome.  It consists of as many partnered letters as possible, plus a unique center if possible.  This motivates a greedy approach.

**Algorithm**

For each letter, say it occurs `v` times.  We know we have `v // 2 * 2` letters that can be partnered for sure.  For example, if we have `'aaaaa'`, then we could have `'aaaa'` partnered, which is `5 // 2 * 2 = 4` letters partnered.

At the end, if there was any `v % 2 == 1`, then that letter could have been a unique center.  Otherwise, every letter was partnered.  To perform this check, we will check for `v % 2 == 1` and `ans % 2 == 0`, the latter meaning we haven't yet added a unique center to the answer.

<iframe src="https://leetcode.com/playground/ZnPVAdHR/shared" frameBorder="0" width="100%" height="310" name="ZnPVAdHR"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `s`.  We need to count each letter.

* Space Complexity: $$O(1)$$, the space for our count, as the alphabet size of `s` is fixed.  We should also consider that in a bit complexity model, technically we need $$O(\log N)$$ bits to store the count values.

---

Analysis written by: [@awice](https://leetcode.com/awice).
