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




## Thought:
