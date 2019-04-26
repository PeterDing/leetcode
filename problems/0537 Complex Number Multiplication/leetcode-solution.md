# 0537 - Complex Number Multiplication

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math, String | [Leetcode](https://leetcode.com/problems/complex-number-multiplication) | [solution](https://leetcode.com/problems/complex-number-multiplication/solution/)


-----------

<p>
Given two strings representing two <a href = "https://en.wikipedia.org/wiki/Complex_number">complex numbers</a>.</p>

<p>
You need to return a string representing their multiplication. Note i<sup>2</sup> = -1 according to the definition.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "1+1i", "1+1i"
<b>Output:</b> "0+2i"
<b>Explanation:</b> (1 + i) * (1 + i) = 1 + i<sup>2</sup> + 2 * i = 2i, and you need convert it to the form of 0+2i.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "1+-1i", "1+-1i"
<b>Output:</b> "0+-2i"
<b>Explanation:</b> (1 - i) * (1 - i) = 1 + i<sup>2</sup> - 2 * i = -2i, and you need convert it to the form of 0+-2i.
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The input strings will not have extra blank.</li>
<li>The input strings will be given in the form of <b>a+bi</b>, where the integer <b>a</b> and <b>b</b> will both belong to the range of [-100, 100]. And <b>the output should be also in this form</b>.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1 Simple Solution[Accepted]

**Algorithm**

Multiplication of two complex numbers can be done as:

$$
(a+ib) \times (x+iy)=ax+i^2by+i(bx+ay)=ax-by+i(bx+ay)
$$

We simply split up the real and the imaginary parts of the given complex strings based on the '+' and the 'i' symbols. We store the real parts of the two strings $$a$$ and $$b$$ as $$x[0]$$ and $$y[0]$$ respectively and the imaginary parts as $$x[1]$$ and $$y[1]$$ respectively. Then, we multiply the real and the imaginary parts as required after converting the extracted parts into integers. Then, we again form the return string in the required format and return the result.

<iframe src="https://leetcode.com/playground/jgLSUzDc/shared" frameBorder="0" name="jgLSUzDc" width="100%" height="309"></iframe>

**Complexity Analysis**

* Time complexity : $$O(1)$$. Here splitting takes constant time as length of the string is very small $$(<20)$$.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
