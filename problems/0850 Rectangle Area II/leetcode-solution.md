# 0850 - Rectangle Area II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Segment Tree | [Leetcode](https://leetcode.com/problems/rectangle-area-ii) | [solution](https://leetcode.com/problems/rectangle-area-ii/solution/)


-----------

<p>We are given a list of (axis-aligned)&nbsp;<code>rectangles</code>.&nbsp; Each&nbsp;<code>rectangle[i] = [x1, y1, x2, y2]&nbsp;</code>, where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the <code>i</code>th rectangle.</p>

<p>Find the total area covered by all <code>rectangles</code> in the plane.&nbsp; Since the answer&nbsp;may be too large, <strong>return it modulo 10^9 + 7</strong>.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="width: 480px; height: 360px;" /></p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
<strong>Output: </strong>6
<strong>Explanation: </strong>As illustrated in the picture.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[0,0,1000000000,1000000000]]
<strong>Output: </strong>49
<strong>Explanation: </strong>The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 200</code></li>
	<li><code><font face="monospace">rectanges[i].length = 4</font></code></li>
	<li><code>0 &lt;= rectangles[i][j] &lt;= 10^9</code></li>
	<li>The total area covered by all rectangles will never exceed&nbsp;<code>2^63 - 1</code>&nbsp;and thus will fit in a 64-bit signed integer.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]


## Solution
---
#### Approach #1: Principle of Inclusion-Exclusion

**Intuition**

Say we have two rectangles, $$A$$ and $$B$$.  The area of their union is:

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

Say we have three rectangles, $$A, B, C$$.  The area of their union is:

$$
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|
$$

This can be seen by drawing a Venn diagram.

Say we have four rectangles, $$A, B, C, D$$.  The area of their union is:

$$
\begin{align}
|A \cup B \cup C \cup D| =\,&\left( |A| + |B| + |C| + |D| \right) - \\
\,&\left(|A \cap B| + |A \cap C| + |A \cap D| + |B \cap C| + |B \cap D| + |C \cap D|\right) +\\
\,&\left(|A \cap B \cap C| + |A \cap B \cap D| + |A \cap C \cap D| + |B \cap C \cap D|\right) -\\
\,&\left(|A \cap B \cap C \cap D|\right)
\end{align}
$$

In general, the area of the union of $$n$$ rectangles $$A_1, A_2, \cdots , A_n$$ will be:

$$
\bigg|\bigcup_{i=1}^n A_i\bigg| = \sum_{\emptyset \neq S \subseteq [n]} (-1)^{|S| + 1} \bigg| \bigcap_{i \in S} A_i \bigg|
$$

**Algorithm**

If we do not know the above fact, we can prove it by considering any point in $$\bigg|\bigcup_{i=1}^n A_i\bigg|$$.  Say this point occurs in all $$A_i (i \in S)$$, and let $$|S| = n$$.  Then on the right side, it is counted $$\binom{n}{1} - \binom{n}{2} + \binom{n}{3} - \cdots \pm \binom{n}{n}$$ times.  By considering the binomial expansion of $$(1 - 1)^n$$, this is in fact equal to $$1$$.

From *Rectangle Area I*, we know that the intersection of two axis-aligned rectangles is another axis-aligned rectangle (or nothing).  So in particular, the intersection $$\bigcap_{i \in S} A_i$$ is always a rectangle (or nothing).

Now our algorithm proceeds as follows:  for every subset $$S$$ of $$\{1, 2, 3, \cdots, N\}$$ (where $$N$$ is the number of rectangles), we'll calculate the intersection of the rectangles in that subset $$\bigcap_{i \in S} A_i$$, and then the area of that rectangle.  This allows us to calculate algorithmically the right-hand side of the general equation we wrote earlier.

<iframe src="https://leetcode.com/playground/LVWa7ckv/shared" frameBorder="0" width="100%" height="500" name="LVWa7ckv"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * 2^N)$$, where $$N$$ is the number of rectangles.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach #2: Coordinate Compression

**Intuition**

<center>
    <img src="../Figures/850/example.png" alt="Image from problem description" style="height: 200px;"/>
</center>

Suppose instead of `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`, we had `[[0,0,200,200],[100,0,200,300],[100,0,300,100]]`.  The answer would just be 100 times bigger.

What about if `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,30002,1]]` ?  Only the blue region would have area `30000` instead of `1`.

Our idea is this: we'll take all the `x` and `y` coordinates, and re-map them to `0, 1, 2, ...` etc.  For example, if `rectangles  = [[0,0,200,200],[100,0,200,300],[100,0,300,100]]`, we could re-map it to `[[0,0,2,2],[1,0,2,3],[1,0,3,1]]`.  Then, we can solve the problem with brute force.  However, each region may actually represent some larger area, so we'll need to adjust for that at the end.

**Algorithm**

Re-map each `x` coordinate to `0, 1, 2, ...`.  Independently, re-map all `y` coordinates too.

We then have a problem that can be solved by brute force: for each rectangle with re-mapped coordinates `(rx1, ry1, rx2, ry2)`, we can fill the grid `grid[x][y] = True` for `rx1 <= x < rx2` and `ry1 <= y < ry2`.

Afterwards, each `grid[rx][ry]` represents the area `(imapx(rx+1) - imapx(rx)) * (imapy(ry+1) - imapy(ry))`, where if `x` got remapped to `rx`, then `imapx(rx) = x` ("inverse-map-x of remapped-x equals x"), and similarly for `imapy`.

<iframe src="https://leetcode.com/playground/hp6mu9MY/shared" frameBorder="0" width="100%" height="500" name="hp6mu9MY"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the number of rectangles.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---
#### Approach #3: Line Sweep

**Intuition**

Imagine we pass a horizontal line from bottom to top over the shape.  We have some active intervals on this horizontal line, which gets updated twice for each rectangle.  In total, there are $$2 * N$$ events, and we can update our (up to $$N$$) active horizontal intervals for each update.

**Algorithm**

For a rectangle like `rec = [1,0,3,1]`, the first update is to add `[1, 3]` to the active set at `y = 0`, and the second update is to remove `[1, 3]` at `y = 1`.  Note that adding and removing respects multiplicity - if we also added `[0, 2]` at `y = 0`, then removing `[1, 3]` at `y = 1` will still leave us with `[0, 2]` active.

This gives us a plan: create these two events for each rectangle, then process all the events in sorted order of `y`.  The issue now is deciding how to process the events `add(x1, x2)` and `remove(x1, x2)` such that we are able to `query()` the total horizontal length of our active intervals.

We can use the fact that our `remove(...)` operation will always be on an interval that was previously added.  Let's store all the `(x1, x2)` intervals in sorted order.  Then, we can `query()` in linear time using a technique similar to a classic LeetCode problem, [Merge Intervals](https://leetcode.com/problems/merge-intervals/).

<iframe src="https://leetcode.com/playground/vyrMx2Y9/shared" frameBorder="0" width="100%" height="500" name="vyrMx2Y9"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2 \log N)$$, where $$N$$ is the number of rectangles.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach #4: Segment Tree

**Intuition and Algorithm**

As in *Approach #3*, we want to support `add(x1, x2)`, `remove(x1, x2)`, and `query()`.  While outside the scope of a typical interview, this is the perfect setting for using a *segment tree*.  For completeness, we include the following implementation.

You can learn more about Segment Trees by visiting the articles of these problems: [Falling Squares](https://leetcode.com/problems/falling-squares/), [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/).


<iframe src="https://leetcode.com/playground/MmabC4t6/shared" frameBorder="0" width="100%" height="500" name="MmabC4t6"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the number of rectangles.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).  Idea for Solution #4 by [@lee215](http://leetcode.com/lee215).
