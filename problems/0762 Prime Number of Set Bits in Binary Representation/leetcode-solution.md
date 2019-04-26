# 0762 - Prime Number of Set Bits in Binary Representation

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Bit Manipulation | [Leetcode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation) | [solution](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solution/)


-----------

<p>
Given two integers <code>L</code> and <code>R</code>, find the count of numbers in the range <code>[L, R]</code> (inclusive) having a prime number of set bits in their binary representation.
</p><p>
(Recall that the number of set bits an integer has is the number of <code>1</code>s present when written in binary.  For example, <code>21</code> written in binary is <code>10101</code> which has 3 set bits.  Also, 1 is not a prime.)
</p><p>

<p><b>Example 1:</b><br /><pre>
<b>Input:</b> L = 6, R = 10
<b>Output:</b> 4
<b>Explanation:</b>
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
</pre></p>

<p><b>Example 2:</b><br /><pre>
<b>Input:</b> L = 10, R = 15
<b>Output:</b> 5
<b>Explanation:</b>
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
</pre></p>

<p><b>Note:</b><br><ol>
<li><code>L, R</code> will be integers <code>L <= R</code> in the range <code>[1, 10^6]</code>.</li>
<li><code>R - L</code> will be at most 10000.</li>
</ol></p>

-----------


## Similar Problems

- [Easy] [Number of 1 Bits](number-of-1-bits)




## Solution:

[TOC]
#### Approach #1: Direct [Accepted]
**Intuition and Approach**

For each number from `L` to `R`, let's find out how many set bits it has.  If that number is `2, 3, 5, 7, 11, 13, 17`, or `19`, then we add one to our count.  We only need primes up to 19 because $$R \leq 10^6 < 2^{20}$$.

<iframe src="https://leetcode.com/playground/GCVcZ6pE/shared" frameBorder="0" width="100%" height="276" name="GCVcZ6pE"></iframe>

**Complexity Analysis**
    
* Time Complexity: $$O(D)$$, where $$D = R-L$$ is the number of integers considered.  In a bit complexity model, this would be $$O(D\log D)$$ as we have to count the bits in $$O(\log D)$$ time.

* Space Complexity: $$O(1)$$.

---
Analysis written by: [@awice](https://leetcode.com/awice).
