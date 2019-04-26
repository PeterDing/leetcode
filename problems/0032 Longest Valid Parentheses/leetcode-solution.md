# 0032 - Longest Valid Parentheses

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | String, Dynamic Programming | [Leetcode](https://leetcode.com/problems/longest-valid-parentheses) | [solution](https://leetcode.com/problems/longest-valid-parentheses/solution/)


-----------

<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, find the length of the longest valid (well-formed) parentheses substring.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()&quot;</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;<code>)()())</code>&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()()&quot;</code>
</pre>


-----------


## Similar Problems

- [Easy] [Valid Parentheses](valid-parentheses)




## Solution:

[TOC]
## Summary

We need to determine the length of the largest valid substring of parentheses from a given string.

## Solution
---
#### Approach 1: Brute Force

**Algorithm**

In this approach, we consider every possible non-empty even length substring from the given string and check whether it's
a valid string of parentheses or not. In order to check the validity, we use the Stack's Method.

Every time we
encounter a $$\text{‘(’}$$, we push it onto the stack. For every $$\text{‘)’}$$ encountered, we pop a $$\text{‘(’}$$ from the stack. If $$\text{‘(’}$$ isn't
 available on the stack for popping at anytime or if stack contains some elements after processing complete substring, the substring of parentheses is invalid. In this way, we repeat the
 process for every possible substring and we keep on
  storing the length of the longest valid string found so far.
```
Example:
"((())"

(( --> invalid
(( --> invalid
() --> valid, length=2
)) --> invalid
((()--> invalid
(())--> valid, length=4
maxlength=4
```

<iframe src="https://leetcode.com/playground/smDecW2X/shared" frameBorder="0" width="100%" height="497" name="smDecW2X"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^3)$$. Generating every possible substring from a string of length $$n$$ requires $$O(n^2)$$. Checking validity of a string of length $$n$$ requires $$O(n)$$.

* Space complexity : $$O(n)$$. A stack of depth $$n$$ will be required for the longest substring.
<br />
<br />
---

#### Approach 2: Using Dynamic Programming

**Algorithm**

This problem can be solved by using Dynamic Programming. We make use of a $$\text{dp}$$ array where $$i$$th element of $$\text{dp}$$ represents the length of the longest valid substring ending at $$i$$th index. We initialize the complete $$\text{dp}$$ array with 0's. Now, it's obvious that the valid substrings must end with $$\text{‘)’}$$. This further leads to the conclusion that the substrings ending with $$\text{‘(’}$$ will always contain '0' at their corresponding $$\text{dp}$$ indices. Thus, we update the $$\text{dp}$$ array only when $$\text{‘)’}$$ is encountered.

To fill $$\text{dp}$$ array we will check every two consecutive characters of the string and if

1. $$\text{s}[i] = \text{‘)’}$$ and $$\text{s}[i - 1] = \text{‘(’}$$, i.e. string looks like $$``.......()" \Rightarrow$$

    $$
    \text{dp}[i]=\text{dp}[i-2]+2
    $$

    We do so because the ending "()" portion is a valid substring anyhow and leads to an increment of 2 in the length of the just previous valid substring's length.

2. $$\text{s}[i] = \text{‘)’}$$ and $$\text{s}[i - 1] = \text{‘)’}$$, i.e. string looks like $$``.......))" \Rightarrow$$

    if $$\text{s}[i - \text{dp}[i - 1] - 1] = \text{‘(’}$$ then

    $$
    \text{dp}[i]=\text{dp}[i-1]+\text{dp}[i-\text{dp}[i-1]-2]+2
    $$

   The reason behind this is that if the 2nd last $$\text{‘)’}$$ was a part of a valid substring (say $$sub_s$$), for the last $$\text{‘)’}$$ to be a part of a larger substring, there must be a corresponding starting $$\text{‘(’}$$ which lies before the valid substring of which the 2nd last $$\text{‘)’}$$ is a part (i.e. before $$sub_s$$). Thus, if the character before $$sub_s$$ happens to be $$\text{‘(’}$$, we update the $$\text{dp}[i]$$ as an addition of $$2$$ in the length of $$sub_s$$ which is $$\text{dp}[i-1]$$. To this, we also add the length of the valid substring just before the term "(,sub_s,)" , i.e. $$\text{dp}[i-\text{dp}[i-1]-2]$$.

For better understanding of this method, see this example:

<!--![Longest_Valid_Parenthesis](../Figures/32_LongestValidParenthesisDP.gif)-->
!?!../Documents/32_Longest_Valid2.json:1000,563!?!

<iframe src="https://leetcode.com/playground/YGuAh4tp/shared" frameBorder="0" width="100%" height="344" name="YGuAh4tp"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Single traversal of string to fill dp array is done.

* Space complexity : $$O(n)$$. dp array of size $$n$$ is used.
<br />
<br />
---
#### Approach 3: Using Stack

**Algorithm**

Instead of finding every possible string and checking its validity, we can make use of stack while scanning
the given string to check if the string scanned so far is valid, and also the length of the longest valid string. In order to do so, we start by pushing $$-1$$ onto the stack.

 For every $$\text{‘(’}$$ encountered, we push its index onto the stack.

 For every $$\text{‘)’}$$ encountered, we pop the topmost element and subtract the current element's index from the top element of the stack, which gives the length of the currently encountered valid string of parentheses. If while popping the element, the stack becomes empty, we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings, and return the length of the longest valid string at the end.

See this example for better understanding.

<!--![Longest_Valid_Parenthesis](../Figures/32_LongestValidParenthesisSTACK.gif)-->
!?!../Documents/32_Longest_Valid_stack_new.json:1000,563!?!

<iframe src="https://leetcode.com/playground/A2oPe4yE/shared" frameBorder="0" width="100%" height="412" name="A2oPe4yE"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. $$n$$ is the length of the given string..

* Space complexity : $$O(n)$$. The size of stack can go up to $$n$$.
<br />
<br />
---
#### Approach 4: Without extra space

**Algorithm**

In this approach, we make use of two counters $$left$$ and $$right$$. First, we start traversing the string from the left towards the right and for every $$\text{‘(’}$$ encountered, we increment the $$left$$ counter and for every $$\text{‘)’}$$ encountered, we increment the $$right$$ counter. Whenever $$left$$ becomes equal to $$right$$, we calculate the length of the current valid string and keep track of maximum length substring found so far. If $$right$$ becomes greater than $$left$$ we reset $$left$$ and $$right$$ to $$0$$.

Next, we start traversing the string from right to left and similar procedure is applied.

Example of this approach:

<!--![Longest_Valid_Parenthesis](../Figures/32_LongestValidParenthesisLR.gif)-->
!?!../Documents/32_Longest_Validlr.json:1000,563!?!

<iframe src="https://leetcode.com/playground/RsBpRHK7/shared" frameBorder="0" width="100%" height="500" name="RsBpRHK7"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Two traversals of the string.

* Space complexity : $$O(1)$$. Only two extra variables $$left$$ and $$right$$ are needed.
