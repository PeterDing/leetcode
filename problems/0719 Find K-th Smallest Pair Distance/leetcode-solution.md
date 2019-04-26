# 0719 - Find K-th Smallest Pair Distance

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Binary Search, Heap | [Leetcode](https://leetcode.com/problems/find-k-th-smallest-pair-distance) | [solution](https://leetcode.com/problems/find-k-th-smallest-pair-distance/solution/)


-----------

<p>Given an integer array, return the k-th smallest <b>distance</b> among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. </p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
nums = [1,3,1]
k = 1
<b>Output: 0</b> 
<b>Explanation:</b>
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>2 <= len(nums) <= 10000</code>.</li>
<li><code>0 <= nums[i] < 1000000</code>.</li>
<li><code>1 <= k <= len(nums) * (len(nums) - 1) / 2</code>.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Find K Pairs with Smallest Sums](find-k-pairs-with-smallest-sums)

- [Medium] [Kth Smallest Element in a Sorted Matrix](kth-smallest-element-in-a-sorted-matrix)

- [Medium] [Find K Closest Elements](find-k-closest-elements)

- [Hard] [Kth Smallest Number in Multiplication Table](kth-smallest-number-in-multiplication-table)

- [Hard] [K-th Smallest Prime Fraction](k-th-smallest-prime-fraction)




## Solution:

[TOC]


#### Approach #1: Heap [Time Limit Exceeded]

**Intuition and Algorithm**

Sort the points.  For every point with index `i`, the pairs with indexes `(i, j)` [by order of distance] are `(i, i+1), (i, i+2), ..., (i, N-1)`.

Let's keep a heap of pairs, initially `heap = [(i, i+1) for all i]`, and ordered by distance (the distance of `(i, j)` is `nums[j] - nums[i]`.)  Whenever we use a pair `(i, x)` from our heap, we will add `(i, x+1)` to our heap when appropriate.

<iframe src="https://leetcode.com/playground/haWM6KvQ/shared" frameBorder="0" width="100%" height="500" name="haWM6KvQ"></iframe>

**Complexity Analysis**

* Time Complexity: $$O((k+N) \log{N})$$, where $$N$$ is the length of `nums`.  As $$k = O(N^2)$$, this is $$O(N^2 \log {N})$$ in the worst case.  The complexity added by our heap operations is either $$O((k+N) \log N)$$ in the Java solution, or $$O(k \log{N} + N)$$ in the Python solution because the `heapq.heapify` operation is linear time.  Additionally, we add $$O(N \log N)$$ complexity due to sorting.

* Space Complexity: $$O(N)$$, the space used to store our `heap` of at most `N-1` elements.

---

#### Approach #2: Binary Search + Prefix Sum [Accepted]

**Intuition**

Let's binary search for the answer.  It's definitely in the range `[0, W]`, where `W = max(nums) - min(nums)]`.  

Let `possible(guess)` be true if and only if there are `k` or more pairs with distance less than or equal to `guess`.  We will focus on evaluating our `possible` function quickly.

**Algorithm**

Let `prefix[v]` be the number of points in `nums` less than or equal to `v`.  Also, let `multiplicity[j]` be the number of points `i` with `i < j and nums[i] == nums[j]`.  We can record both of these with a simple linear scan.

Now, for every point `i`, the number of points `j` with `i < j` and `nums[j] - nums[i] <= guess` is `prefix[x+guess] - prefix[x] + (count[i] - multiplicity[i])`, where `count[i]` is the number of ocurrences of `nums[i]` in `nums`.  The sum of this over all `i` is the number of pairs with distance `<= guess`.  

Finally, because the sum of `count[i] - multiplicity[i]` is the same as the sum of `multiplicity[i]`, we could just replace that term with `multiplicity[i]` without affecting the answer.  (Actually, the sum of multiplicities in total will be a constant used in the answer, so we could precalculate it if we wanted.)

In our Java solution, we computed `possible = count >= k` directly in the binary search instead of using a helper function.

<iframe src="https://leetcode.com/playground/upbfbVHa/shared" frameBorder="0" width="100%" height="500" name="upbfbVHa"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(W + N \log{W} + N \log{N})$$, where $$N$$ is the length of `nums`, and $$W$$ is equal to `nums[nums.length - 1] - nums[0]`.  We do $$O(W)$$ work to calculate `prefix` initially.  The $$\log W$$ factor comes from our binary search, and we do $$O(N)$$ work inside our call to `possible` (or to calculate `count` in Java).  The final $$O(N\log N)$$ factor comes from sorting.

* Space Complexity: $$O(N+W)$$, the space used to store `multiplicity` and `prefix`.

---

#### Approach #3: Binary Search + Sliding Window [Accepted]

**Intuition**

As in *Approach #2*, let's binary search for the answer, and we will focus on evaluating our `possible` function quickly.

**Algorithm**

We will use a sliding window approach to count the number of pairs with distance `<=` guess.  

For every possible `right`, we maintain the loop invariant: `left` is the smallest value such that `nums[right] - nums[left] <= guess`.  Then, the number of pairs with `right` as it's right-most endpoint is `right - left`, and we add all of these up.

<iframe src="https://leetcode.com/playground/UD6QK4gU/shared" frameBorder="0" width="100%" height="429" name="UD6QK4gU"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N \log{W} + N \log{N})$$, where $$N$$ is the length of `nums`, and $$W$$ is equal to `nums[nums.length - 1] - nums[0]`.  The $$\log W$$ factor comes from our binary search, and we do $$O(N)$$ work inside our call to `possible` (or to calculate `count` in Java).  The final $$O(N\log N)$$ factor comes from sorting.

* Space Complexity: $$O(1)$$.  No additional space is used except for integer variables.

---

Analysis written by: [@awice](https://leetcode.com/awice).
