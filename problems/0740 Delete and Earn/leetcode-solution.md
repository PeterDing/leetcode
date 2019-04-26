# 0740 - Delete and Earn

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/delete-and-earn) | [solution](https://leetcode.com/problems/delete-and-earn/solution/)


-----------

<p>Given an array <code>nums</code> of integers, you can perform operations on the array.</p>

<p>In each operation, you pick any <code>nums[i]</code> and delete it to earn <code>nums[i]</code> points. After, you must delete <b>every</b> element equal to <code>nums[i] - 1</code> or <code>nums[i] + 1</code>.</p>

<p>You start with 0 points. Return the maximum number of points you can earn by applying such operations.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> nums = [3, 4, 2]
<b>Output:</b> 6
<b>Explanation:</b> 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> nums = [2, 2, 3, 3, 3, 4]
<b>Output:</b> 9
<b>Explanation:</b> 
Delete 3 to earn 3 points, deleting both 2&#39;s and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li>The length of <code>nums</code> is at most <code>20000</code>.</li>
	<li>Each element <code>nums[i]</code> is an integer in the range <code>[1, 10000]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Easy] [House Robber](house-robber)




## Solution:

[TOC]


#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

Because all numbers are positive, if we "take" a number (use it to score points), we might as well take all copies of it, since we've already erased all its neighbors.  We could keep a count of each number so we know how many points taking a number is worth total.

Now let's investigate what happens when we add a new number `X` (plus copies) that is larger than all previous numbers.  Naively, our answer would be the previous answer, plus the value of `X` - which can be solved with dynamic programming.  However, this fails if our previous answer had a number taken that was adjacent to `X`.

Luckily, we can remedy this.  Let's say we knew `using`, the value of our previous answer, and `avoid`, the value of our previous answer that doesn't use the previously largest value `prev`.  Then we could compute new values of `using` and `avoid` appropriately.

**Algorithm**

For each unique value `k` of `nums` in increasing order, let's maintain the correct values of `avoid` and `using`, which represent the answer if we don't take or take `k` respectively.

If the new value `k` is adjacent to the previously largest value `prev`, then the answer if we must take `k` is `(the point value of k) + avoid`, while the answer if we must not take `k` is `max(avoid, using)`.  Similarly, if `k` is not adjacent to `prev`, the answer if we must take `k` is `(the point value of k) + max(avoid, using)`, and the answer if we must not take `k` is `max(avoid, using)`.

At the end, the best answer may or may not use the largest value in `nums`, so we return `max(avoid, using)`.

Our demonstrated solutions showcase two different kinds of sorts: a library one, and a radix sort.  For each language, the other kind of solution can be done without much difficulty, by using an array (Python) or HashMap (Java) respectively.

<iframe src="https://leetcode.com/playground/TBKVkiLD/shared" frameBorder="0" width="100%" height="395" name="TBKVkiLD"></iframe>

**Complexity Analysis**

* Time Complexity (Python): $$O(N \log N)$$, where $$N$$ is the length of `nums`.  We make a single pass through the sorted keys of $$N$$, and the complexity is dominated by the sorting step.

* Space Complexity (Python): $$O(N)$$, the size of our `count`.

* Time Complexity (Java): We performed a radix sort instead, so our complexity is $$O(N+W)$$ where $$W$$ is the range of allowable values for `nums[i]`.

* Space Complexity (Java): $$O(W)$$, the size of our `count`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
