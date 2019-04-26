# 0923 - 3Sum With Multiplicity

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers | [Leetcode](https://leetcode.com/problems/3sum-with-multiplicity) | [solution](https://leetcode.com/problems/3sum-with-multiplicity/solution/)


-----------

<p>Given an integer array <code>A</code>, and an integer <code>target</code>, return the number of&nbsp;tuples&nbsp;<code>i, j, k</code>&nbsp; such that <code>i &lt; j &lt; k</code> and&nbsp;<code>A[i] + A[j] + A[k] == target</code>.</p>

<p><strong>As the answer can be very large, return it modulo&nbsp;<code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,1,2,2,3,3,4,4,5,5]</span>, target = <span id="example-input-1-2">8</span>
<strong>Output: </strong><span id="example-output-1">20</span>
<strong>Explanation: </strong>
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,1,2,2,2,2]</span>, target = <span id="example-input-2-2">5</span>
<strong>Output: </strong><span id="example-output-2">12</span>
<strong>Explanation: </strong>
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 3000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 100</code></li>
	<li><code>0 &lt;= target &lt;= 300</code></li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach Notes

The approaches described below assume some familiarity with the two pointer technique that can be used to solve the LeetCode problem "Two Sum".

In the problem, we have a sorted array `A` of unique elements, and want to know how many `i < j` with `A[i] + A[j] == target`.

The idea that does it in linear time, is that for each `i` in increasing order, the `j`'s that satisfy the equation `A[i] + A[j] == target` are decreasing.

```python
def solve(A, target):
    # Assume A already sorted
    i, j = 0, len(A) - 1
    ans = 0
    while i < j:
        if A[i] + A[j] < target:
            i += 1
        elif A[i] + A[j] > target:
            j -= 1
        else:
            ans += 1
            i += 1
            j -= 1
    return ans
```

This is not a complete explanation.  For more on this problem, please review the LeetCode problem "Two Sum".

---
#### Approach 1: Three Pointer

**Intuition and Algorithm**

Sort the array.  For each `i`, set `T = target - A[i]`, the remaining target.  We can try using a two-pointer technique to find `A[j] + A[k] == T`.  This approach is the natural continuation of trying to make the two-pointer technique we know from previous problems, work on this problem.

Because some elements are duplicated, we have to be careful.  In a typical case, the target is say, `8`, and we have a remaining array (`A[i+1:]`) of `[2,2,2,2,3,3,4,4,4,5,5,5,6,6]`.  We can analyze this situation with cases.

Whenever `A[j] + A[k] == T`, we should count the multiplicity of `A[j]` and `A[k]`.  In this example, if `A[j] == 2` and `A[k] == 6`, the multiplicities are `4` and `2`, and the total number of pairs is `4 * 2 = 8`.  We then move to the remaining window `A[j:k+1]` of `[3,3,4,4,4,5,5,5]`.

As a special case, if `A[j] == A[k]`, then our manner of counting would be incorrect.  If for example the remaining window is `[4,4,4]`, there are only 3 such pairs.  In general, when `A[j] == A[k]`, we have $$\binom{M}{2} = \frac{M*(M-1)}{2}$$ pairs `(j,k)` (with `j < k`) that satisfy `A[j] + A[k] == T`, where $$M$$ is the multiplicity of `A[j]` (in this case $$M=3$$).

For more details, please see the inline comments.

<iframe src="https://leetcode.com/playground/TCrTgDfK/shared" frameBorder="0" width="100%" height="500" name="TCrTgDfK"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
#### Approach 2: Counting with Cases

**Intuition and Algorithm**

Let `count[x]` be the number of times that `x` occurs in `A`.  For every `x+y+z == target`, we can try to count the correct contribution to the answer.  There are a few cases:

* If `x`, `y`, and `z` are all different, then the contribution is `count[x] * count[y] * count[z]`.

* If `x == y != z`, the contribution is $$\binom{\text{count[x]}}{2} * \text{count[z]}$$.

* If `x != y == z`, the contribution is $$\text{count[x]} * \binom{\text{count[y]}}{2}$$.

* If `x == y == z`, the contribution is $$\binom{\text{count[x]}}{3}$$.

(*Here, $$\binom{n}{k}$$ denotes the binomial coefficient $$\frac{n!}{(n-k)!k!}$$.*)

Each case is commented in the implementations below.

<iframe src="https://leetcode.com/playground/9nU5mTcv/shared" frameBorder="0" width="100%" height="500" name="9nU5mTcv"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + W^2)$$, where $$N$$ is the length of `A`, and $$W$$ is the maximum possible value of `A[i]`.  (Note that this solution can be adapted to be $$O(N^2)$$ even in the case that $$W$$ is very large.)

* Space Complexity:  $$O(W)$$.
<br />
<br />


---
#### Approach 3: Adapt from Three Sum

**Intuition and Algorithm**

As in *Approach 2*, let `count[x]` be the number of times that `x` occurs in `A`.  Also, let `keys` be a sorted list of unique values of `A`.  We will try to adapt a 3Sum algorithm to work on `keys`, but add the correct answer contributions.

For example, if `A = [1,1,2,2,3,3,4,4,5,5]` and `target = 8`, then `keys = [1,2,3,4,5]`.  When doing 3Sum on `keys` (with `i <= j <= k`), we will encounter some tuples that sum to the target, like `(x,y,z) = (1,2,5), (1,3,4), (2,2,4), (2,3,3)`.  We can then use `count` to calculate how many such tuples there are in each case.

This approach assumes familiarity with *3Sum*.  For more, please visit the associated LeetCode problem here [https://leetcode.com/problems/3sum](https://leetcode.com/problems/3sum).

<iframe src="https://leetcode.com/playground/Ph3ok9qb/shared" frameBorder="0" width="100%" height="500" name="Ph3ok9qb"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
