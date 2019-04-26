# 0526 - Beautiful Arrangement

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Backtracking | [Leetcode](https://leetcode.com/problems/beautiful-arrangement) | [solution](https://leetcode.com/problems/beautiful-arrangement/solution/)


-----------

<p>Suppose you have <b>N</b> integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these <b>N</b> numbers successfully if one of the following is true for the i<sub>th</sub> position (1 &lt;= i &lt;= N) in this array:</p>

<ol>
	<li>The number at the i<sub>th</sub> position is divisible by <b>i</b>.</li>
	<li><b>i</b> is divisible by the number at the i<sub>th</sub> position.</li>
</ol>

<p>&nbsp;</p>

<p>Now given N, how many beautiful arrangements can you construct?</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 2
<b>Output:</b> 2
<b>Explanation:</b> 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li><b>N</b> is a positive integer and will not exceed 15.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Beautiful Arrangement II](beautiful-arrangement-ii)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

**Algorithm**

In the brute force method, we can find out all the arrays that can be formed using the numbers from 1 to N(by creating every possible permutation of the given elements). Then, we iterate over all the elements of every permutation generated and check for the required conditions of divisibility.

In order to generate all the possible pairings, we make use of a function `permute(nums, current_index)`. This function creates all the possible permutations of the elements of the given array.

To do so, `permute` takes the index of the current element $$current_index$$ as one of the arguments. Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements. After the swapping has been done, it makes another call to permute but this time with the index of the next element in the array. While returning back, we reverse the swapping done in the current function call.

Thus, when we reach the end of the array, a new ordering of the array's elements is generated. The following animation depicts the process of generating the permutations.

!?!../Documents/561_Array.json:1000,563!?!


<iframe src="https://leetcode.com/playground/PqSksc2S/shared" frameBorder="0" name="PqSksc2S" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n!)$$. A total of $$n!$$ permutations will be generated for an array of length $$n$$.

* Space complexity : $$O(n)$$. The depth of the recursion tree can go upto $$n$$. $$nums$$ array of size $$n$$ is used.

---
#### Approach #2 Better Brute Force [Accepted]

**Algorithm**

In the brute force approach, we create the full array for every permutation and then check the array for the given divisibilty conditions. But this method can be optimized to a great extent. To do so, we can keep checking the elements while being added to the permutation array at every step for the divisibility condition and  can stop creating it any further as soon as we find out the element just added to the permutation violates the divisiblity condition. 

<iframe src="https://leetcode.com/playground/WQVaxmVy/shared" frameBorder="0" name="WQVaxmVy" width="100%" height="513"></iframe>

**Complexity Analysis**

* Time complexity : $$O(k)$$. $$k$$ refers to the number of valid permutations.

* Space complexity : $$O(n)$$. The depth of recursion tree can go upto $$n$$. Further, $$nums$$ array of size $$n$$ is used, where, $$n$$ is the given number.

---

#### Approach #3 Backtracking [Accepted]

**Algorithm**


The idea behind this approach is simple. We try to create all the permutations of numbers from 1 to N. We can fix one number at a particular position and check for the divisibility criteria of that number at the particular position. But, we need to keep a track of the numbers which have already been considered earlier so that they aren't reconsidered while generating the permutations. If the current 
number doesn't satisfy the divisibility criteria, we can leave all the permutations that can be generated with that number at the particular position. This helps to prune the search space of the permutations to a great extent. We do so by trying to place each of the numbers at each position.


We make use of a visited array of size $$N$$. Here, $$visited[i]$$ refers to the $$i^{th}$$ number being already placed/not placed in the array being formed till now(True indicates that the number has already been placed).

We make use of a `calculate` function, which puts all the numbers pending numbers from 1 to N(i.e. not placed till now in the array), indicated by a $$False$$ at the corresponding $$visited[i]$$ position, and tries to create all the permutations with those numbers starting from the $$pos$$ index onwards in the current array. While putting the $$pos^{th}$$ number, we check whether the $$i^{th}$$ number satisfies the divisibility criteria on the go i.e. we continue forward with creating the permutations with the number $$i$$ at the $$pos^{th}$$ position only if the number $$i$$ and $$pos$$ satisfy the given criteria. Otherwise, we continue with putting the next numbers at the same position and keep on generating the permutations.

Look at the animation below for a better understanding of the methodology:

!?!../Documents/526_Beautiful.json:1000,563!?!


Below code is inspired by [@shawngao](http://leetcode.com/shawngao)

<iframe src="https://leetcode.com/playground/cBVwozT4/shared" frameBorder="0" name="cBVwozT4" width="100%" height="377"></iframe>
**Complexity Analysis**

* Time complexity : $$O(k)$$. $$k$$ refers to the number of valid permutations.

* Space complexity : $$O(n)$$. $$visited$$ array of size $$n$$ is used. The depth of recursion tree will also go upto $$n$$. Here, $$n$$ refers to the given integer $$n$$.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
