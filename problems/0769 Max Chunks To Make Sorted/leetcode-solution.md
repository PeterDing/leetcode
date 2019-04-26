# 0769 - Max Chunks To Make Sorted

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/max-chunks-to-make-sorted) | [solution](https://leetcode.com/problems/max-chunks-to-make-sorted/solution/)


-----------

<p>Given an array <code>arr</code> that is a permutation of <code>[0, 1, ..., arr.length - 1]</code>, we split the array into some number of &quot;chunks&quot; (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.</p>

<p>What is the most number of chunks we could have made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,3,2,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn&#39;t sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,0,2,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>arr</code> will have length in range <code>[1, 10]</code>.</li>
	<li><code>arr[i]</code> will be a permutation of <code>[0, 1, ..., arr.length - 1]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Hard] [Max Chunks To Make Sorted II](max-chunks-to-make-sorted-ii)




## Solution:

[TOC]

---
#### Approach #1: Brute Force [Accepted]

**Intuition and Algorithm**

Let's try to find the smallest left-most chunk.  If the first `k` elements are `[0, 1, ..., k-1]`, then it can be broken into a chunk, and we have a smaller instance of the same problem.

We can check whether `k+1` elements chosen from `[0, 1, ..., n-1]` are `[0, 1, ..., k]` by checking whether the maximum of that choice is `k`.

<iframe src="https://leetcode.com/playground/62RMHZZv/shared" frameBorder="0" width="100%" height="225" name="62RMHZZv"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `arr`

* Space Complexity: $$O(1)$$.

---

For more approaches, please visit the article for the companion problem [Max Chunks To Make Sorted II](https://leetcode.com/articles/max-chunks-to-make-sorted-ii/).

---

Analysis written by: [@awice](https://leetcode.com/awice).
