# 0895 - Maximum Frequency Stack

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Hash Table, Stack | [Leetcode](https://leetcode.com/problems/maximum-frequency-stack) | [solution](https://leetcode.com/problems/maximum-frequency-stack/solution/)


-----------

<p>Implement <code>FreqStack</code>, a class which simulates the operation of a stack-like data structure.</p>

<p><code>FreqStack</code>&nbsp;has two functions:</p>

<ul>
	<li><code>push(int x)</code>, which pushes an integer <code>x</code> onto the stack.</li>
	<li><code>pop()</code>, which <strong>removes</strong> and returns the most frequent element in the stack.
	<ul>
		<li>If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>
<span id="example-input-1-1">[&quot;FreqStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;]</span>,
<span id="example-input-1-2">[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,null,null,null,null,null,null,5,7,5,4]</span>
<strong>Explanation</strong>:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -&gt; returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -&gt; returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -&gt; returns 5.
The stack becomes [5,7,4].

pop() -&gt; returns 4.
The stack becomes [5,7].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Calls to <code>FreqStack.push(int x)</code>&nbsp;will be such that <code>0 &lt;= x &lt;= 10^9</code>.</li>
	<li>It is guaranteed that <code>FreqStack.pop()</code> won&#39;t be called if the stack has zero elements.</li>
	<li>The total number of <code>FreqStack.push</code> calls will not exceed <code>10000</code> in a single test case.</li>
	<li>The total number of <code>FreqStack.pop</code>&nbsp;calls will not exceed <code>10000</code> in a single test case.</li>
	<li>The total number of <code>FreqStack.push</code> and <code>FreqStack.pop</code> calls will not exceed <code>150000</code> across all test cases.</li>
</ul>

<div>
<p>&nbsp;</p>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Stack of Stacks

**Intuition**

Evidently, we care about the frequency of an element.  Let `freq` be a `Map` from $$x$$ to the number of occurrences of $$x$$.

Also, we (probably) care about `maxfreq`, the current maximum frequency of any element in the stack.  This is clear because we must pop the element with the maximum frequency.

The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent?  We can use a stack to query this information: the top of the stack is the most recent.

To this end, let `group` be a map from frequency to a stack of elements with that frequency.  We now have all the required components to implement `FreqStack`.

**Algorithm**

Actually, as an implementation level detail, if `x` has frequency `f`, then we'll have `x` in all `group[i] (i <= f)`, not just the top.  This is because each `group[i]` will store information related to the `i`th copy of `x`.

Afterwards, our goal is just to maintain `freq`, `group`, and `maxfreq` as described above.

<iframe src="https://leetcode.com/playground/jD2jBGjF/shared" frameBorder="0" width="100%" height="500" name="jD2jBGjF"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(1)$$ for both `push` and `pop` operations.

* Space Complexity:  $$O(N)$$, where `N` is the number of elements in the `FreqStack`.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
