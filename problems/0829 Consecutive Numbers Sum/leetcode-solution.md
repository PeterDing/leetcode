# 0829 - Consecutive Numbers Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math | [Leetcode](https://leetcode.com/problems/consecutive-numbers-sum) | [solution](https://leetcode.com/problems/consecutive-numbers-sum/solution/)


-----------

<p>Given a positive integer&nbsp;<code>N</code>, how many ways can we write it as a sum of&nbsp;consecutive positive integers?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>5
<strong>Output: </strong>2
<strong>Explanation: </strong>5 = 5 = 2 + 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>9
<strong>Output: </strong>3
<strong>Explanation: </strong>9 = 9 = 4 + 5 = 2 + 3 + 4</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>15
<strong>Output: </strong>4
<strong>Explanation: </strong>15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5</pre>

<p><strong>Note:</strong>&nbsp;<code>1 &lt;= N &lt;= 10 ^ 9</code>.</p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Brute Force [Time Limit Exceeded]

**Intuition and Algorithm**

For each starting number, we scan forward until we meet or exceed the target `N`.  If we meet it, then it represents one way to write `N` as a sum of consecutive numbers.

For example, if `N = 6`, and we scan forward from `1`, we'll get `1 + 2 + 3 = 6` which contributes to the answer.  If we scan forward from `2`, we'll get `2 + 3 + 4` (the first time that the sum is `>= N`) which is too big.

<iframe src="https://leetcode.com/playground/W5wabBJ4/shared" frameBorder="0" width="100%" height="259" name="W5wabBJ4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$.

* Space Complexity: $$O(1)$$.

---
#### Approach #2: Mathematical (Naive) [Time Limit Exceeded]

**Intuition and Algorithm**

We can model the situation by the equation $$N = (x+1) + (x+2) + \cdots + (x+k)$$.  Here, $$x \geq 0, k \geq 1$$.  Using the identity $$1 + 2 + \cdots + k = \frac{k(k+1)}{2}$$, we can simplify this equation to $$2*N = k(2*x + k + 1)$$.

From here, clearly $$1 \leq k \leq 2*N$$.  We can try every such $$k$$.  We need $$x = \frac{\frac{2*N}{k} - k - 1}{2}$$ to be a non-negative integer for a solution to exist for the $$k$$ we are trying.


<iframe src="https://leetcode.com/playground/y3LRDRHT/shared" frameBorder="0" width="100%" height="276" name="y3LRDRHT"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$.

* Space Complexity: $$O(1)$$.


---
#### Approach #3: Mathematical (Fast) [Accepted]

**Intuition and Algorithm**

As in *Approach #2*, $$2*N = k(2*x + k + 1)$$ with $$x \geq 0, k \geq 1$$.  Call $$k$$ the first factor, and $$2*x + k + 1$$ the second factor.  We are looking for ways to solve this equation without trying all $$2*N$$ possibilities.

Now notice that the parity of $$k$$ and $$(2*x + k + 1)$$ are different.  That is, if $$k$$ is even then the other quantity is odd, and vice versa.  Also, $$2*x + k + 1 \geq k + 1 > k$$, so the second factor must be bigger.

Now write $$2N = 2^\alpha * M$$ where $$M$$ is odd.  If we factor $$M = a * b$$, then two candidate solutions are $$k = a, 2x+k+1 = b * 2^\alpha$$, or $$k = a * 2^\alpha, 2x+k+1 = b$$.  However, only one of these solutions will have the second factor larger than the first.  (Because $$\alpha \geq 1$$, we are guaranteed that one factor is strictly larger.)

Thus, the answer is the number of ways to factor the odd part of $$N$$.


<iframe src="https://leetcode.com/playground/RNh28dQE/shared" frameBorder="0" width="100%" height="378" name="RNh28dQE"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\sqrt(N))$$.

* Space Complexity: $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
