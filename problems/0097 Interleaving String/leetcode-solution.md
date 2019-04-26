# 0097 - Interleaving String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | String, Dynamic Programming | [Leetcode](https://leetcode.com/problems/interleaving-string) | [solution](https://leetcode.com/problems/interleaving-string/solution/)


-----------

<p>Given <em>s1</em>, <em>s2</em>, <em>s3</em>, find whether <em>s3</em> is formed by the interleaving of <em>s1</em> and <em>s2</em>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, <em>s3</em> = &quot;aadbbcbcac&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, <em>s3</em> = &quot;aadbbbaccc&quot;
<strong>Output:</strong> false
</pre>


-----------


## Similar Problems




## Solution:

[TOC]
## Summary

We need to determine whether a given string can be formed by interleaving the other two strings.

## Solution

---
#### Approach 1: Brute Force

The most basic idea is to find every string possible by all interleavings of the two given strings $$s1$$ and $$s2$$.
In order to implement this method, we are using recursion. We start by taking the current character of the
first string $$s1$$ and then appending all possible interleavings of the remaining portion of the first string $$s1$$ and the second string $$s2$$ and comparing each result formed with the required interleaved string $$s3$$.
Similarly, we choose one character from the second string $$s2$$ and form all the interleavings with the remaining portion of $$s2$$ and $$s1$$ to check if the required string $$s1$$ can be formed.

For implementing the recursive function, we make the function call recursively as
$$is\_Interleave(s1,i+1,s2,j,res+s1.charAt(i),s3)$$, in which we have chosen the current character from $$s1$$ and then make another function call $$is\_Interleave(s1,i,s2,j+1,res+s2.charAt(j),s3)$$, in which the current character of $$s2$$ is chosen. Here, $$res$$ refers to that portion(interleaved) of $$s1$$ and $$s2$$ which has already been processed. If anyone of these calls return the result as $$True$$, it means that atleast one interleaving gives the required result $$s3$$. The recursive calls end when both the strings $$s1$$ and $$s2$$ have been fully processed.

Let's look at a small example to see how the execution proceeds.

```
s1="abc"
s2="bcd"
s3="abcbdc"
```

Firstly we choose 'a' of $$s1$$ as the processed part i.e. res and call the recursive function considering the new strings as $$s1$$="bc",
$$s2$$="bcd", $$s3$$="abcbdc". When this function returns a result, we again call the recursive function but with the new strings as $$s1$$="abc", $$s2$$="cd", $$s3$$="abcbdc"


<iframe src="https://leetcode.com/playground/t2zVV2Mu/shared" frameBorder="0" width="100%" height="344" name="t2zVV2Mu"></iframe>

**Complexity Analysis**

* Time complexity : $$O(2^{m+n})$$. $$m$$ is the length of $$s1$$ and $$n$$ is the length of $$s2$$.

* Space complexity : $$O(m+n)$$. The size of stack for recursive calls can go upto $$m+n$$.
<br />
<br />
---
#### Approach 2: Recursion with memoization

**Algorithm**

In the recursive approach discussed above, we are considering every possible string formed by interleaving the two given
strings. But, there will be cases encountered in which, the same portion of $$s1$$ and $$s2$$ would have been processed already
but in different orders(permutations). But irrespective of the order of processing, if the resultant string formed till now
is matching with the required string($$s3$$), the final result is dependent only on the remaining portions of $$s1$$ and $$s2$$, but
not on the already processed portion. Thus, the recursive approach leads to redundant computations.

This redundancy can be removed by making use of memoization along with recursion. For this, we maitain 3 pointers $$i, j, k$$
 which correspond to the index of the current character of $$s1, s2, s3$$ respectively. Also, we maintain a 2D memo array to keep a track of the substrings processed so far. $$memo[i][j]$$ stores a 1/0 or -1 depending on
 whether the current portion of strings i.e. upto $$i^{th}$$ index for $$s1$$ and upto $$j^{th}$$ index for s2 has already been evaluated. Again, we start by selecting the current character of $$s1$$ (pointed by $$i$$). If it matches the current character
 of $$s3$$ (pointed by $$k$$), we include it in the processed string and call the same function recurively as:
 $$is\_Interleave(s1, i+1, s2, j, s3, k+1,memo)$$

Thus, here we have called the function by incrementing the pointers $$i$$ and $$k$$ since the portion of strings upto those indices
 has already been processed. Similarly, we choose one character from the second string and continue. The recursive function
 ends when either of the two strings $$s1$$ or $$s2$$ has been fully processed. If, let's say, the string $$s1$$ has been fully processed,
 we directly compare the remaining portion of $$s2$$ with the remaining portion of $$s3$$. When the backtrack occurs from the recursive
 calls, we store the value returned by the recursive functions in the memoization array memo appropriatelys so that when it is encountered the next time, the recursive function won't be called, but the memoization array itself will return the previous generated result.

 <iframe src="https://leetcode.com/playground/Mikhb9rY/shared" frameBorder="0" width="100%" height="500" name="Mikhb9rY"></iframe>

**Complexity Analysis**

* Time complexity : $$O(2^{m+n})$$. $$m$$ is the length of $$s1$$ and $$n$$ is the length of $$s2$$.

* Space complexity : $$O(m+n)$$. The size of stack for recursive calls can go upto $$m+n$$.
<br />
<br />
---
#### Approach 3: Using 2D Dynamic Programming

**Algorithm**


The recursive approach discussed in above solution included a character from one of the strings $$s1$$ or $$s2$$ in the resultant
interleaved string and called a recursive function to check whether the remaining portions of $$s1$$ and $$s2$$ can be interleaved
to form the remaining portion of $$s3$$. In the current approach, we
 look at the same problem the other way around. Here, we include one character from $$s1$$ or $$s2$$ and check whether the
 resultant string formed so far by one particular interleaving of the the current prefix of $$s1$$ and $$s2$$ form a prefix of $$s3$$.

 Thus, this approach relies on the fact that the in order to determine whether a substring
 of $$s3$$(upto index $$k$$), can be formed by interleaving strings $$s1$$ and $$s2$$ upto indices $$i$$ and $$j$$ respectively, solely depends
 on the characters of $$s1$$ and $$s2$$ upto indices $$i$$ and $$j$$ only and not on the characters coming afterwards.

 To implement this method, we'll make use of a 2D boolean array $$dp$$. In this array $$dp[i][j]$$ implies if it is possible to
 obtain a substring of length $$(i+j+2)$$ which is a prefix of $$s3$$ by some interleaving of prefixes of strings $$s1$$ and $$s2$$ having
 lengths $$(i+1)$$ and $$(j+1)$$ respectively. For filling in the entry of $$dp[i][j]$$, we need to consider two cases:

 1. The character
 just included i.e. either at $$i^{th}$$ index of $$s1$$ or at $$j^{th}$$ index of $$s2$$ doesn't match the character at $$k^{th}$$ index of $$s3$$, where $$k=i+j+1$$.
 In this case, the resultant string formed using some interleaving of prefixes of $$s1$$ and $$s2$$ can never result in a prefix of length $$k+1$$ in $$s3$$. Thus, we enter $$False$$ at the character $$dp[i][j]$$.

 2. The character
 just included i.e. either at $$i^{th}$$ index of $$s1$$ or at $$j^{th}$$ index of $$s2$$  matches the character at $$k^{th}$$ index of $$s3$$, where $$k=i+j+1$$.
Now, if the character just included(say $$x$$) which matches the character at $$k^{th}$$ index of $$s3$$, is the character at $$i^{th}$$ index of $$s1$$, we need to keep $$x$$ at the last position in the resultant interleaved string formed so far. Thus, in order to use string $$s1$$ and $$s2$$ upto indices $$i$$ and $$j$$ to form a resultant string of length $$(i+j+2)$$ which is a prefix of $$s3$$, we need to ensure that the strings $$s1$$ and $$s2$$ upto indices $$(i-1)$$ and $$j$$ respectively obey the same property.

 Similarly, if we just included the $$j^{th}$$ character of $$s2$$, which matches with the $$k^{th}$$ character of $$s3$$, we need to ensure that the strings $$s1$$ and $$s2$$ upto indices $$i$$ and $$(j-1)$$ also obey the same
property to enter a $$true$$ at $$dp[i][j]$$.

This can be made clear with the following example:

```
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
```

<!--![97_Interleaving](../Figures/97_Interleaving.gif)-->
!?!../Documents/97_Interleaving.json:1000,563!?!


<iframe src="https://leetcode.com/playground/3Bj59cXr/shared" frameBorder="0" width="100%" height="429" name="3Bj59cXr"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m \cdot n)$$. dp array of size $$m*n$$ is filled.

* Space complexity : $$O(m \cdot n)$$. 2D dp of size $$(m+1)*(n+1)$$ is required. $$m$$ and $$n$$ are the lengths of strings $$s1$$ and $$s2$$ respectively.
<br />
<br />
---
#### Approach 4: Using 1D Dynamic Programming

**Algorithm**

This approach is the same as the previous approach except that we have used only 1D $$dp$$ array to store the results of the
 prefixes of the strings processed so far. Instead of maintaining a 2D array, we can maintain a 1D array only and update the
 array's element $$dp[i]$$ when needed using $$dp[i-1]$$ and the previous value of $$dp[i]$$.

 <iframe src="https://leetcode.com/playground/5RbcdJJj/shared" frameBorder="0" width="100%" height="429" name="5RbcdJJj"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m \cdot n)$$. dp array of size $$n$$ is filled $$m$$ times.

* Space complexity : $$O(n)$$. $$n$$ is the length of the string $$s1$$.
