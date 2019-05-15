# 0014 - Longest Common Prefix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/longest-common-prefix) | [solution](https://leetcode.com/problems/longest-common-prefix/solution/)

-----------

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p><strong>Note:</strong></p>

<p>All given inputs are in lowercase letters <code>a-z</code>.</p>

-----------


## Similar Problems




## Thought:

```python
stack = []
i = 0
while True:
    for s in array:
        stack[-1] ? s[i]
    i += 1
```

