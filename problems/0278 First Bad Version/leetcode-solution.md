# 0278 - First Bad Version

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Binary Search | [Leetcode](https://leetcode.com/problems/first-bad-version) | [solution](https://leetcode.com/problems/first-bad-version/solution/)


-----------

<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which will return whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p><b>Example:</b></p>

<pre>
Given n = 5, and version = 4 is the first bad version.

<code>call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true

Then 4 is the first bad version.&nbsp;</code>
</pre>

-----------


## Similar Problems

- [Medium] [Find First and Last Position of Element in Sorted Array](find-first-and-last-position-of-element-in-sorted-array)

- [Easy] [Search Insert Position](search-insert-position)

- [Easy] [Guess Number Higher or Lower](guess-number-higher-or-lower)




## Solution:

[TOC]

## Summary

This is a very simple problem. There is a subtle trap that you may fall into if you are not careful. Other than that, it is a direct application of a very famous algorithm.

## Solution

---
#### Approach #1 (Linear Scan) [Time Limit Exceeded]

The straight forward way is to brute force it by doing a linear scan.

<iframe src="https://leetcode.com/playground/Ezb8JYsL/shared" frameBorder="0" name="Ezb8JYsL" width="100%" height="190"></iframe>

**Complexity analysis**

* Time complexity : $$O(n)$$.
Assume that $$isBadVersion(version)$$ takes constant time to check if a *version* is bad. It takes at most $$n - 1$$ checks, therefore the overall time complexity is $$O(n)$$.

* Space complexity : $$O(1)$$.

---
#### Approach #2 (Binary Search) [Accepted]

It is not difficult to see that this could be solved using a classic algorithm - Binary search. Let us see how the search space could be halved each time below.

    Scenario #1: isBadVersion(mid) => false

     1 2 3 4 5 6 7 8 9
     G G G G G G B B B       G = Good, B = Bad
     |       |       |
    left    mid    right

Let us look at the first scenario above where $$isBadVersion(mid) \Rightarrow  false$$. We know that all versions preceding and including $$mid$$ are all good. So we set $$left = mid + 1$$ to indicate that the new search space is the interval $$[mid + 1, right]$$ (inclusive).

    Scenario #2: isBadVersion(mid) => true

     1 2 3 4 5 6 7 8 9
     G G G B B B B B B       G = Good, B = Bad
     |       |       |
    left    mid    right

The only scenario left is where $$isBadVersion(mid) \Rightarrow true$$. This tells us that $$mid$$ may or may not be the first bad version, but we can tell for sure that all versions after $$mid$$ can be discarded. Therefore we set $$right = mid$$ as the new search space of interval $$[left,mid]$$ (inclusive).

In our case, we indicate $$left$$ and $$right$$ as the boundary of our search space (both inclusive). This is why we initialize $$left = 1$$ and $$right = n $$. How about the terminating condition? We could guess that $$left$$ and $$right$$ eventually both meet and it must be the first bad version, but how could you tell for sure?

The formal way is to [prove by induction](http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html), which you can read up yourself if you are interested. Here is a helpful tip to quickly prove the correctness of your binary search algorithm
during an interview. We just need to test an input of size 2. Check if it reduces the search space to a single element (which must be the answer) for both of the scenarios above. If not, your algorithm will never terminate.

If you are setting $$mid = \frac{left + right}{2}$$, you have to be very careful. Unless you are using a language that does not overflow such as [Python](https://www.reddit.com/r/Python/comments/36xu5z/can_integer_operations_overflow_in_python/), $$left + right$$ could overflow. One way to fix this is to use $$left + \frac{right - left}{2}$$ instead.

If you fall into this subtle overflow bug, you are not alone. Even Jon Bentley's own implementation of binary search had this [overflow bug](https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues) and remained undetected for over twenty years.

<iframe src="https://leetcode.com/playground/VQBrosDg/shared" frameBorder="0" name="VQBrosDg" width="100%" height="275"></iframe>

**Complexity analysis**

* Time complexity : $$O(\log n)$$.
The search space is halved each time, so the time complexity is $$O(\log n)$$.

* Space complexity : $$O(1)$$.
