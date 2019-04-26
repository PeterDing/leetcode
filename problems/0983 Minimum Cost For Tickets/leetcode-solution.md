# 0983 - Minimum Cost For Tickets

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/minimum-cost-for-tickets) | [solution](https://leetcode.com/problems/minimum-cost-for-tickets/solution/)


-----------

<p>In a country popular for train travel, you&nbsp;have planned some train travelling one year in advance.&nbsp; The days of the year that you will travel is given as an array <code>days</code>.&nbsp; Each day is an integer from <code>1</code> to <code>365</code>.</p>

<p>Train tickets are sold in 3 different ways:</p>

<ul>
	<li>a 1-day pass is sold for <code>costs[0]</code> dollars;</li>
	<li>a 7-day pass is sold for <code>costs[1]</code> dollars;</li>
	<li>a 30-day pass is sold for <code>costs[2]</code> dollars.</li>
</ul>

<p>The passes allow that many days of consecutive travel.&nbsp; For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.</p>

<p>Return the minimum number of dollars you need to travel every day in the given list of <code>days</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>days = <span id="example-input-1-1">[1,4,6,7,8,20]</span>, costs = <span id="example-input-1-2">[2,7,15]</span>
<strong>Output: </strong><span id="example-output-1">11</span>
<strong>Explanation: </strong>
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>days = <span id="example-input-2-1">[1,2,3,4,5,6,7,8,9,10,30,31]</span>, costs = <span id="example-input-2-2">[2,7,15]</span>
<strong>Output: </strong><span id="example-output-2">17</span>
<strong>Explanation: </strong>
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= days.length &lt;= 365</code></li>
	<li><code>1 &lt;= days[i] &lt;= 365</code></li>
	<li><code>days</code> is in strictly increasing order.</li>
	<li><code>costs.length == 3</code></li>
	<li><code>1 &lt;= costs[i] &lt;= 1000</code></li>
</ol>


-----------


## Similar Problems

- [Medium] [Coin Change](coin-change)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming (Day Variant)

**Intuition and Algorithm**

For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass.  If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.

We can express those choices as a recursion and use dynamic programming.  Let's say `dp(i)` is the cost to fulfill your travel plan from day `i` to the end of the plan.  Then, if you have to travel today, your cost is:

$$
\text{dp}(i) = \min(\text{dp}(i+1) + \text{costs}[0], \text{dp}(i+7) + \text{costs}[1], \text{dp}(i+30) + \text{costs}[2])
$$

<iframe src="https://leetcode.com/playground/vQP5W3UT/shared" frameBorder="0" width="100%" height="500" name="vQP5W3UT"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(W)$$, where $$W = 365$$ is the maximum numbered day in your travel plan.

* Space Complexity:  $$O(W)$$.
<br />
<br />


---
#### Approach 2: Dynamic Programming (Window Variant)

**Intuition and Algorithm**

As in *Approach 1*, we only need to buy a travel pass on a day we intend to travel.

Now, let `dp(i)` be the cost to travel from day `days[i]` to the end of the plan.  If say, `j1` is the largest index such that `days[j1] < days[i] + 1`, `j7` is the largest index such that `days[j7] < days[i] + 7`, and `j30` is the largest index such that `days[j30] < days[i] + 30`, then we have:

$$
\text{dp}(i) = \min(\text{dp}(j1) + \text{costs}[0], \text{dp}(j7) + \text{costs}[1], \text{dp}(j30) + \text{costs}[2])
$$

<iframe src="https://leetcode.com/playground/NtqEyFYA/shared" frameBorder="0" width="100%" height="500" name="NtqEyFYA"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of unique days in your travel plan.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
