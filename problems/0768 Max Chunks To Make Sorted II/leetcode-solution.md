# 0768 - Max Chunks To Make Sorted II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array | [Leetcode](https://leetcode.com/problems/max-chunks-to-make-sorted-ii) | [solution](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/solution/)


-----------

<p><em>This question is the same as &quot;Max Chunks to Make Sorted&quot; except the integers of the given array are not necessarily distinct, the input array could be up to length <code>2000</code>, and the elements could be up to <code>10**8</code>.</em></p>

<hr />

<p>Given an array <code>arr</code> of integers (<strong>not necessarily distinct</strong>), we split the array into some number of &quot;chunks&quot; (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.</p>

<p>What is the most number of chunks we could have made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn&#39;t sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,1,3,4,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>arr</code> will have length in range <code>[1, 2000]</code>.</li>
	<li><code>arr[i]</code> will be an integer in range <code>[0, 10**8]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Max Chunks To Make Sorted](max-chunks-to-make-sorted)




## Solution:

[TOC]

---
#### Approach #1: Sliding Window [Accepted]

**Intuition**

Let's try to find the smallest left-most chunk.

**Algorithm**

Notice that if $$a_1, a_2, \dots, a_m$$ is a chunk, and $$a_1, a_2, \dots, a_n$$ is a chunk ($$m < n$$), then $$a_{m+1}, a_{m+2}, \dots, a_n$$ is a chunk too.  This shows that a greedy approach produces the highest number of chunks.

We know the array `arr` should end up like `expect = sorted(arr)`.  If the count of the first `k` elements minus the count what those elements should be is zero everywhere, then the first `k` elements form a valid chunk.  We repeatedly perform this process.

We can use a variable `nonzero` to count the number of letters where the current count is non-zero.

<iframe src="https://leetcode.com/playground/B8GKxQrY/shared" frameBorder="0" width="100%" height="480" name="B8GKxQrY"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N \log N)$$, where $$N$$ is the length of `arr`

* Space Complexity: $$O(N)$$.

---
#### Approach #2: Sorted Count Pairs [Accepted]

**Intuition**

As in *Approach #1*, let's try to find the smallest left-most chunk, where we have some expectation `expect = sorted(arr)`

If the elements were distinct, then it is enough to find the smallest `k` with `max(arr[:k+1]) == expect[k]`, as this must mean the elements of `arr[:k+1]` are some permutation of `expect[:k+1]`.

Since the elements are not distinct, this fails; but we can amend the cumulative multiplicity of each element to itself to make the elements distinct.

**Algorithm**

Instead of elements `x`, have counted elements `(x, count)` where `count` ranges from `1` to the total number of `x` present in `arr`.

Now `cur` will be the cumulative maximum of `counted[:k+1]`, where we expect a result of `Y = expect[k]`.  We count the number of times they are equal.

<iframe src="https://leetcode.com/playground/jLmjinpa/shared" frameBorder="0" width="100%" height="500" name="jLmjinpa"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N \log N)$$, where $$N$$ is the length of `arr`

* Space Complexity: $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
