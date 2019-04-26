# 0920 - Number of Music Playlists

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/number-of-music-playlists) | [solution](https://leetcode.com/problems/number-of-music-playlists/solution/)


-----------

<p>Your music player contains <code>N</code>&nbsp;different songs and she wants to listen to <code>L</code><strong> </strong>(not necessarily different) songs during your trip. &nbsp;You&nbsp;create&nbsp;a playlist so&nbsp;that:</p>

<ul>
	<li>Every song is played at least once</li>
	<li>A song can only be played again only if&nbsp;<code>K</code>&nbsp;other songs have been played</li>
</ul>

<p>Return the number of possible playlists.&nbsp; <strong>As the answer can be very large, return it modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, L = <span id="example-input-1-2">3</span>, K = <span id="example-input-1-3">1</span>
<strong>Output: </strong><span id="example-output-1">6
<strong>Explanation</strong>: </span><span>There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">2</span>, L = <span id="example-input-2-2">3</span>, K = <span id="example-input-2-3">0</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span id="example-output-1"><strong>Explanation</strong>: </span><span>There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">2</span>, L = <span id="example-input-3-2">3</span>, K = <span id="example-input-3-3">1</span>
<strong>Output: </strong><span id="example-output-3">2
<strong>Explanation</strong>: </span><span>There are 2 possible playlists. [1, 2, 1], [2, 1, 2]</span>
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= K &lt; N &lt;= L &lt;= 100</code></li>
</ol>
</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

Let `dp[i][j]` be the number of playlists of length `i` that have exactly `j` unique songs.  We want `dp[L][N]`, and it seems likely we can develop a recurrence for `dp`.

**Algorithm**

Consider `dp[i][j]`.  Last song, we either played a song for the first time or we didn't.  If we did, then we had `dp[i-1][j-1] * (N-j)` ways to choose it.  If we didn't, then we repeated a previous song in `dp[i-1][j] * max(j-K, 0)` ways (`j` of them, except the last `K` ones played are banned.)

<iframe src="https://leetcode.com/playground/9tJ8LAAB/shared" frameBorder="0" width="100%" height="327" name="9tJ8LAAB"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NL)$$.

* Space Complexity:  $$O(NL)$$.  (However, we can adapt this algorithm to only store the last row of `dp` to easily get $$O(L)$$ space complexity.)
<br />
<br />


---
#### Approach 2: Partitions + Dynamic Programming

(*Note: This solution is extremely challenging, but is a natural consequence of trying to enumerate the playlists in this manner.*)

**Intuition**

Since we are interested in playing every song at least once, let's keep track of what times $$x = (x_1, x_2, \cdots)$$ a song was played that wasn't yet played before.  For example, if we have 5 songs `abcde`, and we play `abacabdcbaeacbd`, then $$x = (1, 2, 4, 7, 11)$$ as these are the first occurrences of a unique song.  For convenience, we'll also put $$x_{N+1} = L+1$$.  Our strategy is to count the number of playlists $$\#_x$$ that satisfy this $$x$$, so that our final answer will be $$\sum \#_x$$.  

Doing a direct count,

$$
\#_x = N * (N-1) * \cdots * (N-K+1) 1^{x_{K+1} - x_K - 1} * (N-K+2)  2^{x_{K+2} - x_{K+1}} * \cdots
$$

$$
\Rightarrow \#_x = N! \prod_{j=1}^{N-K+1} j^{x_{K+j} - x_{K+j-1} - 1}
$$

Now, let $$\delta_i = x_{K+i} - x_{K+i-1} - 1$$, so that $$\sum \delta_i = L-N$$.  To recap, the final answer will be (for $$S = L-N, P = N-K+1$$):

$$
N! \Big(\sum\limits_{\delta : \sum\limits_{0 \leq i \leq P} \delta_i = S} \prod\limits_{j=1}^P j^{\delta_j} \Big)
$$

For convenience, let's denote the stuff in the large brackets as $$\langle S, P\rangle$$.

**Algorithm**

We can develop a recurrence for $$\langle S, P\rangle$$ mathematically, by factoring out the $$P^{\delta_P}$$ term.

$$
\langle S, P\rangle = \sum_{\delta_P = 0}^S P^{\delta_P} \sum_{\sum\limits_{0\leq i < P} \delta_i = S - \delta_P} \prod\limits_{j=1}^{P-1} j^{\delta_j}
$$

$$
\Rightarrow \langle S, P\rangle = \sum_{\delta_P = 0}^S P^{\delta_P} \langle S - \delta_P, P-1\rangle
$$

so that it can be shown through algebraic manipulation that:
$$
\langle S, P \rangle = P \langle S-1, P-1 \rangle + \langle S, P-1 \rangle
$$

With this recurrence, we can perform dynamic programming similar to Approach 1.  The final answer is $$N! \langle L-N, N-K+1 \rangle$$.

<iframe src="https://leetcode.com/playground/KdGurUUX/shared" frameBorder="0" width="100%" height="395" name="KdGurUUX"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NL)$$.

* Space Complexity:  $$O(L)$$.
<br />
<br />


---
#### Approach 3: Generating Functions

(*Note: This solution is extremely challenging and not recommended for interviews, but is included here for completeness.*)

**Analysis**

Following the terminology of Approach 2, we would like to compute $$\langle S, P \rangle$$ quickly.  We can use generating functions.

For a fixed $$P$$, consider the function:

$$
f(x) = (1^0x^0 + 1^1x^1 + 1^2x^2 + 1^3x^3 + \cdots) * (2^0x^0 + 2^1x^1 + 2^2x^2 + 2^3x^3 + \cdots)
$$
$$
\cdots * (P^0x^0 + P^1x^1 + P^2x^2 + P^3x^3 + \cdots)
$$

$$
\Leftrightarrow f(x) = \prod_{k=1}^{P} (\sum_{j \geq 0} k^j x^j) = \prod_{k=1}^P \frac{1}{1-kx}
$$

The coefficient of $$x^S$$ in $$f$$ (denoted $$[x^S]f$$) is the desired $$\langle S, P \rangle$$.

By the Chinese Remainder theorem on polynomials, this product can be written as a partial fraction decomposition:

$$
\prod_{k=1}^P \frac{1}{1-kx} = \sum_{k=1}^P \frac{A_k}{1-kx}
$$

for some rational coefficients $$A_k$$.  We can solve for these coefficients by clearing denominators and setting $$x = 1/m$$ for $$1 \leq m \leq P$$.  Then for a given $$m$$, all the terms except the $$m$$-th vanish, and:

$$
A_m = \frac{1}{\prod\limits_{\substack{1 \leq j \leq P\\j \neq m}} 1 - j/m} = \prod_{j \neq m} \frac{m}{m-j}
$$

Since a geometric series has sum $$\sum_{j \geq 0} (kx)^j = \frac{1}{1-kx}$$, altogether it implies:

$$
[x^S]f = \sum_{k=1}^P A_k * k^S
$$

so that the final answer is

$$
\text{answer} = N! \sum_{k=1}^{N-K} k^{L-N} \prod_{\substack{1 \leq j \leq N-K\\j \neq k}} \frac{k}{k-j}
$$

$$
\Rightarrow \text{answer} = N! \sum_k k^{L-K-1} \prod_{j \neq k} \frac{1}{k-j}
$$

We only need a quick way to compute $$C_k = \prod\limits_{j \neq k} \frac{1}{k-j}$$.  Indeed,

$$
C_{k+1} = C_k * \frac{k - (N-K)}{k}
$$

so that we now have everything we need to compute the answer quickly.


<iframe src="https://leetcode.com/playground/ypP5xqYU/shared" frameBorder="0" width="100%" height="395" name="ypP5xqYU"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log L)$$.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
