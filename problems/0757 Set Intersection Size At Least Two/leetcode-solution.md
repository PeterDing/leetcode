# 0757 - Set Intersection Size At Least Two

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Greedy | [Leetcode](https://leetcode.com/problems/set-intersection-size-at-least-two) | [solution](https://leetcode.com/problems/set-intersection-size-at-least-two/solution/)


-----------

<p>
An integer interval <code>[a, b]</code> (for integers <code>a < b</code>) is a set of all consecutive integers from <code>a</code> to <code>b</code>, including <code>a</code> and <code>b</code>.
</p><p>
Find the minimum size of a set S such that for every integer interval A in <code>intervals</code>, the intersection of S with A has size at least 2.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
<b>Output:</b> 3
<b>Explanation:</b>
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
<b>Output:</b> 5
<b>Explanation:</b>
An example of a minimum sized set is {1, 2, 3, 4, 5}.
</pre>
</p>

<p><b>Note:</b><br><ol>
<li><code>intervals</code> will have length in range <code>[1, 3000]</code>.</li>
<li><code>intervals[i]</code> will have length <code>2</code>, representing some integer interval.</li>
<li><code>intervals[i][j]</code> will be an integer in <code>[0, 10^8]</code>.</li>
</ol></p>

-----------


## Similar Problems




## Solution:

[TOC]

#### Approach #1: Greedy [Accepted]

**Intuition**

Let's try to solve a simpler problem: what is the answer when the set intersection size is at least *one*?

Sort the points.  Take the last interval `[s, e]`, which point on this interval will be in `S`?  Since every other interval has start point `<= s`, it is strictly better to choose `s` as the start.  So we can repeatedly take `s` in our set `S` and remove all intervals containing `s`.

We will try to extend this solution to the case when we want an intersection of size two.

**Algorithm**

For each interval, we will perform the algorithm described above, storing a `todo` *multiplicity* which starts at `2`.  As we identify points in `S`, we will subtract from these multiplicities as appropriate.

One case that is important to handle is the following:
`[[1, 2], [2, 3], [2, 4], [4, 5]]`.  If we put `4, 5` in `S`, then we put `2` in `S`, when handling `[2, 3]` we need to put `3` in `S`, not `2` which was already put.

We can handle this case succinctly by sorting intervals `[s, e]` by `s` ascending, then `e` descending.  This makes it so that any interval encountered with the same `s` has the lowest possible `e`, and so it has the highest *multiplicity*.  When at interval `[s, e]` and choosing points to be included into `S`, it will always be the case that the start of the interval (either `s` or `s, s+1`) will be unused.

<iframe src="https://leetcode.com/playground/w4QM4e3U/shared" frameBorder="0" width="100%" height="412" name="w4QM4e3U"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the length of `intervals`.

* Space Complexity: $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
