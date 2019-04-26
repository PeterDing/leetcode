# 0466 - Count The Repetitions

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/count-the-repetitions) | [solution](https://leetcode.com/problems/count-the-repetitions/solution/)


-----------

<p>Define <code>S = [s,n]</code> as the string S which consists of n connected strings s. For example, <code>["abc", 3]</code> ="abcabcabc". </p>
<p>On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc”  can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.</p>
<p>You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 &le; n1 &le; 10<sup>6</sup> and 1 &le; n2 &le; 10<sup>6</sup>. Now consider the strings S1 and S2, where <code>S1=[s1,n1]</code> and <code>S2=[s2,n2]</code>. Find the maximum integer M such that <code>[S2,M]</code> can be obtained from <code>S1</code>.</p>

<p><b>Example:</b>
<pre>
Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
</pre>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach #1 Brute force [Time Limit Exceeded]

**Intuition**

According to the question, we need to find $$m$$ such that $$[S2,m]$$ is the largest subsequence that can be found in $$S1$$. $$S2$$ is essentially $$[s2,n2]$$ and $$S1$$ is $$[s1,n1]$$ and so, we can find the number of times $$s2$$ repeats in $$[s1,n1]$$, say $$\text{repeat_count}$$. And the number of times $$S2$$ repeats in $$S1$$ is therefore $$\text{(repeat_count/n2)}$$. Simple.

**Algorithm**

* Initialize $$\text{index=0}$$ and $$\text{repeat_count=0}$$. $$\text{index}$$ represents the current index in $$s2$$ to be checked against $$s1$$ and $$\text{repeat_count}$$ represents the number of times $$s2$$ repeats in $$S1$$.
* Iterate over the variable $$i$$ from $$0$$ to $$n1-1$$:
    * Iterate over the variable $$j$$ from $$0$$ to $$\text{size(s1)}-1$$:  
        * If $$\text{s1[j] }$$ is equal to $$\text{s2[index]}$$, increment $$\text{index}$$.
        * If $$index$$ is equal to $$size(s2)$$, this implies that $$s2$$ has completed one repartition and hence set $$\text{index=0}$$ and increment the $$\text{repeat_count}$$.
* Return $$\text{(repeat_count / n2)}$$ since, $$S2$$ is $$\text{[s2,n2]}$$.


<iframe src="https://leetcode.com/playground/y5jtZgJj/shared" frameBorder="0" name="y5jtZgJj" width="100%" height="326"></iframe>

**Complexity Analysis**

* Time complexity: $$O(n1*size(s1))$$.
    * We iterate over the entire length of string $$s1$$ for $$n1$$ times.

* Space complexity: $$O(1)$$ extra space for $$\text{index}$$ and $$\text{repeat_count}$$.

---
#### Approach #2 A better brute force [Accepted]

**Intuition**

In Approach #1, we simply checked for repetition over the entire $$[s1,n1]$$. However, $$n1$$ could be quiet large and thus, is inefficient to iterate over complete $$S1$$. We can take advantage of the fact that $$s1$$ is repeating and hence, we could find a pattern of repetition of $$s2$$ in $$S1$$. Once, we get the repetition pattern, we can easy calculate how many times the pattern repeats in $$n2$$ in $$O(1)$$.

*But what's the pattern!*

In approach #1, we kept $$\text{index}$$ which tells the index to search in $$s2$$. We try to see in the below illustration if this $$\text{index}$$ repeats itself after some fixed iterations of $$s1$$ or not and if so, then how can we leverage it.

![Count the repitition](../Figures/466/count_the_repititions.png){:width="700px"}
{:align="center"}

After finding the repitition pattern, we can calculate the sum of repeating pattern, part before repitition and part left after repitition as the result in $$O(1)$$.   

*But will this repitition always take place?*

Yes! By **Pigeonhole principle**, which states that if $$n$$ items are put into $$m$$ containers, with $$n > m$$, then at least one container must contain more than one item. So, according to this, we are sure to find 2 same $$index$$ after scanning at max $$\text{size(s2)}$$ blocks of $$s1$$.


**Algorithm**

* Intialize $$count=0$$ nd $$index=0$$, which are same as in Approach #1.
* Initialize 2 arrays, say $$\text{indexr}$$ and $$\text{countr}$$ of size $$(\text{size(s2)}+1)$$, initialized with 0. The size $$(\text{size(s2)}+1)$$ is based on the Pigeonhole principle as discussed above. The 2 arrays specifies the $$\text{index}$$ and $$\text{count}$$ at the start of each $$s1$$ block.
* Iterate over $$i$$ from $$0$$ to $$n1-1$$:
    * Iterate over $$j$$ from $$0$$ to $$\text{size(s1)}-1$$:
        * If $$\text{s1[j]} == \text{s2[index]}$$, increment $$\text{index}$$.
        * If $$\text{index}$$ is equal to $$\text{size(s2)}$$, set $$\text{index} = 0$$ and increment $$\text{count}$$.
    * Set $$\text{countr[i]}=\text{count}$$ and $$\text{indexr[i]}=\text{index}$$
    * Iterate over $$k$$ from $$0$$ to $$i-1$$:
        * If we find the repitition, i.e. current $$\text{index} = \text{indexr[k]}$$, we calculate the count for block before the repitition starts, the repeating block and the block left after repitition pattern, which can be calculated as:

        $$
        \begin{align}
        \text{prev_count} &= \text{countr}[k] \\
        \text{pattern_count} &= (\text{countr}[i] - \text{countr}[k]) * \frac{n1 - 1 - k}{i - k} \\
        \text{remain_count} &= \text{countr}\left[k + \left(n1 - 1 - k\right) \% \left(i - k \right)\right] - \text{countr}[k]
        \end{align}
        $$

        * Sum the 3 counts and return the sum divided by $$n2$$, since $$\text{S2 = [s2,n2]}$$
* If no repetition is found, return $$\text{countr[n1-1]/n2}$$.


<iframe src="https://leetcode.com/playground/2UJEXG8V/shared" frameBorder="0" name="2UJEXG8V" width="100%" height="515"></iframe>

**Complexity analysis**

* Time complexity: $$\text{O(size(s1)*size(s2))}$$.
    * According to the Pigeonhole principle, we need to iterate over $$s1$$ only $$(\text{size(s2)+1})$$ times at max.

* Space complexity: $$O(\text{size(s2)})$$ extra space for $$\text{indexr}$$ and $$\text{countr}$$ string.

---
Analysis written by [@abhinavbansal0](https://leetcode.com/abhinavbansal0).
