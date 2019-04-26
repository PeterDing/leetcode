# 0871 - Minimum Number of Refueling Stops

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Heap | [Leetcode](https://leetcode.com/problems/minimum-number-of-refueling-stops) | [solution](https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/)


-----------

<p>A car travels from a starting position to a destination which is <code>target</code> miles east of the starting position.</p>

<p>Along the way, there are gas stations.&nbsp; Each <code>station[i]</code>&nbsp;represents a gas station that is <code>station[i][0]</code> miles east of the starting position, and has <code>station[i][1]</code> liters of gas.</p>

<p>The car starts with an infinite tank of gas, which initially has&nbsp;<code>startFuel</code>&nbsp;liters of fuel in it.&nbsp; It uses 1 liter of gas per 1 mile that it drives.</p>

<p>When the car&nbsp;reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.</p>

<p>What is the least number of refueling stops the car must make in order to reach its destination?&nbsp; If it cannot reach the destination, return <code>-1</code>.</p>

<p>Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.&nbsp; If the car reaches the destination with 0 fuel left, it is still considered to have arrived.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>target = <span id="example-input-1-1">1</span>, startFuel = <span id="example-input-1-2">1</span>, stations = <span id="example-input-1-3">[]</span>
<strong>Output: </strong><span id="example-output-1">0</span>
<strong>Explanation: </strong>We can reach the target without refueling.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>target = <span id="example-input-2-1">100</span>, startFuel = <span id="example-input-2-2">1</span>, stations = <span id="example-input-2-3">[[10,100]]</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong>We can&#39;t reach the target (or even the first gas station).
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>target = <span id="example-input-3-1">100</span>, startFuel = <span id="example-input-3-2">10</span>, stations = <span id="example-input-3-3">[[10,60],[20,30],[30,30],[60,40]]</span>
<strong>Output: </strong><span id="example-output-3">2</span>
<strong>Explanation: </strong>
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= target, startFuel, stations[i][1] &lt;= 10^9</code></li>
	<li><code>0 &lt;= stations.length &lt;= 500</code></li>
	<li><code>0 &lt; stations[0][0] &lt; stations[1][0] &lt; ... &lt; stations[stations.length-1][0] &lt; target</code></li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

Let's determine `dp[i]`, the farthest location we can get to using `i` refueling stops.  This is motivated by the fact that we want the smallest `i` for which `dp[i] >= target`.

**Algorithm**

Let's update `dp` as we consider each station in order.  With no stations, clearly we can get a maximum distance of `startFuel` with `0` refueling stops.

Now let's look at the update step.  When adding a station `station[i] = (location, capacity)`, any time we could reach this station with `t` refueling stops, we can now reach `capacity` further with `t+1` refueling stops.

For example, if we could reach a distance of 15 with 1 refueling stop, and now we added a station at location 10 with 30 liters of fuel, then we could potentially reach a distance of 45 with 2 refueling stops.

<iframe src="https://leetcode.com/playground/CrpMSMbm/shared" frameBorder="0" width="100%" height="310" name="CrpMSMbm"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `stations`.

* Space Complexity:  $$O(N)$$, the space used by `dp`.
<br />
<br />


---
#### Approach 2: Heap

**Intuition**

When driving past a gas station, let's remember the amount of fuel it contained.  We don't need to decide yet whether to fuel up here or not - for example, there could be a bigger gas station up ahead that we would rather refuel at.

When we run out of fuel before reaching the next station, we'll retroactively fuel up: greedily choosing the largest gas stations first.

This is guaranteed to succeed because we drive the largest distance possible before each refueling stop, and therefore have the largest choice of gas stations to (retroactively) stop at.

**Algorithm**

`pq` ("priority queue") will be a max-heap of the capacity of each gas station we've driven by.  We'll also keep track of `tank`, our current fuel.

When we reach a station but have negative fuel (ie. we needed to have refueled at some point in the past), we will add the capacities of the largest gas stations we've driven by until the fuel is non-negative.

If at any point this process fails (that is, no more gas stations), then the task is impossible.

<iframe src="https://leetcode.com/playground/k5wvzRam/shared" frameBorder="0" width="100%" height="500" name="k5wvzRam"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `stations`.

* Space Complexity:  $$O(N)$$, the space used by `pq`.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).  Approach 1 inspired by @lee215.
