# 0828 - Unique Letter String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Two Pointers | [Leetcode](https://leetcode.com/problems/unique-letter-string) | [solution](https://leetcode.com/problems/unique-letter-string/solution/)


-----------

<p>A character is unique in string <code>S</code> if it occurs exactly once in it.</p>

<p>For example, in string <code>S = &quot;LETTER&quot;</code>, the only unique characters are <code>&quot;L&quot;</code> and <code>&quot;R&quot;</code>.</p>

<p>Let&#39;s define <code>UNIQ(S)</code> as the number of unique characters in string <code>S</code>.</p>

<p>For example, <code>UNIQ(&quot;LETTER&quot;) =&nbsp; 2</code>.</p>

<p>Given a string <code>S</code> with only uppercases, calculate the sum of <code>UNIQ(substring)</code> over all non-empty substrings of <code>S</code>.</p>

<p>If there are two or more equal substrings at different positions in <code>S</code>, we consider them different.</p>

<p>Since the answer can be very large, return&nbsp;the answer&nbsp;modulo&nbsp;<code>10 ^ 9 + 7</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;ABC&quot;
<strong>Output: </strong>10
<strong>Explanation: </strong>All possible substrings are: &quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;AB&quot;,&quot;BC&quot; and &quot;ABC&quot;.
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;ABA&quot;
<strong>Output: </strong>8
<strong>Explanation: </strong>The same as example 1, except uni(&quot;ABA&quot;) = 1.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong> <code>0 &lt;= S.length &lt;= 10000</code>.</p>


-----------


## Similar Problems




## Thought:
