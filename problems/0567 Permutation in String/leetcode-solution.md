# 0567 - Permutation in String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers, Sliding Window | [Leetcode](https://leetcode.com/problems/permutation-in-string) | [solution](https://leetcode.com/problems/permutation-in-string/solution/)


-----------

<p>Given two strings <b>s1</b> and <b>s2</b>, write a function to return true if <b>s2</b> contains the permutation of <b>s1</b>. In other words, one of the first string&#39;s permutations is the <b>substring</b> of the second string.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input: </b>s1 = &quot;ab&quot; s2 = &quot;eidbaooo&quot;
<b>Output: </b>True
<b>Explanation:</b> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>s1= &quot;ab&quot; s2 = &quot;eidboaoo&quot;
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The input strings only contain lower case letters.</li>
	<li>The length of both given strings is in range [1, 10,000].</li>
</ol>


-----------


## Similar Problems

- [Hard] [Minimum Window Substring](minimum-window-substring)

- [Easy] [Find All Anagrams in a String](find-all-anagrams-in-a-string)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

**Algorithm**

The simplest method is to generate all the permutations of the short string  and to check if the generated permutation is a substring of the longer string.

In order to generate all the possible pairings, we make use of a function `permute(string_1, string_2, current_index)`. This function creates all the possible permutations of the short string $$s1$$.

To do so, permute takes the index of the current element $$current_index$$ as one of the arguments. Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements. After the swapping has been done, it makes another call to permute but this time with the index of the next element in the array. While returning back, we reverse the swapping done in the current function call.

Thus, when we reach the end of the array, a new ordering of the array's elements is generated. The following animation depicts the process of generating the permutations.

!?!../Documents/561_Array.json:1000,563!?!

<iframe src="https://leetcode.com/playground/p3HAqkFZ/shared" frameBorder="0" name="p3HAqkFZ" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n!)$$. We match all the permutations of the short string $$s1$$, of length $$s1$$, with $$s2$$. Here, $$n$$ refers to the length of $$s1$$.

* Space complexity : $$O(n^2)$$. The depth of the recursion tree is $$n$$($$n$$ refers to the length of the short string $$s1$$). Every node of the recursion tree contains a string of max. length $$n$$.

---

#### Approach #2 Using sorting [Time Limit Exceeded]:

**Algorithm**

The idea behind this approach is that one string will be a permutation of another string only if both of them contain the same characters the same number of times. One string $$x$$ is a permutation of other string $$y$$ only if $$sorted(x)=sorted(y)$$. 

In order to check this, we can sort the two strings and compare them.  We sort the short string $$s1$$ and all the substrings of $$s2$$, sort them and compare them with the sorted $$s1$$ string. If the two match completely, $$s1$$'s permutation is a substring of $$s2$$, otherwise not.

<iframe src="https://leetcode.com/playground/zWvWj8oK/shared" frameBorder="0" name="zWvWj8oK" width="100%" height="326"></iframe>

**Complexity Analysis**

* Time complexity : $$O\big(l_1log(l_1)+(l_2-l_1)l_1log(l_1)\big)$$. where $$l_1$$ is the length of string $$l_1$$ and $$l_2$$ is the length of string $$l_2$$.

* Space complexity : $$O(l_1)$$. $$t$$ array is used .

---

#### Approach #3 Using Hashmap [Time Limit Exceeded]

**Algorithm**

As discussed above, one string will be a permutation of another string only if both of them contain the same charaters with the same frequency. We can consider every possible substring in the long string $$s2$$ of the same length as that of $$s1$$ and check the frequency of occurence of the characters appearing in the two. If the frequencies of every letter match exactly, then only $$s1$$'s permutation can be a substring of $$s2$$. 

In order to implement this approach, instead of sorting and then comparing the elements for equality, we make use of a hashmap $$s1map$$ which stores the frequency of occurence of all the characters in the short string $$s1$$. We consider every possible substring of $$s2$$ of the same length as that of $$s1$$, find its corresponding hashmap as well, namely $$s2map$$. Thus, the substrings considered can be viewed as a window of length as that of $$s1$$ iterating over $$s2$$. If the two hashmaps obtained are identical for any such window, we can conclude that $$s1$$'s permutation is a substring of $$s2$$, otherwise not.

<iframe src="https://leetcode.com/playground/SvwMjwJX/shared" frameBorder="0" name="SvwMjwJX" width="100%" height="513"></iframe>

**Complexity Analysis**

* Time complexity : $$O(l_1+26*l_1*(l_2-l_1))$$. hashmap contains atmost 26 keys. where $$l_1$$ is the length of string $$l_1$$ and $$l_2$$ is the length of string $$l_2$$.

* Space complexity : $$O(1)$$. hashmap contains atmost 26 key-value pairs.

---
#### Approach #4 Using Array [Accepted]

**Algorithm**

Instead of making use of a special HashMap datastructure just to store the frequency of occurence of characters, we can use a simpler array data structure to store the frequencies. Given strings contains only lowercase alphabets ('a' to 'z'). So we need to take an array of size 26.The rest of the process remains the same as the last approach.

<iframe src="https://leetcode.com/playground/48H3F2LJ/shared" frameBorder="0" name="48H3F2LJ" width="100%" height="496"></iframe>
**Complexity Analysis**

* Time complexity : $$O(l_1+26*l_1*(l_2-l_1))$$,  where $$l_1$$ is the length of string $$l_1$$ and $$l_2$$ is the length of string $$l_2$$.

* Space complexity : $$O(1)$$. $$s1map$$ and $$s2map$$ of size 26 is used.

---
#### Approach #5 Sliding Window  [Accepted]:

**Algorithm**

Instead of generating the hashmap afresh for every window considered in $$s2$$, we can create the hashmap just once for the first window in $$s2$$. Then, later on when we slide the window, we know that we add one preceding character and add a new succeeding character to the new window considered. Thus, we can update the hashmap by just updating the indices associated with those two characters only. Again, for every updated hashmap, we compare all the elements of the hashmap for equality to get the required result.

<iframe src="https://leetcode.com/playground/o4pqWwhn/shared" frameBorder="0" name="o4pqWwhn" width="100%" height="496"></iframe>

**Complexity Analysis**

* Time complexity : $$O(l_1+26*(l_2-l_1))$$,  where $$l_1$$ is the length of string $$l_1$$ and $$l_2$$ is the length of string $$l_2$$.

* Space complexity : $$O(1)$$. Constant space is used.

---
#### Approach #6 Optimized Sliding Window [Accepted]:

**Algorithm**

The last approach can be optimized, if instead of comparing all the elements of the hashmaps for every updated $$s2map$$ corresponding to every window of $$s2$$ considered, we keep a track of the number of elements which were already matching in the earlier hashmap and update just the count of matching elements when we shift the window towards the right.

To do so, we maintain a $$count$$ variable, which stores the number of characters(out of the 26 alphabets), which have the same frequency of occurence in $$s1$$ and the current window in $$s2$$. When we slide the window, if the deduction of the last element and the addition of the new element leads to a new frequency match of any of the characters, we increment the $$count$$ by 1. If not, we keep the $$count$$ intact. But, if a character whose frequency was the same earlier(prior to addition and removal) is added, it now leads to a frequency mismatch which is taken into account by decrementing the same $$count$$ variable. If, after the shifting of the window, the $$count$$ evaluates to 26, it means all the characters match in frequency totally. So, we return a True in that case immediately.

<iframe src="https://leetcode.com/playground/T5J3SxqR/shared" frameBorder="0" name="T5J3SxqR" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(l_1+(l_2-l_1))$$. where $$l_1$$ is the length of string $$l_1$$ and $$l_2$$ is the length of string $$l_2$$.

* Space complexity : $$O(1)$$. Constant space is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
