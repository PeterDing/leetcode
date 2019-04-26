# 0826 - Most Profit Assigning Work

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers | [Leetcode](https://leetcode.com/problems/most-profit-assigning-work) | [solution](https://leetcode.com/problems/most-profit-assigning-work/solution/)


-----------

<p>We have jobs: <code>difficulty[i]</code>&nbsp;is the difficulty of the&nbsp;<code>i</code>th job, and&nbsp;<code>profit[i]</code>&nbsp;is the profit of the&nbsp;<code>i</code>th job.&nbsp;</p>

<p>Now we have some workers.&nbsp;<code>worker[i]</code>&nbsp;is the ability of the&nbsp;<code>i</code>th worker, which means that this worker can only complete a job with difficulty at most&nbsp;<code>worker[i]</code>.&nbsp;</p>

<p>Every worker can be assigned at most one job, but one job&nbsp;can be completed multiple times.</p>

<p>For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.&nbsp; If a worker cannot complete any job, his profit is $0.</p>

<p>What is the most profit we can make?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>Output: </strong>100 
<strong>Explanation: W</strong>orkers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= difficulty.length = profit.length &lt;= 10000</code></li>
	<li><code>1 &lt;= worker.length &lt;= 10000</code></li>
	<li><code>difficulty[i], profit[i], worker[i]</code>&nbsp; are in range&nbsp;<code>[1, 10^5]</code></li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Sorting Events [Accepted]

**Intuition**

We can consider the workers in any order, so let's process them in order of skill.

If we processed all jobs with lower skill first, then the profit is just the most profitable job we have seen so far.

**Algorithm**

We can use a "two pointer" approach to process jobs in order.  We will keep track of `best`, the maximum profit seen.

For each worker with a certain `skill`, after processing all jobs with lower or equal difficulty, we add `best` to our answer.

<iframe src="https://leetcode.com/playground/52pUn6By/shared" frameBorder="0" width="100%" height="412" name="52pUn6By"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N + Q \log Q)$$, where $$N$$ is the number of jobs, and $$Q$$ is the number of people.

* Space Complexity: $$O(N)$$, the additional space used by `jobs`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
