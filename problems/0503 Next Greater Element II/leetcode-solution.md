# 0503 - Next Greater Element II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack | [Leetcode](https://leetcode.com/problems/next-greater-element-ii) | [solution](https://leetcode.com/problems/next-greater-element-ii/solution/)


-----------

<p>
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,2,1]
<b>Output:</b> [2,-1,2]
<b>Explanation:</b> The first 1's next greater number is 2; </br>The number 2 can't find next greater number; </br>The second 1's next greater number needs to search circularly, which is also 2.
</pre>
</p>

<p><b>Note:</b>
The length of given array won't exceed 10000.
</p>

-----------


## Similar Problems

- [Easy] [Next Greater Element I](next-greater-element-i)

- [Medium] [Next Greater Element III](next-greater-element-iii)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force (using Double Length Array) [Time Limit Exceeded]

 In this method, we make use of an array $$doublenums$$ which is formed by concatenating two copies of the given $$nums$$ array one after the other. Now, when we need to find out the next greater element for $$nums[i]$$, we can simply scan all the elements $$doublenums[j]$$, such that $$i < j < length(doublenums)$$. The first element found satisfying the given condition is the required result for $$nums[i]$$. If no such element is found, we put a $$\text{-1}$$ at the appropriate position in the $$res$$ array.

 
<iframe src="https://leetcode.com/playground/tRcR8Lx3/shared" frameBorder="0" name="tRcR8Lx3" width="100%" height="377"></iframe>

 **Complexity Analysis**

 * Time complexity : $$O(n^2)$$. The complete $$doublenums$$ array(of size $$\text{2n}$$) is scanned for all the elements of $$nums$$ in the worst case.

 * Space complexity : $$O(n)$$. $$doublenums$$ array of size $$\text{2n}$$ is used. $$res$$ array of size $$\text{n}$$ is used.


---

#### Approach #2 Better Brute Force [Accepted]

Instead of making a double length copy of $$nums$$ array , we can traverse circularly in the $$nums$$ array by making use of the $$\text{%(modulus)}$$ operator. For every element $$nums[i]$$, we start searching in the $$nums$$ array(of length $$n$$) from the index $$(i+1)%n$$ and look at the next(cicularly) $$n-1$$ elements. For $$nums[i]$$ we do so by scanning over $$nums[j]$$, such that
$$(i+1)%n &leq; j &leq; (i+(n-1))%n$$, and we look for the first greater element found. If no such element is found, we put a $$\text{-1}$$ at the appropriate position in the $$res$$ array.

 
<iframe src="https://leetcode.com/playground/LCG759JD/shared" frameBorder="0" name="LCG759JD" width="100%" height="309"></iframe>

 **Complexity Analysis**

 * Time complexity : $$O(n^2)$$. The complete $$nums$$ array of size $$n$$ is scanned for all the elements of $$nums$$ in the worst case.

 * Space complexity : $$O(n)$$. $$res$$ array of size $$n$$ is used.

---

#### Approach #3 Using Stack [Accepted]

This approach makes use of a stack. This stack stores the indices of the appropriate elements from $$nums$$ array.  The top of the stack refers to the index of the Next Greater Element found so far. We store the indices instead of the elements since there could be duplicates in the $$nums$$ array. The description of the method will make the above statement clearer.

We start traversing the $$nums$$ array from right towards the left. For an element $$nums[i]$$ encountered, we pop all the elements
$$stack[top]$$ from the stack such that $$nums\big[stack[top]\big] &le; nums[i]$$. We continue the popping till we encounter a $$stack[top]$$ satisfying $$nums\big[stack[top]\big] > nums[i]$$. Now, it is obvious that the current $$stack[top]$$ only can act as the
Next Greater Element for $$nums[i]$$(right now, considering only the elements lying to the right of $$nums[i]$$).

If no element remains on the top of the stack, it means no larger element than $$nums[i]$$ exists to its right. Along with this, we also push the index of the element just encountered($$nums[i]$$), i.e. $$i$$ over the top of the stack, so that $$nums[i]$$(or $$stack[top$$) now acts as the Next Greater Element for the elements lying to its left.

We go through two such passes over the complete $$nums$$ array. This is done so as to complete a circular traversal over the $$nums$$ array. The first pass could make some wrong entries in the $$res$$ array since it considers only the elements lying to the right of $$nums[i]$$, without a circular traversal. But, these entries are corrected in the second pass.  

Further, to ensure the correctness of the method, let's look at the following cases.

Assume that $$nums[j]$$ is the correct Next Greater Element for $$nums[i]$$, such that $$i < j &le; stack[top]$$. Now, whenever we encounter $$nums[j]$$, if $$nums[j] > nums\big[stack[top]\big]$$, it would have already popped the previous $$stack[top]$$ and $$j$$ would have become the topmost element. On the other hand, if  $$nums[j] < nums\big[stack[top]\big]$$, it would have become the topmost element by being pushed above the previous $$stack[top]$$. In both the cases, if $$nums[j] > nums[i]$$, it will be correctly determined to be the Next Greater Element.

The following example makes the procedure clear:

<!--![Next_Greater_Element_II](../Figures/503_Next_Greater_Element_II.gif)-->
!?!../Documents/503_Next_Greater2.json:1000,563!?!

As the animation above depicts, after the first pass, there are a number of wrong entries(marked as $$\text{-1}$$) in the $$res$$ array, because only the elements lying to the corresponding right(non-circular) have been considered till now. But, after the second pass, the correct values are substituted.



 
<iframe src="https://leetcode.com/playground/in37fqRd/shared" frameBorder="0" name="in37fqRd" width="100%" height="309"></iframe>

 **Complexity Analysis**

 * Time complexity : $$O(n)$$. Only two traversals of the $$nums$$ array are done. Further, atmost $$\text{2n}$$ elements are pushed and popped from the stack.

 * Space complexity : $$O(n)$$. A stack of size $$n$$ is used. $$res$$ array of size $$n$$ is used.

---


Analysis written by: [@vinod23](https://leetcode.com/vinod23)
