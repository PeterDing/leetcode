# 0435 - Non-overlapping Intervals

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/non-overlapping-intervals) | [solution](https://leetcode.com/problems/non-overlapping-intervals/solution/)


-----------

<p>Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.</p>

<p><b>Note:</b></p>

<ol>
	<li>You may assume the interval&#39;s end point is always bigger than its start point.</li>
	<li>Intervals like [1,2] and [2,3] have borders &quot;touching&quot; but they don&#39;t overlap each other.</li>
</ol>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [ [1,2], [2,3], [3,4], [1,3] ]

<b>Output:</b> 1

<b>Explanation:</b> [1,3] can be removed and the rest of intervals are non-overlapping.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [ [1,2], [1,2], [1,2] ]

<b>Output:</b> 2

<b>Explanation:</b> You need to remove two [1,2] to make the rest of intervals non-overlapping.
</pre>

<p>&nbsp;</p>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> [ [1,2], [2,3] ]

<b>Output:</b> 0

<b>Explanation:</b> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>


-----------


## Similar Problems

- [Medium] [Minimum Number of Arrows to Burst Balloons](minimum-number-of-arrows-to-burst-balloons)




## Thought:
