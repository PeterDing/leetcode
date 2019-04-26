# 0717 - 1-bit and 2-bit Characters

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/1-bit-and-2-bit-characters) | [solution](https://leetcode.com/problems/1-bit-and-2-bit-characters/solution/)


-----------

<p>We have two special characters. The first character can be represented by one bit <code>0</code>. The second character can be represented by two bits (<code>10</code> or <code>11</code>).  </p>

<p>Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
bits = [1, 0, 0]
<b>Output:</b> True
<b>Explanation:</b> 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
bits = [1, 1, 1, 0]
<b>Output:</b> False
<b>Explanation:</b> 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
</pre>
</p>

<p><b>Note:</b>
<li><code>1 <= len(bits) <= 1000</code>.</li>
<li><code>bits[i]</code> is always <code>0</code> or <code>1</code>.</li>
</p>

-----------


## Similar Problems

- [Medium] [Gray Code](gray-code)




## Solution:

[TOC]


#### Approach #1: Increment Pointer [Accepted]

**Intuition and Algorithm**

When reading from the `i`-th position, if `bits[i] == 0`, the next character must have 1 bit; else if `bits[i] == 1`, the next character must have 2 bits.  We increment our read-pointer `i` to the start of the next character appropriately.  At the end, if our pointer is at `bits.length - 1`, then the last character must have a size of 1 bit.

**Python**
```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
```

**Java**
```java
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.length - 1) {
            i += bits[i] + 1;
        }
        return i == bits.length - 1;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `bits`.

* Space Complexity: $$O(1)$$, the space used by `i`.

---
#### Approach #2: Greedy [Accepted]

**Intuition and Algorithm**

The second-last `0` must be the end of a character (or, the beginning of the array if it doesn't exist).  Looking from that position forward, the array `bits` takes the form `[1, 1, ..., 1, 0]` where there are zero or more `1`'s present in total.  It is easy to show that the answer is `true` if and only if there are an even number of ones present.

In our algorithm, we will find the second last zero by performing a linear scan from the right.  We present two slightly different approaches below.

**Python**
```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
```

**Java**
```java
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = bits.length - 2;
        while (i >= 0 && bits[i] > 0) i--;
        return (bits.length - i) % 2 == 0;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `bits`.

* Space Complexity: $$O(1)$$, the space used by `parity` (or `i`).

---

Analysis written by: [@awice](https://leetcode.com/awice).
