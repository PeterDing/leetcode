# 0839 - Similar String Groups

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Depth-first Search, Union Find, Graph | [Leetcode](https://leetcode.com/problems/similar-string-groups) | [solution](https://leetcode.com/problems/similar-string-groups/solution/)


-----------

<p>Two strings <code>X</code>&nbsp;and <code>Y</code>&nbsp;are similar if we can swap two letters (in different positions) of <code>X</code>, so that&nbsp;it equals <code>Y</code>.</p>

<p>For example, <code>&quot;tars&quot;</code>&nbsp;and <code>&quot;rats&quot;</code>&nbsp;are similar (swapping at positions <code>0</code> and <code>2</code>), and <code>&quot;rats&quot;</code> and <code>&quot;arts&quot;</code> are similar, but <code>&quot;star&quot;</code> is not similar to <code>&quot;tars&quot;</code>, <code>&quot;rats&quot;</code>, or <code>&quot;arts&quot;</code>.</p>

<p>Together, these form two connected groups by similarity: <code>{&quot;tars&quot;, &quot;rats&quot;, &quot;arts&quot;}</code> and <code>{&quot;star&quot;}</code>.&nbsp; Notice that <code>&quot;tars&quot;</code> and <code>&quot;arts&quot;</code> are in the same group even though they are not similar.&nbsp; Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.</p>

<p>We are given a list <code>A</code> of strings.&nbsp; Every string in <code>A</code> is an anagram of every other string in <code>A</code>.&nbsp; How many groups are there?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[&quot;tars&quot;,&quot;rats&quot;,&quot;arts&quot;,&quot;star&quot;]
<strong>Output: </strong>2</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>A.length &lt;= 2000</code></li>
	<li><code>A[i].length &lt;= 1000</code></li>
	<li><code>A.length * A[i].length &lt;= 20000</code></li>
	<li>All words in <code>A</code>&nbsp;consist of lowercase letters only.</li>
	<li>All words in <code>A</code> have the same length and are anagrams of each other.</li>
	<li>The judging time limit has been increased for this question.</li>
</ol>


-----------


## Similar Problems




## Thought:
