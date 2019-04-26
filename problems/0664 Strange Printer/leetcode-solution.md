# 0664 - Strange Printer

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Depth-first Search | [Leetcode](https://leetcode.com/problems/strange-printer) | [solution](https://leetcode.com/problems/strange-printer/solution/)


-----------

<p>
There is a strange printer with the following two special requirements:

<ol>
<li>The printer can only print a sequence of the same character each time.</li>
<li>At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.</li>
</ol>

</p>

<p>
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aaabbb"
<b>Output:</b> 2
<b>Explanation:</b> Print "aaa" first and then print "bbb".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "aba"
<b>Output:</b> 2
<b>Explanation:</b> Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
</pre>
</p>

<p><b>Hint</b>: Length of the given string will not exceed 100.</p>

-----------


## Similar Problems

- [Hard] [Remove Boxes](remove-boxes)




## Solution:

[TOC]

#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

It is natural to consider letting `dp(i, j)` be the answer for printing `S[i], S[i+1], ..., S[j]`, but proceeding from here is difficult.  We need the following sequence of deductions:

* Whatever turn creates the final print of `S[i]` might as well be the first turn, and also there might as well only be one print, since any later prints on interval `[i, k]` could just be on `[i+1, k]`.

* Say the first print is on `[i, k]`.  We can assume `S[i] == S[k]`, because if it wasn't, we could print up to the last occurrence of `S[i]` in `[i, k]` for the same result.

* When correctly printing everything in `[i, k]` (with `S[i] == S[k]`), it will take the same amount of steps as correctly printing everything in `[i, k-1]`.  This is because if `S[i]` and `S[k]` get completed in separate steps, we might as well print them first in one step instead.

**Algorithm**

With the above deductions, the algorithm is straightforward.

To compute a recursion for `dp(i, j)`, for every `i <= k <= j` with `S[i] == S[k]`, we have some candidate answer `dp(i, k-1) + dp(k+1, j)`, and we take the minimum of these candidates.  Of course, when `k = i`, the candidate is just `1 + dp(i+1, j)`.

To avoid repeating work, we memoize our intermediate answers `dp(i, j)`.

<iframe src="https://leetcode.com/playground/L3mAUr9w/shared" frameBorder="0" width="100%" height="378" name="L3mAUr9w"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^3)$$ where $$N$$ is the length of `s`.  For each of $$O(N^2)$$ possible states representing a subarray of `s`, we perform $$O(N)$$ work iterating through `k`.

* Space Complexity: $$O(N^2)$$, the size of our `memo`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
