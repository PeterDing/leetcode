# 0866 - Prime Palindrome

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math | [Leetcode](https://leetcode.com/problems/prime-palindrome) | [solution](https://leetcode.com/problems/prime-palindrome/solution/)


-----------

<p>Find the smallest prime palindrome greater than or equal to <code>N</code>.</p>

<p>Recall that a&nbsp;number is <em>prime</em> if it&#39;s only divisors are 1 and itself, and it is greater than 1.&nbsp;</p>

<p>For example, 2,3,5,7,11 and 13 are&nbsp;primes.</p>

<p>Recall that a number is a <em>palindrome</em> if it reads the same from left to right as it does from right to left.&nbsp;</p>

<p>For example, 12321 is a palindrome.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">6</span>
<strong>Output: </strong><span id="example-output-1">7</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">8</span>
<strong>Output: </strong><span id="example-output-2">11</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">13</span>
<strong>Output: </strong><span id="example-output-3">101</span></pre>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 10^8</code></li>
	<li>The answer is guaranteed to exist and be less than <code>2 * 10^8</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach Framework

**Investigation of Brute Force**

Let's investigate and improve on a brute force method.

With basic methods, we can check whether an integer $$N$$ is a palindrome in $$O(\log N)$$ time, and check whether it is prime in $$O(\sqrt{N})$$ time.  So we would probably like to do the palindrome check first.

Now, say we naively check every number $$N, N+1, \cdots, N+K$$.  How big is $$K$$?

Well, the palindromes could be approximately $$10^4$$ apart, since for example `99988999`'s next palindrome is `99999999`.  

If we assume being a palindrome and being a prime is independent, then based on the density of primes, $$K \approx 10^4 \log N$$, and we would do a palindrome check on approximately $$10^4 \log^2 N$$ values, and a primality test on $$\log N$$ values of complexity $$\sqrt{N} \log N$$.  This seems to work.

However, we can't make this assumption of independence: whether a number is a palindrome or prime are *negatively correlated* events!  For example, $$22, 33, 44, \cdots, 99$$ are clearly not prime.  Actually, all palindromes with an even number of digits are divisible by 11, and are therefore not prime!  (Except for 11.)  For example, an 8 digit palindrome can be written as:

$$\sum_{i=0}^{3} a_i(10^{7-i} + 10^i) \equiv \sum a_i((-1)^{7-i} + (-1)^i) \equiv \sum a_i(0) \equiv 0 \pmod{11}$$

where the second-last equivalence follows as $$i$$ and $$7-i$$ have different parity.

**Density of Palindromes**

For a palindrome of $$d$$ digits, choosing the first $$k = \lfloor \frac{d+1}{2} \rfloor$$ digits uniquely determines the remaining digits.  Hence, there are $$9 * 10^{k-1}$$ of them (the first digit can't be 0.)  Thus, there are

$$9(10^0 + 10^0 + 10^1 + 10^1 + 10^2 + 10^2 + 10^3 + 10^3) < 20000$$

palindromes of 8 digits or less.  

Actually, we don't need to check the palindromes with an even number of digits, so there are under 10000 palindromes we need to check.  However, we also need to check palindromes until we encounter the first 9 digit prime palindrome, as all 8 digit numbers $$N$$ will have an answer equal to that.  Luckily, it occurs quickly: `100030001` is the 4th 9-digit value checked.  (We can verify this with brute force.)

For each palindrome, we can test whether it is prime in $$O(\sqrt{N})$$ operations.  So in total, an approach centered around enumerating palindromes seems like it will succeed.
<br />
<br />


---
#### Approach 1: Iterate Palindromes

**Intuition**

Say we have a palindrome $$X$$.  What is the next palindrome?

Each palindrome of $$d$$ digits has a *palindromic root*, it's first $$k = \frac{d+1}{2}$$ digits.  The next palindrome is formed by the next root.

For example, if $$123$$ is a root for the 5 digit palindrome $$12321$$, then the next palindrome is $$12421$$ with root $$124$$.

Notice that roots and palindromes are not a bijection, as palindromes $$123321$$ and $$12321$$ have the same root.

**Algorithm**

For each *palindromic root*, let's find the two associated palindromes (one with an odd number of digits, and one with an even number.)  For roots with $$k$$ digits, they will generate palindromes of $$2*k - 1$$ and $$2*k$$ digits.

If we didn't know that palindromes with an even number of digits (and greater than 11) are never prime, we're still fine - we can just check both possibilities.  When checking both possibilities, we check the palindromes with $$2k - 1$$ digits first, as they are all smaller than the palindromes with $$2k$$ digits.

We'll use an idea from [[LeetCode Problem: Reverse an Integer]](https://leetcode.com/problems/reverse-integer), in order to check whether an integer is a palindrome.  We could have also converted the integer to a string, and checked the indices directly.

As for testing primes with `isPrime(N)`, we'll use the standard $$O(\sqrt{N})$$ check: testing whether every number $$\leq \sqrt{N}$$ is a divisor of $$N$$.

<iframe src="https://leetcode.com/playground/UgnkELMD/shared" frameBorder="0" width="100%" height="500" name="UgnkELMD"></iframe>

**Complexity Analysis**

* Time Complexity:  Based on our analysis above, we performed on the order of $$O(N)$$ operations (not counting log factors from dealing with integers), given we knew the existence of prime palindrome `100030001`.  

  Interestingly, the time complexity is an open problem in mathematics, as it is not even known whether there are infinitely many prime palindromes, or whether palindromes behave as random integers for our purposes here - see [["Almost All Palindromes are Composite"]](https://arxiv.org/pdf/math/0405056.pdf) for more.

* Space Complexity:  $$O(\log N)$$, the space used by `s` (or `sb` in Java.)
<br />
<br />


---
#### Approach 2: Brute Force with Mathematical Shortcut

**Intuition**

Our brute force works except when $$N$$ is 8 digits (as explained in *Approach Framework* when we established that all 8 digit palindromes are not prime), so we can skip all 8 digit numbers.

**Algorithm**

For each number, check whether it is a palindrome.  If it is, check whether it is a prime.  If the number is 8 digits, skip to the 9 digit numbers.

<iframe src="https://leetcode.com/playground/NSw4owuf/shared" frameBorder="0" width="100%" height="500" name="NSw4owuf"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, with the caveats explained in *Approach #1*, and ignoring the $$\log N$$ factor when checking an integer for palindromes.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
