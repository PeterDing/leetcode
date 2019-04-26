# 0918 - Maximum Sum Circular Subarray

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/maximum-sum-circular-subarray) | [solution](https://leetcode.com/problems/maximum-sum-circular-subarray/solution/)


-----------

<p>Given a <strong>circular&nbsp;array</strong>&nbsp;<strong>C</strong> of integers represented by&nbsp;<code>A</code>, find the maximum possible sum of a non-empty subarray of <strong>C</strong>.</p>

<p>Here, a&nbsp;<em>circular&nbsp;array</em> means the end of the array connects to the beginning of the array.&nbsp; (Formally, <code>C[i] = A[i]</code> when <code>0 &lt;= i &lt; A.length</code>, and <code>C[i+A.length] = C[i]</code>&nbsp;when&nbsp;<code>i &gt;= 0</code>.)</p>

<p>Also, a subarray may only include each element of the fixed buffer <code>A</code> at most once.&nbsp; (Formally, for a subarray <code>C[i], C[i+1], ..., C[j]</code>, there does not exist <code>i &lt;= k1, k2 &lt;= j</code> with <code>k1 % A.length&nbsp;= k2 % A.length</code>.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,-2,3,-2]</span>
<strong>Output: </strong><span id="example-output-1">3
<strong>Explanation: </strong>Subarray [3] has maximum sum 3</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,-3,5]</span>
<strong>Output: </strong><span id="example-output-2">10
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [5,5] has maximum sum </span><span>5 + 5 = 10</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,-1,2,-1]</span>
<strong>Output: </strong><span id="example-output-3">4
<strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [2,-1,3] has maximum sum </span><span>2 + (-1) + 3 = 4</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,-2,2,-3]</span>
<strong>Output: </strong><span id="example-output-4">3
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [3] and [3,-2,2] both have maximum sum </span><span>3</span>
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[-2,-3,-1]</span>
<strong>Output: </strong><span id="example-output-5">-1
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [-1] has maximum sum -1</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ol>
	<li><code>-30000 &lt;= A[i] &lt;= 30000</code></li>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
</ol>
</div>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Notes and A Primer on Kadane's Algorithm

**About the Approaches**

In both Approach 1 and Approach 2, "grindy" solutions are presented that require less insight, but may be more intuitive to those with a solid grasp of the techniques in those approaches.  Without prior experience, these approaches would be very challenging to emulate.

Approaches 3 and 4 are much easier to implement, but require some insight.

**Explanation of Kadane's Algorithm**

To understand the solutions in this article, we need some familiarity with Kadane's algorithm.  In this section, we will explain the core idea behind it.

For a given array `A`, Kadane's algorithm can be used to find the maximum sum of the subarrays of `A`.  Here, we only consider non-empty subarrays.

Kadane's algorithm is based on dynamic programming.  Let `dp[j]` be the maximum sum of a subarray that ends in `A[j]`.  That is,

$$
\text{dp}[j] = \max\limits_i (A[i] + A[i+1] + \cdots + A[j])
$$

Then, a subarray ending in `j+1` (such as `A[i], A[i+1] + ... + A[j+1]`) maximizes the `A[i] + ... + A[j]` part of the sum by being equal to `dp[j]` if it is non-empty, and `0` if it is.  Thus, we have the recurrence:

$$
\text{dp}[j+1] = A[j+1] + \max(\text{dp}[j], 0)
$$

Since a subarray must end somewhere, $$\max\limits_j dp[j]$$ must be the desired answer.

To compute `dp` efficiently, Kadane's algorithm is usually written in the form that reduces space complexity.  We maintain two variables: `ans` as $$\max\limits_j dp[j]$$, and `cur` as $$dp[j]$$; and update them as $$j$$ iterates from $$0$$ to $$A\text{.length} - 1$$.

Then, Kadane's algorithm is given by the following psuedocode:

```python
#Kadane's algorithm
ans = cur = None
for x in A:
    cur = x + max(cur, 0)
    ans = max(ans, cur)
return ans
```


---
#### Approach 1: Next Array

**Intuition and Algorithm**

Subarrays of circular arrays can be classified as either as *one-interval* subarrays, or *two-interval* subarrays, depending on how many intervals of the fixed-size buffer `A` are required to represent them.

For example, if `A = [0, 1, 2, 3, 4, 5, 6]` is the underlying buffer of our circular array, we could represent the subarray `[2, 3, 4]` as one interval $$[2, 4]$$, but we would represent the subarray `[5, 6, 0, 1]` as two intervals $$[5, 6], [0, 1]$$.

Using Kadane's algorithm, we know how to get the maximum of *one-interval* subarrays, so it only remains to consider *two-interval* subarrays.

Let's say the intervals are $$[0, i], [j, A\text{.length} - 1]$$.  Let's try to compute the *i-th candidate*: the largest possible sum of a two-interval subarray for a given $$i$$.  Computing the $$[0, i]$$ part of the sum is easy.  Let's write

$$
T_j = A[j] + A[j+1] + \cdots + A[A\text{.length} - 1]
$$

and

$$
R_j = \max\limits_{k \geq j} T_k
$$

so that the desired i-th candidate is:

$$
(A[0] + A[1] + \cdots + A[i]) + R_{i+2}
$$

Since we can compute $$T_j$$ and $$R_j$$ in linear time, the answer is straightforward after this setup.


<iframe src="https://leetcode.com/playground/N59534xu/shared" frameBorder="0" width="100%" height="500" name="N59534xu"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Prefix Sums + Monoqueue

**Intuition**

First, we can frame the problem as a problem on a fixed array.

We can consider any subarray of the circular array with buffer `A`, to be a subarray of the fixed array `A+A`.

For example, if `A = [0,1,2,3,4,5]` represents a circular array, then the subarray `[4,5,0,1]` is also a subarray of fixed array `[0,1,2,3,4,5,0,1,2,3,4,5]`.  Let `B = A+A` be this fixed array.

Now say $$N = A\text{.length}$$, and consider the prefix sums

$$
P_k = B[0] + B[1] + \cdots + B[k-1]
$$

Then, we want the largest $$P_j - P_i$$ where $$j - i \leq N$$.

Now, consider the j-th candidate answer: the best possible $$P_j - P_i$$ for a fixed $$j$$.  We want the $$i$$ so that $$P_i$$ is smallest, with $$j - N \leq i < j$$.  Let's call this the *optimal i for the j-th candidate answer*.  We can use a monoqueue to manage this.

**Algorithm**

Iterate forwards through $$j$$, computing the $$j$$-th candidate answer at each step.  We'll maintain a `queue` of potentially optimal $$i$$'s.

The main idea is that if $$i_1 < i_2$$ and $$P_{i_1} \geq P_{i_2}$$, then we don't need to remember $$i_1$$ anymore.

Please see the inline comments for more algorithmic details about managing the queue.

<iframe src="https://leetcode.com/playground/qZ9ttQZM/shared" frameBorder="0" width="100%" height="500" name="qZ9ttQZM"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 3: Kadane's (Sign Variant)

**Intuition and Algorithm**

As in Approach 1, subarrays of circular arrays can be classified as either as *one-interval* subarrays, or *two-interval* subarrays.

Using Kadane's algorithm `kadane` for finding the maximum sum of non-empty subarrays, the answer for one-interval subarrays is `kadane(A)`.

Now, let $$N = A\text{.length}$$.  For a two-interval subarray like:

$$
(A_0 + A_1 + \cdots + A_i) + (A_j + A_{j+1} + \cdots + A_{N - 1})
$$

we can write this as

$$
(\sum_{k=0}^{N-1} A_k) - (A_{i+1} + A_{i+2} + \cdots + A_{j-1})
$$

For two-interval subarrays, let $$B$$ be the array $$A$$ with each element multiplied by $$-1$$.  Then the answer for two-interval subarrays is $$\text{sum}(A) + \text{kadane}(B)$$.

Except, this isn't quite true, as if the subarray of $$B$$ we choose is the entire array, the resulting two interval subarray $$[0, i] + [j, N-1]$$ would be empty.

We can remedy this problem by doing Kadane twice: once on $$B$$ with the first element removed, and once on $$B$$ with the last element removed.

<iframe src="https://leetcode.com/playground/pVGZH9TH/shared" frameBorder="0" width="100%" height="463" name="pVGZH9TH"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$ in additional space complexity.
<br />
<br />


---
#### Approach 4: Kadane's (Min Variant)

**Intuition and Algorithm**

As in Approach 3, subarrays of circular arrays can be classified as either as *one-interval* subarrays (which we can use Kadane's algorithm), or *two-interval* subarrays.

We can modify Kadane's algorithm to use `min` instead of `max`.  All the math in our explanation of Kadane's algorithm remains the same, but the algorithm lets us find the minimum sum of a subarray instead.

For a two interval subarray written as $$(\sum_{k=0}^{N-1} A_k) - (\sum_{k=i+1}^{j-1} A_k)$$, we can use our `kadane-min` algorithm to minimize the "interior" $$(\sum_{k=i+1}^{j-1} A_k)$$ part of the sum.

Again, because the interior $$[i+1, j-1]$$ must be non-empty, we can break up our search into a search on `A[1:]` and on `A[:-1]`.

<iframe src="https://leetcode.com/playground/RkbHxhiP/shared" frameBorder="0" width="100%" height="500" name="RkbHxhiP"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$ in additional space complexity.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
