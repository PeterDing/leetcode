# 0007 - Reverse Integer

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/reverse-integer) | [solution](https://leetcode.com/problems/reverse-integer/solution/)


-----------

<p>Given a 32-bit signed integer, reverse digits of an integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 123
<strong>Output:</strong> 321
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -123
<strong>Output:</strong> -321
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 120
<strong>Output:</strong> 21
</pre>

<p><strong>Note:</strong><br />
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.</p>


-----------


## Similar Problems

- [Medium] [String to Integer (atoi)](string-to-integer-atoi)

- [Easy] [Reverse Bits](reverse-bits)




## Solution:

[TOC]

## Solution
---

#### Approach 1: Pop and Push Digits & Check before Overflow

**Intuition**

We can build up the reverse integer one digit at a time.
While doing so, we can check beforehand whether or not appending another digit would cause overflow.

**Algorithm**

Reversing an integer can be done similarly to reversing a string.

We want to repeatedly "pop" the last digit off of $$x$$ and "push" it to the back of the $$\text{rev}$$. In the end, $$\text{rev}$$ will be the reverse of the $$x$$.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.

```cpp
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```

However, this approach is dangerous, because the statement $$\text{temp} = \text{rev} \cdot 10 + \text{pop}$$ can cause overflow.

Luckily, it is easy to check beforehand whether or this statement would cause an overflow.

To explain, lets assume that $$\text{rev}$$ is positive.

1. If $$temp = \text{rev} \cdot 10 + \text{pop}$$ causes overflow, then it must be that $$\text{rev} \geq \frac{INTMAX}{10}$$
2. If $$\text{rev} > \frac{INTMAX}{10}$$, then $$temp = \text{rev} \cdot 10 + \text{pop}$$ is guaranteed to overflow.
3. If $$\text{rev} == \frac{INTMAX}{10}$$, then $$temp = \text{rev} \cdot 10 + \text{pop}$$ will overflow if and only if $$\text{pop} > 7$$

Similar logic can be applied when $$\text{rev}$$ is negative.

<iframe src="https://leetcode.com/playground/Ufhk9yCy/shared" frameBorder="0" width="100%" height="293" name="Ufhk9yCy"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(\log(x))$$. There are roughly $$\log_{10}(x)$$ digits in $$x$$.
* Space Complexity: $$O(1)$$.
