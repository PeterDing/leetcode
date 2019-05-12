# 0005 - Longest Palindromic Substring

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String, Dynamic Programming | [Leetcode](https://leetcode.com/problems/longest-palindromic-substring) | [solution](https://leetcode.com/problems/longest-palindromic-substring/solution/)

-----------

<p>Given a string <strong>s</strong>, find the longest palindromic substring in <strong>s</strong>. You may assume that the maximum length of <strong>s</strong> is 1000.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Note:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>


-----------


## Similar Problems

- [Hard] [Shortest Palindrome](shortest-palindrome)

- [Easy] [Palindrome Permutation](palindrome-permutation)

- [Hard] [Palindrome Pairs](palindrome-pairs)

- [Medium] [Longest Palindromic Subsequence](longest-palindromic-subsequence)

- [Medium] [Palindromic Substrings](palindromic-substrings)




## Thought:

Dynamic progamming is based on recursion.

For recursion, we find the first completed process for the problem.

Secondly, we use the solution to apply the next process.

For DP, we need previous result to solve next result.



The Solution is Following:

```
1. xabcdeffedcbayabcdeffedcba
         |    |
         p1   p2
         cmp p2, p2 - 2(p2 - p1)
2. xabcdeffedcbayabcdeffedcba
                      |
                      p1 stored at p1 == p1 + 1
```

$O(n)$

