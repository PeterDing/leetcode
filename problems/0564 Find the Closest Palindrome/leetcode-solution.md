# 0564 - Find the Closest Palindrome

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | String | [Leetcode](https://leetcode.com/problems/find-the-closest-palindrome) | [solution](https://leetcode.com/problems/find-the-closest-palindrome/solution/)


-----------

<p>Given an integer n, find the closest integer (not including itself), which is a palindrome. </p>

<p>The 'closest' is defined as absolute difference minimized between two integers.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "123"
<b>Output:</b> "121"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input <b>n</b> is a positive integer represented by string, whose length will not exceed 18.</li>
<li>If there is a tie, return the smaller one as answer.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force[Time Limit Exceeded]

The simplest solution is to consider every possible number smaller than the given number $$n$$, starting by decrementing 1 from the given number and go on in descending order. Similarly, we can consider every possible number greater than $$n$$ starting by incrementing 1 from the given number and going in ascending order. We can continue doing so in an alternate manner till we find a number which is a palindrome.

<iframe src="https://leetcode.com/playground/DvreVK8V/shared" frameBorder="0" name="DvreVK8V" width="100%" height="377"></iframe>

**Complexity Analysis**

* Time complexity : $$O(\sqrt{n})$$. Upto $$2*\sqrt{n}$$ numbers could be generated in the worst case.

* Space complexity : $$O(1)$$. Constant space is used.

---

#### Approach #2 Using Math[Accepted]

**Algorithm**

To understand this method, let's start with a simple illustration. Assume that the number given to us is "abcxy". One way to convert this number into a palindrome is to replicate one half of the string to the other half. If we try replicating the second half to the first half, the new palindrome obtained will be "yxcxy" which lies at an absolute of $$\left|10000(a-y) + 1000(b-x)\right|$$ from the original number. But, if we replicate the first half to the second half of the string, we obtain "abcba", which lies at an absolute difference of $$\left|10(x-b) + (y-a)\right|$$. Trying to change $$c$$ additionaly in either case would incur an additional value of atleast 100 in the absolute difference.

From the above illustration, we can conclude that if replication is used to generate the palindromic number, we should always replicate the first half to the second half. In this implementation, we've stored such a number in $$a$$ at a difference of $$diff1$$ from $$n$$.

But, there exists another case as well, where the digit at the middle index is incremented or decremented. In such cases, it could be profitable to make changes to the central digit only since such changes could lead to a palindrome formation nearer to the original digit. e.g. 10987. Using the above criteria, the palindrome obtained will be 10901 which is at a more difference from 10987 than 11011. A similar situation occurs if a 0 occurs at the middle digit. But, again as discussed previously, we need to consider only the first half digits to obtain the new palindrome. This special effect occurs with 0 or 9 at the middle digit since, only decrementing 0 and incrementing 9 at that digit place can lead to the change in the rest of the digits towards their left. In any other case, the situation boils down to the one discussed in the first paragraph.

Now, whenever we find a 0 near the middle index, in order to consider the palindromes which are lesser than $$n$$, we subtract a 1 from the first half of the number to obtain a new palindromic half e.g. If the given number $$n$$ is 20001, we subtract a 1 from 200 creating a number of the form 199xx. To obtain the new palindrome, we replicate the first half to obtain 19991. Taking another example of  10000, (with a 1 at the MSB), we subtract a 1 from 100 creating 099xx as the new number transforming to a 9999 as the new palindrome. This number is stored in $$b$$ having a difference of $$diff2$$ from $$n$$

Similar treatment needs to be done with a 9 at the middle digit, except that this time we need to consider the numbers larger than the current number. For this, we add a 1 to the first half. e.g. Taking the number 10987, we add a 1 to 109 creating a number of the form 110xx(11011 is the new palindrome). This palindrome is stored in $$c$$ having a difference of $$diff3$$ from $$n$$.

Out of these three palindromes, we can choose the one with a minimum difference from $$n$$. Further, in case of a tie, we need to return the smallest palindrome obtained. For resolving this tie's conflict, we can observe that a tie is possible only if one number is larger than $$n$$ and another is lesser than $$n$$. Further, we know that the number $$b$$ is obtained by decreasing $$n$$. Thus, in case of conflict between $$b$$ and any other number, we need to choose $$b$$. Similarly, $$c$$ is obtained by increasing $$n$$. Thus, in case of a tie between $$c$$ and any other number, we need to choose the number other than $$c$$.



<iframe src="https://leetcode.com/playground/Y6G9NDDf/shared" frameBorder="0" name="Y6G9NDDf" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(l)$$. Scanning, insertion, deletion,, mirroring takes $$O(l)$$, where $$l$$ is the length of the string.

* Space complexity : $$O(l)$$. Temporary variables are used to store the strings.

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
