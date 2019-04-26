# 0446 - Arithmetic Slices II - Subsequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/arithmetic-slices-ii-subsequence) | [solution](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solution/)


-----------

<p>A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>

<p>For example, these are arithmetic sequences:</p>

<pre>
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>The following sequence is not arithmetic.</p>

<pre>
1, 1, 2, 5, 7</pre>
&nbsp;

<p>A zero-indexed array A consisting of N numbers is given. A <b>subsequence</b> slice of that array is any sequence of integers (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) such that 0 &le; P<sub>0</sub> &lt; P<sub>1</sub> &lt; ... &lt; P<sub>k</sub> &lt; N.</p>

<p>A <b>subsequence</b> slice (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) of array A is called arithmetic if the sequence A[P<sub>0</sub>], A[P<sub>1</sub>], ..., A[P<sub>k-1</sub>], A[P<sub>k</sub>] is arithmetic. In particular, this means that k &ge; 2.</p>

<p>The function should return the number of arithmetic subsequence slices in the array A.</p>

<p>The input contains N integers. Every integer is in the range of -2<sup>31</sup> and 2<sup>31</sup>-1 and 0 &le; N &le; 1000. The output is guaranteed to be less than 2<sup>31</sup>-1.</p>
&nbsp;

<p><b>Example:</b></p>

<pre>
<b>Input:</b> [2, 4, 6, 8, 10]

<b>Output:</b> 7

<b>Explanation:</b>
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
</pre>


-----------


## Similar Problems

- [Medium] [Arithmetic Slices](arithmetic-slices)




## Solution:

[TOC]

#### Approach #1 Brute Force [Time Limit Exceeded]

**Intuition**

Enumerate all possible subsequences to see if they are arithmetic sequences.

**Algorithm**

We can use depth-first search to generate all subsequences. We can check a Subsequence is arithmetic or not by its definition.


<iframe src="https://leetcode.com/playground/yNoZjyFt/shared" frameBorder="0" width="100%" height="500" name="yNoZjyFt"></iframe>

**Complexity Analysis**

* Time complexity : $$O(2^n)$$. For each element in the array, it can be in or outside the subsequence. So the time complexity is $$O(2^n)$$.

* Space complexity : $$O(n)$$. We only need the space to store the array.

---
#### Approach #2 Dynamic Programming [Accepted]

**Intuition**

To determine an arithmetic sequence, we need at least two parameters: the first (or last) element of the sequence, and the common difference.


**Algorithm**

Starting from this point, we can easily figure out that one state representation that may work:

> `f[i][d]` denotes the number of arithmetic subsequences that ends with `A[i]` and its common difference is `d`.

Let's try to find the state transitions based on the representation above. Assume we want to append a new element `A[i]` to existing arithmetic subsequences to form new subsequences. We can append `A[i]` to an existing arithmetic subsequence, only if the difference between the sequence's last element and `A[i]` is equal to the sequence's common difference.

Thus, we can define the state transitions for the element `A[i]` intuitively :

> for all `j < i`, f[i][A[i] - A[j]] += f[j][A[i] - A[j]].

This demonstrates the appending process above to form new arithmetic subsequences.

But here comes the problem. Initially all `f[i][d]` are set to be `0`, but how can we form a new arithmetic subsequence if there are no existing subsequences before?

In the original definition of arithmetic subsequences, the length of the subsequence must be at least `3`. This makes it hard to form new subsequences if only two indices `i` and `j` are given. How about taking the subsequences of length `2` into account?

We can define `weak arithmetic subsequences` as follows:

> **Weak arithmetic subsequences** are subsequences that  consist of at least two elements and if the difference between any two consecutive elements is the same.

There are two properties of weak arithmetic subsequences that are very useful:

- For any pair `i, j (i != j)`, `A[i]` and `A[j]` can always form a weak arithmetic subsequence.

- If we can append a new element to a weak arithmetic subsequence and keep it arithmetic, then the new subsequence must be an arithmetic subsequence.

The second property is quite trival, because the only difference between arithmetic subsequences and weak arithmetic subsequences is their length.

Thus we can change the state representations accordingly:

> `f[i][d]` denotes the number of weak arithmetic subsequences that ends with `A[i]` and its common difference is `d`.

Now the state transitions are quite straightforward:

> for all `j < i`, f[i][A[i] - A[j]] += (f[j][A[i] - A[j]] + 1).

The `1` appears here because of the property one, we can form a new weak arithmetic subsequence for the pair `(i, j)`.

Now the number of all weak arithmetic subsequences is the sum of all `f[i][d]`. But how can we get the number of arithmetic subsequences that are not `weak`?

There are two ways:

- First, we can count the number of `pure weak` arithmetic subsequences directly. The `pure weak` arithmetic subsequences are the arithmetic subsequences of length `2`, so the number of `pure weak` arithmetic subsequences should be equal to the number of pairs `(i, j)`, which is $$\binom{n}{2} = \frac{n * (n - 1)}{2}.$$

- Second, for the summation `f[i][A[i] - A[j]] += (f[j][A[i] - A[j]] + 1)`, `f[j][A[i] - A[j]]` is the number of existing weak arithmetic subsequences, while `1` is the new subsequence built with `A[i]` and `A[j]`. Based on property two, when we are appending new elements to existing weak arithmetic subsequences, we are forming arithmetic subsequences. So the first part, `f[j][A[i] - A[j]]` is the number of new formed arithmetic subsequences, and can be added to the answer.

We can use the following example to illustrate the process:

> [1, 1, 2, 3, 4, 5]

We need to count the answer for the above sequence.

- For the first element `1`, there is no element in front of it, the answer remains `0`.

- For the second element `1`, the element itself with the previous `1` can form a pure weak arithmetic subsequence with common difference `0` : `[1, 1]`.

- For the third element `2`, it cannot be appended to the only weak arithmetic subsequence `[1, 1]`, so the answer remains `0`. Similar to the second element, it can form new weak arithmetic subsequences `[1, 2]` and `[1, 2]`.

- For the forth element `3`, if we append it to some arithmetic subsequences ending with `2`, these subsequences must have a common difference of `3 - 2 = 1`. Indeed there are two: `[1, 2]` and `[1, 2]`. So we can append `3` to the end of these subsequences, and the answer is added by `2`. Similar to above, it can form new weak arithmetic subsequences `[1, 3], [1, 3]` and `[2, 3]`.

- The other elements are the same, we can view the process in the figure below. The red bracket indicates the weak arithmetic subsequence of length `2`, and the black bracket indicates the arithmetic subsequence. The answer should be the total number of black brackets.

<img src="../Figures/446_Arithmetic_Slices_II_Subsequence.png" width=80% height=80% />

<iframe src="https://leetcode.com/playground/MVagoidb/shared" frameBorder="0" width="100%" height="446" name="MVagoidb"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n ^ 2)$$. We can use double loop to enumerate all possible states.

* Space complexity : $$O(n ^ 2)$$. For each `i`, we need to store at most `n` distinct common differences, so the total space complexity is $$O(n ^ 2)$$.
