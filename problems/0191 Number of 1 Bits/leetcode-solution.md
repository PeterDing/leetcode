# 0191 - Number of 1 Bits

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Bit Manipulation | [Leetcode](https://leetcode.com/problems/number-of-1-bits) | [solution](https://leetcode.com/problems/number-of-1-bits/solution/)


-----------

<p>Write a function that takes an unsigned integer and return&nbsp;the number of &#39;1&#39;&nbsp;bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 00000000000000000000000000001011
<strong>Output:</strong> 3
<strong>Explanation: </strong>The input binary string <code><strong>00000000000000000000000000001011</strong>&nbsp;has a total of three &#39;1&#39; bits.</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 00000000000000000000000010000000
<strong>Output:</strong> 1
<strong>Explanation: </strong>The input binary string <strong>00000000000000000000000010000000</strong>&nbsp;has a total of one &#39;1&#39; bit.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 11111111111111111111111111111101
<strong>Output:</strong> 31
<strong>Explanation: </strong>The input binary string <strong>11111111111111111111111111111101</strong> has a total of thirty one &#39;1&#39; bits.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.</li>
	<li>In Java,&nbsp;the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2&#39;s complement notation</a>. Therefore, in <strong>Example 3</strong>&nbsp;above the input represents the signed integer <code>-3</code>.</li>
</ul>

<p>&nbsp;</p>

<p><b>Follow up</b>:</p>

<p>If this function is called many times, how would you optimize it?</p>


-----------


## Similar Problems

- [Easy] [Reverse Bits](reverse-bits)

- [Easy] [Power of Two](power-of-two)

- [Medium] [Counting Bits](counting-bits)

- [Easy] [Binary Watch](binary-watch)

- [Easy] [Hamming Distance](hamming-distance)

- [Easy] [Binary Number with Alternating Bits](binary-number-with-alternating-bits)

- [Easy] [Prime Number of Set Bits in Binary Representation](prime-number-of-set-bits-in-binary-representation)




## Solution:

## Solution
---

#### Approach #1 (Loop and Flip) [Accepted]

** Algorithm**

The solution is straight-forward. We check each of the $$32$$ bits of the number. If the bit is $$1$$, we add one to the number of $$1$$-bits.

We can check the $$i^{th}$$ bit of a number using a *bit mask*. We start with a mask $$m=1$$, because the binary representation of $$1$$ is,

$$
0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0001
$$
Clearly, a logical AND between any number and the mask $$1$$ gives us the least significant bit of this number. To check the next bit, we shift the mask to the left by one.

$$
0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0010
$$

And so on.

**Java**

```java
public int hammingWeight(int n) {
    int bits = 0;
    int mask = 1;
    for (int i = 0; i < 32; i++) {
        if ((n & mask) != 0) {
            bits++;
        }
        mask <<= 1;
    }
    return bits;
}
```

**Complexity Analysis**

The run time depends on the number of bits in $$n$$. Because $$n$$ in this piece of code is a 32-bit integer, the time complexity is $$O(1)$$.

The space complexity is $$O(1)$$, since no additional space is allocated.

---
#### Approach #2 (Bit Manipulation Trick) [Accepted]

**Algorithm**

We can make the previous algorithm simpler and a little faster. Instead of checking every bit of the number, we repeatedly flip the least-significant $$1$$-bit of the number to $$0$$, and add $$1$$ to the sum. As soon as the number becomes $$0$$, we know that it does not have any more $$1$$-bits, and we return the sum.

The key idea here is to realize that for any number $$n$$, doing a bit-wise AND of $$n$$ and $$n - 1$$ flips the least-significant $$1$$-bit in $$n$$ to $$0$$. Why? Consider the binary representations of $$n$$ and $$n - 1$$.

![Number of 1 Bits](https://leetcode.com/media/original_images/191_Number_Of_Bits.png){:width="400px"}
{:align="center"}

*Figure 1. AND-ing $$n$$ and $$n-1$$ flips the least-significant $$1$$-bit to 0.*
{:align="center"}

In the binary representation, the least significant $$1$$-bit in $$n$$ always corresponds to a $$0$$-bit in $$n - 1$$. Therefore, anding the two numbers $$n$$ and $$n - 1$$ always flips the least significant $$1$$-bit in $$n$$ to $$0$$, and keeps all other bits the same.

Using this trick, the code becomes very simple.

**Java**

```java
public int hammingWeight(int n) {
    int sum = 0;
    while (n != 0) {
        sum++;
        n &= (n - 1);
    }
    return sum;
}
```

**Complexity Analysis**

The run time depends on the number of $$1$$-bits in $$n$$. In the worst case, all bits in $$n$$ are $$1$$-bits. In case of a 32-bit integer, the run time is $$O(1)$$.

The space complexity is $$O(1)$$, since no additional space is allocated.

Analysis written by: @noran.
