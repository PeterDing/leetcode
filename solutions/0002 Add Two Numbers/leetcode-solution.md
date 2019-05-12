# 0002 - Add Two Numbers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List, Math | [Leetcode](https://leetcode.com/problems/add-two-numbers) | [solution](https://leetcode.com/problems/add-two-numbers/solution/)


-----------

<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b> and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> (2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<b>Output:</b> 7 -&gt; 0 -&gt; 8
<b>Explanation:</b> 342 + 465 = 807.
</pre>


-----------


## Similar Problems

- [Medium] [Multiply Strings](multiply-strings)

- [Easy] [Add Binary](add-binary)

- [Easy] [Sum of Two Integers](sum-of-two-integers)

- [Easy] [Add Strings](add-strings)

- [Medium] [Add Two Numbers II](add-two-numbers-ii)

- [Easy] [Add to Array-Form of Integer](add-to-array-form-of-integer)




## Solution:

## Solution
---
#### Approach 1: Elementary Math

**Intuition**

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.

![Illustration of Adding two numbers](../Figures/2_add_two_numbers.svg){:width="539px"}
{:align="center"}

*Figure 1. Visualization of the addition of two numbers: $$342 + 465 = 807$$.  
Each node contains a single digit and the digits are stored in reverse order.*
{:align="center"}

**Algorithm**

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of $$l1$$ and $$l2$$. Since each digit is in the range of $$0 \ldots 9$$, summing two digits may "overflow". For example $$5 + 7 = 12$$. In this case, we set the current digit to $$2$$ and bring over the $$carry = 1$$ to the next iteration. $$carry$$ must be either $$0$$ or $$1$$ because the largest possible sum of two digits (including the carry) is $$9 + 9 + 1 = 19$$.

The pseudocode is as following:

* Initialize current node to dummy head of the returning list.
* Initialize carry to $$0$$.
* Initialize $$p$$ and $$q$$ to head of $$l1$$ and $$l2$$ respectively.
* Loop through lists $$l1$$ and $$l2$$ until you reach both ends.
    * Set $$x$$ to node $$p$$'s value. If $$p$$ has reached the end of $$l1$$, set to $$0$$.
    * Set $$y$$ to node $$q$$'s value. If $$q$$ has reached the end of $$l2$$, set to $$0$$.
    * Set $$sum = x + y + carry$$.
    * Update $$carry = sum / 10$$.
    * Create a new node with the digit value of $$(sum \bmod 10)$$ and set it to current node's next, then advance current node to next.
    * Advance both $$p$$ and $$q$$.
* Check if $$carry = 1$$, if so append a new node with digit $$1$$ to the returning list.
* Return dummy head's next node.

Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

Take extra caution of the following cases:

| Test case | Explanation |
| ------------- | ---------------- |
| $$l1=[0,1]$$<br>$$l2=[0,1,2]$$ | When one list is longer than the other. |
| $$l1=[]$$<br>$$l2=[0,1]$$ | When one list is null, which means an empty list. |
| $$l1=[9,9]$$<br>$$l2=[1]$$ | The sum could have an extra carry of one at the end, which is easy to forget. |

<iframe src="https://leetcode.com/playground/5onAHA8v/shared" frameBorder="0" width="100%" height="378" name="5onAHA8v"></iframe>

**Complexity Analysis**

* Time complexity : $$O(\max(m, n))$$. Assume that $$m$$ and $$n$$ represents the length of $$l1$$ and $$l2$$ respectively, the algorithm above iterates at most $$\max(m, n)$$ times.

* Space complexity : $$O(\max(m, n))$$. The length of the new list is at most $$\max(m,n) + 1$$.

**Follow up**

What if the the digits in the linked list are stored in non-reversed order? For example:

$$
(3 \to 4 \to 2) + (4 \to 6 \to 5) = 8 \to 0 \to 7
$$
