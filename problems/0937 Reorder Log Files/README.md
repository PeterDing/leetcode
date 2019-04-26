# 0937 - Reorder Log Files

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/reorder-log-files) | [solution](https://leetcode.com/problems/reorder-log-files/solution/)


-----------

<p>You have an array of <code>logs</code>.&nbsp; Each log is a space delimited string of words.</p>

<p>For each log, the first word in each log is an alphanumeric <em>identifier</em>.&nbsp; Then, either:</p>

<ul>
	<li>Each word after the identifier will consist only of lowercase letters, or;</li>
	<li>Each word after the identifier will consist only of digits.</li>
</ul>

<p>We will call these two varieties of logs <em>letter-logs</em> and <em>digit-logs</em>.&nbsp; It is guaranteed that each log has at least one word after its identifier.</p>

<p>Reorder the logs so that all of the letter-logs come before any digit-log.&nbsp; The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.&nbsp; The digit-logs should be put in their original order.</p>

<p>Return the final order of the logs.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;a1 9 2 3 1&quot;,&quot;g1 act car&quot;,&quot;zo4 4 7&quot;,&quot;ab1 off key dog&quot;,&quot;a8 act zoo&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;g1 act car&quot;,&quot;a8 act zoo&quot;,&quot;ab1 off key dog&quot;,&quot;a1 9 2 3 1&quot;,&quot;zo4 4 7&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= logs.length &lt;= 100</code></li>
	<li><code>3 &lt;= logs[i].length &lt;= 100</code></li>
	<li><code>logs[i]</code> is guaranteed to have an identifier, and a word after the identifier.</li>
</ol>
</div>


-----------


## Similar Problems




## Thought:
