# 0981 - Time Based Key-Value Store

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, Binary Search | [Leetcode](https://leetcode.com/problems/time-based-key-value-store) | [solution](https://leetcode.com/problems/time-based-key-value-store/solution/)


-----------

<p>Create a timebased key-value store class&nbsp;<code>TimeMap</code>, that supports two operations.</p>

<p>1. <code>set(string key, string value, int timestamp)</code></p>

<ul>
	<li>Stores the <code>key</code> and <code>value</code>, along with the given <code>timestamp</code>.</li>
</ul>

<p>2. <code>get(string key, int timestamp)</code></p>

<ul>
	<li>Returns a value such that <code>set(key, value, timestamp_prev)</code> was called previously, with <code>timestamp_prev &lt;= timestamp</code>.</li>
	<li>If there are multiple such values, it returns the one with the largest <code>timestamp_prev</code>.</li>
	<li>If there are no values, it returns the empty string (<code>&quot;&quot;</code>).</li>
</ul>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">[&quot;TimeMap&quot;,&quot;set&quot;,&quot;get&quot;,&quot;get&quot;,&quot;set&quot;,&quot;get&quot;,&quot;get&quot;]</span>, inputs = <span id="example-input-1-2">[[],[&quot;foo&quot;,&quot;bar&quot;,1],[&quot;foo&quot;,1],[&quot;foo&quot;,3],[&quot;foo&quot;,&quot;bar2&quot;,4],[&quot;foo&quot;,4],[&quot;foo&quot;,5]]</span>
<strong>Output: </strong><span id="example-output-1">[null,null,&quot;bar&quot;,&quot;bar&quot;,null,&quot;bar2&quot;,&quot;bar2&quot;]</span>
<strong>Explanation: </strong><span id="example-output-1">&nbsp; 
TimeMap kv; &nbsp; 
kv.set(&quot;foo&quot;, &quot;bar&quot;, 1); // store the key &quot;foo&quot; and value &quot;bar&quot; along with timestamp = 1 &nbsp; 
kv.get(&quot;foo&quot;, 1);  // output &quot;bar&quot; &nbsp; 
kv.get(&quot;foo&quot;, 3); // output &quot;bar&quot; since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie &quot;bar&quot; &nbsp; 
kv.set(&quot;foo&quot;, &quot;bar2&quot;, 4); &nbsp; 
kv.get(&quot;foo&quot;, 4); // output &quot;bar2&quot; &nbsp; 
kv.get(&quot;foo&quot;, 5); //output &quot;bar2&quot; &nbsp; 
</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-2-1">[&quot;TimeMap&quot;,&quot;set&quot;,&quot;set&quot;,&quot;get&quot;,&quot;get&quot;,&quot;get&quot;,&quot;get&quot;,&quot;get&quot;]</span>, inputs = <span id="example-input-2-2">[[],[&quot;love&quot;,&quot;high&quot;,10],[&quot;love&quot;,&quot;low&quot;,20],[&quot;love&quot;,5],[&quot;love&quot;,10],[&quot;love&quot;,15],[&quot;love&quot;,20],[&quot;love&quot;,25]]</span>
<strong>Output: </strong><span id="example-output-2">[null,null,null,&quot;&quot;,&quot;high&quot;,&quot;high&quot;,&quot;low&quot;,&quot;low&quot;]</span>
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>All key/value strings are lowercase.</li>
	<li>All key/value strings have&nbsp;length in the range&nbsp;<code>[1, 100]</code></li>
	<li>The <code>timestamps</code> for all <code>TimeMap.set</code> operations are strictly increasing.</li>
	<li><code>1 &lt;= timestamp &lt;= 10^7</code></li>
	<li><code>TimeMap.set</code> and <code>TimeMap.get</code>&nbsp;functions will be called a total of <code>120000</code> times (combined) per test case.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: HashMap + Binary Search

**Intuition and Algorithm**

For each `key` we get or set, we only care about the timestamps and values for that key.  We can store this information in a `HashMap`.

Now, for each `key`, we can binary search the sorted list of timestamps to find the relevant `value` for that `key`.

<iframe src="https://leetcode.com/playground/jS7yH954/shared" frameBorder="0" width="100%" height="500" name="jS7yH954"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(1)$$ for each `set` operation, and $$O(\log N)$$ for each `get` operation, where $$N$$ is the number of entries in the `TimeMap`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: TreeMap

**Intuition and Algorithm**

In `Java`, we can use `TreeMap.floorKey(timestamp)` to find the largest timestamp smaller than the given `timestamp`.

We build our solution in the same way as *Approach 1*, swapping in this functionality.

<iframe src="https://leetcode.com/playground/pH7WK8ph/shared" frameBorder="0" width="100%" height="429" name="pH7WK8ph"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(1)$$ for each `set` operation, and $$O(\log N)$$ for each `get` operation, where $$N$$ is the number of entries in the `TimeMap`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
