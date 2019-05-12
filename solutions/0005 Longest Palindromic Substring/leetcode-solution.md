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




## Solution:

[TOC]

## Summary
This article is for intermediate readers. It introduces the following ideas:
Palindrome, Dynamic Programming and String Manipulation. Make sure you understand what a palindrome means. A palindrome is a string which reads the same in both directions. For example, $$S$$ = "aba" is a palindrome, $$S$$ = "abc" is not.

## Solution
---
#### Approach 1: Longest Common Substring

**Common mistake**

Some people will be tempted to come up with a quick solution, which is unfortunately flawed (however can be corrected easily):

> Reverse $$S$$ and become $$S'$$. Find the longest common substring between $$S$$ and $$S'$$, which must also be the longest palindromic substring.

This seemed to work, let’s see some examples below.

For example, $$S$$ = "caba", $$S'$$ = "abac".

The longest common substring between $$S$$ and $$S'$$ is "aba", which is the answer.

Let’s try another example: $$S$$ = "abacdfgdcaba", $$S'$$ = "abacdgfdcaba".

The longest common substring between $$S$$ and $$S'$$ is "abacd". Clearly, this is not a valid palindrome.

**Algorithm**

We could see that the longest common substring method fails when there exists a reversed copy of a non-palindromic substring in some other part of $$S$$. To rectify this, each time we find a longest common substring candidate, we check if the substring’s indices are the same as the reversed substring’s original indices. If it is, then we attempt to update the longest palindrome found so far; if not, we skip this and find the next candidate.

This gives us an $$O(n^2)$$ Dynamic Programming solution which uses $$O(n^2)$$ space (could be improved to use $$O(n)$$ space). Please read more about Longest Common Substring [here](http://en.wikipedia.org/wiki/Longest_common_substring).
<br />
<br />

---
#### Approach 2: Brute Force

The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.

**Complexity Analysis**

* Time complexity : $$O(n^3)$$.
Assume that $$n$$ is the length of the input string, there are a total of $$\binom{n}{2} = \frac{n(n-1)}{2}$$ such substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes $$O(n)$$ time, the run time complexity is $$O(n^3)$$.

* Space complexity : $$O(1)$$.
<br />
<br />

---
#### Approach 3: Dynamic Programming

To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

We define $$P(i,j)$$ as following:

$$
P(i,j) =
     \begin{cases}
       \text{true,} &\quad\text{if the substring } S_i \dots S_j \text{ is a palindrome}\\
       \text{false,} &\quad\text{otherwise.} \
     \end{cases}
$$

Therefore,

$$
P(i, j) = ( P(i+1, j-1) \text{ and } S_i == S_j )
$$

The base cases are:

$$
P(i, i) = true
$$

$$
P(i, i+1) = ( S_i == S_{i+1} )
$$

This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...


**Complexity Analysis**

* Time complexity : $$O(n^2)$$.
This gives us a runtime complexity of $$O(n^2)$$.

* Space complexity : $$O(n^2)$$.
It uses $$O(n^2)$$ space to store the table.

**Additional Exercise**

Could you improve the above space complexity further and how?
<br />
<br />

---
#### Approach 4: Expand Around Center

In fact, we could solve it in $$O(n^2)$$ time using only constant space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only $$2n - 1$$ such centers.

You might be asking why there are $$2n - 1$$ but not $$n$$ centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.

<iframe src="https://leetcode.com/playground/5w5ZZtTd/shared" frameBorder="0" width="100%" height="446" name="5w5ZZtTd"></iframe>


**Complexity Analysis**

* Time complexity : $$O(n^2)$$.
Since expanding a palindrome around its center could take $$O(n)$$ time, the overall complexity is $$O(n^2)$$.

* Space complexity : $$O(1)$$.
<br />
<br />
---

#### Approach 5: Manacher's Algorithm

There is even an $$O(n)$$ algorithm called Manacher's algorithm, explained [here in detail](http://articles.leetcode.com/longest-palindromic-substring-part-ii/). However, it is a non-trivial algorithm, and no one expects you to come up with this algorithm in a 45 minutes coding session. But, please go ahead and understand it, I promise it will be a lot of fun.
