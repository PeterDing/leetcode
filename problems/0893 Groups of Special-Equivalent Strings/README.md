# 0893 - Groups of Special-Equivalent Strings

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/groups-of-special-equivalent-strings) | [solution](https://leetcode.com/problems/groups-of-special-equivalent-strings/solution/)


-----------

<p>You are given an array <code>A</code> of strings.</p>

<p>Two strings <code>S</code> and <code>T</code> are&nbsp;<em>special-equivalent</em>&nbsp;if after any number of <em>moves</em>, S == T.</p>

<p>A <em>move</em> consists of choosing two indices <code>i</code> and <code>j</code> with <code>i % 2 == j % 2</code>, and swapping <code>S[i]</code> with <code>S[j]</code>.</p>

<p>Now, a <em>group of special-equivalent strings from <code>A</code></em>&nbsp;is a&nbsp;non-empty subset S of <code>A</code>&nbsp;such that any string not in S&nbsp;is not special-equivalent with any string in S.</p>

<p>Return the number of groups of special-equivalent strings from <code>A</code>.</p>

<p>&nbsp;</p>

<ul>
</ul>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;a&quot;,&quot;c&quot;,&quot;c&quot;]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<span><strong>Explanation</strong>: 3 groups [&quot;a&quot;,&quot;a&quot;], [&quot;b&quot;], [&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;aa&quot;,&quot;bb&quot;,&quot;ab&quot;,&quot;ba&quot;]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation</strong>: 4 groups <span id="example-input-2-1">[&quot;aa&quot;], [&quot;bb&quot;], [&quot;ab&quot;], [&quot;ba&quot;]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;]</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation</strong>: 3 groups [&quot;abc&quot;,&quot;cba&quot;], [&quot;acb&quot;,&quot;bca&quot;], [&quot;bac&quot;,&quot;cab&quot;]
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[&quot;abcd&quot;,&quot;cdab&quot;,&quot;adcb&quot;,&quot;cbad&quot;]</span>
<strong>Output: </strong><span id="example-output-4">1</span>
<strong>Explanation</strong>: 1 group <span id="example-input-4-1">[&quot;abcd&quot;,&quot;cdab&quot;,&quot;adcb&quot;,&quot;cbad&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
	<li>All <code>A[i]</code> have the same length.</li>
	<li>All <code>A[i]</code> consist of only lowercase letters.</li>
</ul>
</div>
</div>
</div>
</div>


-----------


## Similar Problems




## Thought:
