# 0521 - Longest Uncommon Subsequence I 

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/longest-uncommon-subsequence-i) | [solution](https://leetcode.com/problems/longest-uncommon-subsequence-i/solution/)


-----------

<p>
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be <b>any</b> subsequence of the other strings.
</p>

<p>
A <b>subsequence</b> is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
</p>

<p>
The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aba", "cdc"
<b>Output:</b> 3
<b>Explanation:</b> The longest uncommon subsequence is "aba" (or "cdc"), <br/>because "aba" is a subsequence of "aba", <br/>but not a subsequence of any other strings in the group of two strings. 
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>Both strings' lengths will not exceed 100.</li>
<li>Only letters from a ~ z will appear in input strings. </li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Longest Uncommon Subsequence II](longest-uncommon-subsequence-ii)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

In the brute force approach we will generate all the possible $$2^n$$ subsequences of both the strings and store their number of occurences in a hashmap.
Longest subsequence whose frequency is equal to $$1$$ will be the required subsequence.
And, if it is not found we will return $$-1$$.


<iframe src="https://leetcode.com/playground/tSXGPoqU/shared" frameBorder="0" name="tSXGPoqU" width="100%" height="479"></iframe>

**Complexity Analysis**

* Time complexity : $$O(2^x+2^y)$$. where $$x$$ and $$y$$ are the lengths of strings $$a$$ and $$b$$ respectively . Number of subsequences will be $$2^x+2^y$$.
* Space complexity : $$O(2^x+2^y)$$. $$2^x+2^y$$ subsequences will be generated.

---
#### Approach #2 Simple Solution[Accepted]

**Algorithm**

Simple analysis of this problem can lead to an easy solution.

These three cases are possible with string $$a$$ and $$b$$:-

* $$a=b$$. If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return -1.

* $$length(a)=length(b)$$ and $$a \ne b$$. Example: $$abc$$ and $$abd$$. In this case we can consider any string i.e. $$abc$$ or $$abd$$ as a required subsequence, as out of these two strings one string will never be a subsequence of other string. Hence, return $$length(a)$$ or $$length(b)$$.

* $$length(a) \ne length(b)$$. Example $$abcd$$ and $$abc$$. In this case we can consider bigger string as a required subsequence because bigger string can't be a subsequence of smaller string. Hence, return $$max(length(a),length(b))$$.


<iframe src="https://leetcode.com/playground/YdNcPgTE/shared" frameBorder="0" name="YdNcPgTE" width="100%" height="173"></iframe>

**Complexity Analysis**

* Time complexity : $$O(min(x,y))$$. where $$x$$ and $$y$$ are the lengths of strings $$a$$ and $$b$$ respectively. Here equals method will take $$min(x,y)$$ time .

* Space complexity : $$O(1)$$. No extra space required.

---


Analysis written by: [@vinod23](https://leetcode.com/vinod23)
