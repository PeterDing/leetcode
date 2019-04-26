# 0128 - Longest Consecutive Sequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Union Find | [Leetcode](https://leetcode.com/problems/longest-consecutive-sequence) | [solution](https://leetcode.com/problems/longest-consecutive-sequence/solution/)


-----------

<p>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.</p>

<p>Your algorithm should run in O(<em>n</em>) complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[100, 4, 200, 1, 3, 2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>


-----------


## Similar Problems

- [Medium] [Binary Tree Longest Consecutive Sequence](binary-tree-longest-consecutive-sequence)




## Solution:

[TOC]

#### Approach 1: Brute Force

**Intuition**

Because a sequence could start at any number in `nums`, we can exhaust the
entire search space by building as long a sequence as possible from every
number.

**Algorithm**

The brute force algorithm does not do anything clever - it just considers
each number in `nums`, attempting to count as high as possible from that
number using only numbers in `nums`. After it counts too high (i.e.
`currentNum` refers to a number that `nums` does not contain), it records the
length of the sequence if it is larger than the current best. The algorithm
is necessarily optimal because it explores every possibility.

<iframe src="https://leetcode.com/playground/puxLaX5E/shared" frameBorder="0" width="100%" height="500" name="puxLaX5E"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^3)$$.

    The outer loop runs exactly $$n$$ times, and because `currentNum`
    increments by 1 during each iteration of the `while` loop, it runs in
    $$O(n)$$ time. Then, on each iteration of the `while` loop, an $$O(n)$$
    lookup in the array is performed. Therefore, this brute force algorithm
    is really three nested $$O(n)$$ loops, which compound multiplicatively to a
    cubic runtime.

* Space complexity : $$O(1)$$.

    The brute force algorithm only allocates a handful of integers, so it uses constant
    additional space.

<br />

---

#### Approach 2: Sorting

**Intuition**

If we can iterate over the numbers in ascending order, then it will be
easy to find sequences of consecutive numbers. To do so, we can sort the
array.

**Algorithm**

Before we do anything, we check for the base case input of the empty array.
The longest sequence in an empty array is, of course, 0, so we can simply
return that. For all other cases, we sort `nums` and consider each number
after the first (because we need to compare each number to its previous
number). If the current number and the previous are equal, then our current
sequence is neither extended nor broken, so we simply move on to the next
number. If they are unequal, then we must check whether the current number
extends the sequence (i.e. `nums[i] == nums[i-1] + 1`). If it does, then we
add to our current count and continue. Otherwise, the sequence is broken, so
we record our current sequence and reset it to 1 (to include the number that
broke the sequence). It is possible that the last element of `nums` is part
of the longest sequence, so we return the maximum of the current sequence and
the longest one.

![Sorting Example](../Figures/128/sorting.png)
{:align="center"}

Here, an example array is sorted before the linear scan identifies all consecutive sequences.
The longest sequence is colored in red.

<iframe src="https://leetcode.com/playground/M9Rxw5qk/shared" frameBorder="0" width="100%" height="497" name="M9Rxw5qk"></iframe>

**Complexity Analysis**

* Time complexity : $$O(nlgn)$$.

    The main `for` loop does constant work $$n$$ times, so the algorithm's time
    complexity is dominated by the invocation of `sort`, which will run in
    $$O(nlgn)$$ time for any sensible implementation.

* Space complexity : $$O(1)$$ (or $$O(n)$$).

    For the implementations provided here, the space complexity is constant
    because we sort the input array in place. If we are not allowed to modify
    the input array, we must spend linear space to store a sorted copy.

<br />

---

#### Approach 3: HashSet and Intelligent Sequence Building

**Intuition**

It turns out that our initial brute force solution was on the right track, but missing
a few optimizations necessary to reach $$O(n)$$ time complexity.

**Algorithm**

This optimized algorithm contains only two changes from the brute force
approach: the numbers are stored in a `HashSet` (or `Set`, in Python) to
allow $$O(1)$$ lookups, and we only attempt to build sequences from numbers
that are not already part of a longer sequence. This is accomplished by first
ensuring that the number that would immediately precede the current number in
a sequence is not present, as that number would necessarily be part of a
longer sequence.

<iframe src="https://leetcode.com/playground/KbUGJ84k/shared" frameBorder="0" width="100%" height="497" name="KbUGJ84k"></iframe>


**Complexity Analysis**

* Time complexity : $$O(n)$$.

    Although the time complexity appears to be quadratic due to the `while`
    loop nested within the `for` loop, closer inspection reveals it to be
    linear. Because the `while` loop is reached only when `currentNum` marks
    the beginning of a sequence (i.e. `currentNum-1` is not present in
    `nums`), the `while` loop can only run for $$n$$ iterations throughout the
    entire runtime of the algorithm. This means that despite looking like
    $$O(n \cdot n)$$ complexity, the nested loops actually run in $$O(n + n) = O(n)$$
    time. All other computations occur in constant time, so the overall
    runtime is linear.

* Space complexity : $$O(n)$$.

    In order to set up $$O(1)$$ containment lookups, we allocate linear space
    for a hash table to store the $$O(n)$$ numbers in `nums`. Other than that,
    the space complexity is identical to that of the brute force solution.
