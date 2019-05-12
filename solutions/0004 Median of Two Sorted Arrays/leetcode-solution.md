# 0004 - Median of Two Sorted Arrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Binary Search, Divide and Conquer | [Leetcode](https://leetcode.com/problems/median-of-two-sorted-arrays) | [solution](https://leetcode.com/problems/median-of-two-sorted-arrays/solution/)

-----------

<p>There are two sorted arrays <b>nums1</b> and <b>nums2</b> of size m and n respectively.</p>

<p>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</p>

<p>You may assume <strong>nums1</strong> and <strong>nums2</strong>&nbsp;cannot be both empty.</p>

<p><b>Example 1:</b></p>

<pre>
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
</pre>

<p><b>Example 2:</b></p>

<pre>
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
</pre>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach 1: Recursive Approach

To solve this problem, we need to understand "What is the use of median". In statistics, the median is used for:

>Dividing a set into two equal length subsets, that one subset is always greater than the other.

If we understand the use of median for dividing, we are very close to the answer.

First let's cut $$\text{A}$$ into two parts at a random position $$i$$:

```
          left_A             |        right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
```

Since $$\text{A}$$ has $$m$$ elements, so there are $$m+1$$ kinds of cutting ($$i = 0 \sim m$$).

And we know:

>$$\text{len}(\text{left\_A}) = i, \text{len}(\text{right\_A}) = m - i$$.
>
>Note: when $$i = 0$$, $$\text{left\_A}$$ is empty, and when $$i = m$$, $$\text{right\_A}$$ is empty.

With the same way, cut $$\text{B}$$ into two parts at a random position $$j$$:

```

          left_B             |        right_B
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```

Put $$\text{left\_A}$$ and $$\text{left\_B}$$ into one set, and put $$\text{right\_A}$$ and $$\text{right\_B}$$ into another set. Let's name them $$\text{left\_part}$$ and $$\text{right\_part}$$:

```
          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```

If we can ensure:

>1. $$\text{len}(\text{left\_part}) = \text{len}(\text{right\_part})$$
>2. $$\max(\text{left\_part}) \leq \min(\text{right\_part})$$

then we divide all elements in $$\{\text{A}, \text{B}\}$$ into two parts with equal length, and one part is always greater than the other. Then

$$
\text{median} = \frac{\text{max}(\text{left}\_\text{part}) + \text{min}(\text{right}\_\text{part})}{2}
$$

To ensure these two conditions, we just need to ensure:

>1. $$i + j = m - i + n - j$$ (or: $$m - i + n - j + 1$$)  
>   if $$n \geq m$$, we just need to set:  $$ \ i = 0 \sim m,\  j = \frac{m + n + 1}{2} - i \\$$  
>  
>  
>2.  $$\text{B}[j-1] \leq \text{A}[i]$$ and $$\text{A}[i-1] \leq \text{B}[j]$$

ps.1 For simplicity, I presume $$\text{A}[i-1], \text{B}[j-1], \text{A}[i], \text{B}[j]$$ are always valid even if $$i=0$$, $$i=m$$, $$j=0$$, or $$j=n$$.
I will talk about how to deal with these edge values at last.

ps.2 Why $$n \geq m$$? Because I have to make sure $$j$$ is non-negative since $$0 \leq i \leq m$$ and $$j = \frac{m + n + 1}{2} - i$$. If $$n < m$$, then $$j$$ may be negative, that will lead to wrong result.

So, all we need to do is:

>Searching $$i$$ in $$[0, m]$$, to find an object $$i$$ such that:
>  
>$$\qquad \text{B}[j-1] \leq \text{A}[i]\ $$ and $$\ \text{A}[i-1] \leq \text{B}[j],\ $$ where $$j = \frac{m + n + 1}{2} - i$$

And we can do a binary search following steps described below:

1. Set $$\text{imin} = 0$$, $$\text{imax} = m$$, then start searching in $$[\text{imin}, \text{imax}]$$
2. Set $$i = \frac{\text{imin} + \text{imax}}{2}$$, $$j = \frac{m + n + 1}{2} - i$$
3. Now we have $$\text{len}(\text{left}\_\text{part})=\text{len}(\text{right}\_\text{part})$$. And there are only 3 situations that we may encounter:  

    - $$\text{B}[j-1] \leq \text{A}[i]$$ and $$\text{A}[i-1] \leq \text{B}[j]$$  
      Means we have found the object $$i$$, so stop searching.  

    - $$\text{B}[j-1] > \text{A}[i]$$  
      Means $$\text{A}[i]$$ is too small. We must adjust $$i$$ to get $$\text{B}[j-1] \leq \text{A}[i]$$.  
      Can we increase $$i$$?  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes. Because when $$i$$ is increased, $$j$$ will be decreased.  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So $$\text{B}[j-1]$$ is decreased and $$\text{A}[i]$$ is increased, and $$\text{B}[j-1] \leq \text{A}[i]$$ may  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;be satisfied.  
      Can we decrease $$i$$?  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No! Because when $$i$$ is decreased, $$j$$ will be increased.  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So $$\text{B}[j-1]$$ is increased and $$\text{A}[i]$$ is decreased, and $$\text{B}[j-1] \leq \text{A}[i]$$ will  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;be never satisfied.  
      So we must increase $$i$$. That is, we must adjust the searching range to $$[i+1, \text{imax}]$$.  
      So, set $$\text{imin} = i+1$$, and goto 2.

    - $$\text{A}[i-1] > \text{B}[j]$$:  
      Means $$\text{A}[i-1]$$ is too big. And we must decrease $$i$$ to get   $$\text{A}[i-1]\leq \text{B}[j]$$.  
      That is, we must adjust the searching range to $$[\text{imin}, i-1]$$.  
      So, set $$\text{imax} = i-1$$, and goto 2.


When the object $$i$$ is found, the median is:

>$$\max(\text{A}[i-1], \text{B}[j-1]), \ $$ when $$m + n$$ is odd

>$$\frac{\max(\text{A}[i-1], \text{B}[j-1]) + \min(\text{A}[i], \text{B}[j])}{2}, \ ​$$ when $$m + n​$$ is even

Now let's consider the edges values $$i=0,i=m,j=0,j=n​$$ where $$\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]​$$ may not exist.
Actually this situation is easier than you think.

What we need to do is ensuring that $$\text{max}(\text{left}\_\text{part}) \leq \text{min}(\text{right}\_\text{part})$$. So, if $$i$$ and $$j$$ are not edges values (means $$\text{A}[i-1],
\text{B}[j-1],\text{A}[i],\text{B}[j]$$ all exist), then we must check both $$\text{B}[j-1] \leq \text{A}[i]$$ and $$\text{A}[i-1] \leq \text{B}[j]$$.
But if some of $$\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]$$ don't exist, then we don't need to check one (or both) of these two conditions.
For example, if $$i=0$$, then $$\text{A}[i-1]$$ doesn't exist, then we don't need to check $$\text{A}[i-1] \leq \text{B}[j]$$.
So, what we need to do is:

>Searching $$i$$ in $$[0, m]$$, to find an object $$i$$ such that:
>
>$$(j = 0$$ or $$i = m$$ or $$\text{B}[j-1] \leq \text{A}[i])$$ and  
>$$(i = 0$$ or $$j = n$$ or $$\text{A}[i-1] \leq \text{B}[j]),$$  where $$j = \frac{m + n + 1}{2} - i$$

And in a searching loop, we will encounter only three situations:

>1. $$(j = 0$$ or $$i = m$$ or $$\text{B}[j-1] \leq \text{A}[i])$$ and  
    $$(i = 0$$ or $$j = n$$ or $$\text{A}[i-1] \leq \text{B}[j])$$  
    Means $$i$$ is perfect, we can stop searching.
>2. $$j > 0$$ and $$i < m$$ and $$\text{B}[j - 1] > \text{A}[i]$$  
    Means $$i$$ is too small, we must increase it.
>3. $$i > 0$$ and $$j < n$$ and $$\text{A}[i - 1] > \text{B}[j]$$  
    Means $$i$$ is too big, we must decrease it.

Thanks to [@Quentin.chen](https://leetcode.com/Quentin.chen) for pointing out that: $$i < m \implies j > 0$$ and $$i > 0 \implies j < n$$. Because:


>$$m \leq n,\  i < m \implies j = \frac{m+n+1}{2} - i > \frac{m+n+1}{2} - m \geq \frac{2m+1}{2} - m \geq 0$$
>
>$$m \leq n,\  i > 0 \implies j = \frac{m+n+1}{2} - i < \frac{m+n+1}{2} \leq \frac{2n+1}{2} \leq n$$


So in situation 2. and 3. , we don't need to check whether $$j > 0$$ and whether $$j < n$$.

<iframe src="https://leetcode.com/playground/X5mgSxnd/shared" frameBorder="0" width="100%" height="500" name="X5mgSxnd"></iframe>

**Complexity Analysis**

* Time complexity: $$O\big(\log\big(\text{min}(m,n)\big)\big)​$$.  
At first, the searching range is $$[0, m]​$$.
And the length of this searching range will be reduced by half after each loop.
So, we only need $$\log(m)​$$ loops. Since we do constant operations in each loop, so the time complexity is $$O\big(\log(m)\big)​$$.
Since $$m \leq n​$$, so the time complexity is $$O\big(\log\big(\text{min}(m,n)\big)\big)​$$.

* Space complexity: $$O(1)$$.  
We only need constant memory to store $$9$$ local variables, so the space complexity is $$O(1)$$.
