# 0857 - Minimum Cost to Hire K Workers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Heap | [Leetcode](https://leetcode.com/problems/minimum-cost-to-hire-k-workers) | [solution](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/)


-----------

<p>There are <code>N</code> workers.&nbsp; The <code>i</code>-th worker has a <code>quality[i]</code> and a minimum wage expectation <code>wage[i]</code>.</p>

<p>Now we want to hire exactly <code>K</code>&nbsp;workers to form a <em>paid group</em>.&nbsp; When hiring a group of K workers, we must pay them according to the following rules:</p>

<ol>
	<li>Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.</li>
	<li>Every worker in the paid group must be paid at least their minimum wage expectation.</li>
</ol>

<p>Return the least amount of money needed to form a paid group satisfying the above conditions.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>quality = <span id="example-input-1-1">[10,20,5]</span>, wage = <span id="example-input-1-2">[70,50,30]</span>, K = <span id="example-input-1-3">2</span>
<strong>Output: </strong><span id="example-output-1">105.00000
<strong>Explanation</strong>: </span><span>We pay 70 to 0-th worker and 35 to 2-th worker.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>quality = <span id="example-input-2-1">[3,1,10,10,1]</span>, wage = <span id="example-input-2-2">[4,8,2,2,7]</span>, K = <span id="example-input-2-3">3</span>
<strong>Output: </strong><span id="example-output-2">30.66667
<strong>Explanation</strong>: </span><span>We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.</span> 
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= N &lt;= 10000</code>, where <code>N = quality.length = wage.length</code></li>
	<li><code>1 &lt;= quality[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= wage[i] &lt;= 10000</code></li>
	<li>Answers within <code>10^-5</code> of the correct answer will be considered correct.</li>
</ol>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Greedy

**Intuition**

At least one worker will be paid their minimum wage expectation.  If not, we could scale all payments down by some factor and still keep everyone earning more than their wage expectation.

**Algorithm**

For each `captain` worker that will be paid their minimum wage expectation, let's calculate the cost of hiring K workers where each point of quality is worth `wage[captain] / quality[captain]` dollars.  With this approach, the remaining implementation is straightforward.

Note that this algorithm would not be efficient enough to pass larger test cases.

<iframe src="https://leetcode.com/playground/6wfBasLL/shared" frameBorder="0" width="100%" height="500" name="6wfBasLL"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2 \log N)$$, where $$N$$ is the number of workers.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Heap

**Intuition**

As in *Approach #1*, at least one worker is paid their minimum wage expectation.

Additionally, every worker has some minimum `ratio` of dollars to quality that they demand.  For example, if `wage[0] = 100` and `quality[0] = 20`, then the `ratio` for worker 0 is `5.0`.

The key insight is to iterate over the ratio.  Let's say we hire workers with a ratio `R` or lower.  Then, we would want to know the `K` workers with the lowest quality, and the sum of that quality.  We can use a heap to maintain these variables.

**Algorithm**

Maintain a max heap of quality.  (We're using a minheap, with negative values.)  We'll also maintain `sumq`, the sum of this heap.

For each worker in order of ratio, we know all currently considered workers have lower ratio.  (This worker will be the 'captain', as described in *Approach #1*.)  We calculate the candidate answer as this ratio times the sum of the smallest K workers in quality.

<iframe src="https://leetcode.com/playground/KRXJr8dq/shared" frameBorder="0" width="100%" height="500" name="KRXJr8dq"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the number of workers.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
