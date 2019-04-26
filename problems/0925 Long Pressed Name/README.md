# 0925 - Long Pressed Name

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Two Pointers, String | [Leetcode](https://leetcode.com/problems/long-pressed-name) | [solution](https://leetcode.com/problems/long-pressed-name/solution/)


-----------

<p>Your friend is typing his <code>name</code>&nbsp;into a keyboard.&nbsp; Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code>&nbsp;characters of the keyboard.&nbsp; Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-1-1">&quot;alex&quot;</span>, typed = <span id="example-input-1-2">&quot;aaleex&quot;</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-2-1">&quot;saeed&quot;</span>, typed = <span id="example-input-2-2">&quot;ssaaedd&quot;</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>'e' must have been pressed twice, but it wasn't in the typed output.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-3-1">&quot;leelee&quot;</span>, typed = <span id="example-input-3-2">&quot;lleeelee&quot;</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>name = <span id="example-input-4-1">&quot;laiden&quot;</span>, typed = <span id="example-input-4-2">&quot;laiden&quot;</span>
<strong>Output: </strong><span id="example-output-4">true</span>
<strong>Explanation: </strong>It's not necessary to long press any character.
</pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>name.length &lt;= 1000</code></li>
	<li><code>typed.length &lt;= 1000</code></li>
	<li>The characters of <code>name</code> and <code>typed</code> are lowercase letters.</li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>

-----------


## Similar Problems




## Thought:
