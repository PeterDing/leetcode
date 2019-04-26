# 0030 - Substring with Concatenation of All Words

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Hash Table, Two Pointers, String | [Leetcode](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | [solution](https://leetcode.com/problems/substring-with-concatenation-of-all-words/solution/)


-----------

<p>You are given a string, <strong>s</strong>, and a list of words, <strong>words</strong>, that are all of the same length. Find all starting indices of substring(s) in <strong>s</strong> that is a concatenation of each word in <strong>words</strong> exactly once and without any intervening characters.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>Output:</strong> <code>[0,9]</code>
<strong>Explanation:</strong> Substrings starting at index 0 and 9 are &quot;barfoor&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;wordgoodgoodgoodbestword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;good&quot;,&quot;best&quot;,&quot;word&quot;]
<strong>Output:</strong> <code>[]</code>
</pre>


-----------


## Similar Problems

- [Hard] [Minimum Window Substring](minimum-window-substring)




## Thought:
