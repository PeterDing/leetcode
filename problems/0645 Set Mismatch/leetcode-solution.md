# 0645 - Set Mismatch

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table, Math | [Leetcode](https://leetcode.com/problems/set-mismatch) | [solution](https://leetcode.com/problems/set-mismatch/solution/)


-----------

<p>
The set <code>S</code> originally contains numbers from 1 to <code>n</code>. But unfortunately, due to the data error, one of the numbers in the set got duplicated to <b>another</b> number in the set, which results in repetition of one number and loss of another number. 
</p>

<p>
Given an array <code>nums</code> representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> nums = [1,2,2,4]
<b>Output:</b> [2,3]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The given array size will in the range [2, 10000].</li>
<li>The given array's numbers won't have any order.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Find the Duplicate Number](find-the-duplicate-number)




## Solution:

[TOC]

## Solution

 
#### Approach 1: Brute Force

The most naive solution is to consider each number from $$1$$ to $$n$$, and traverse over the whole $$nums$$ array to check if the current number occurs twice in $$nums$$
or doesn't occur at all. We need to set the duplicate number, $$dup$$ and the missing number, $$missing$$, appropriately in such cases respectively.

<iframe src="https://leetcode.com/playground/ugiTepy3/shared" frameBorder="0" width="100%" height="344" name="ugiTepy3"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. We traverse over the $$nums$$ array of size $$n$$ for each of the numbers from $$1$$ to $$n$$.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br>
<br>

---

#### Approach 2: Better Brute Force

In the last approach, we continued the search process, even when we've already found the duplicate and the missing number. But, as per the problem statement, 
we know that only one number will be repeated and only one number will be missing. Thus, we can optimize the last approach to some extent, by stopping 
the search process as soon as we find these two required numbers.

<iframe src="https://leetcode.com/playground/PcMPwwzf/shared" frameBorder="0" width="100%" height="378" name="PcMPwwzf"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. We traverse over the $$nums$$ array of size $$n$$ for each of the numbers from $$1$$ to $$n$$, in the worst case.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br>
<br>

---
#### Approach 3: Using Sorting

**Algorithm**

One way to further optimize the last approach is to sort the given $$nums$$ array. This way, the numbers which are equal will always lie together. 
Further, we can easily identify the missing number by checking if every two consecutive elements in the sorted $$nums$$ array are just one count apart or not.


<iframe src="https://leetcode.com/playground/Dj9BhAnK/shared" frameBorder="0" width="100%" height="276" name="Dj9BhAnK"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n\log n)$$. Sorting takes $$O(n\log n)$$ time.

* Space complexity : $$O(\log n)$$. Sorting takes $$O(\log n)$$ space. 
<br>
<br>

---
#### Approach 4: Using Map

**Algorithm**

The given problem can also be solved easily if we can somehow keep a track of the number of times each element of the $$nums$$ array occurs. One way to 
do so is to make an entry for each element of $$nums$$ in a HashMap $$map$$. This $$map$$ stores the entries in the form $$(num_i, count_i)$$. Here, $$num$$ refers to
the $$i^{th}$$ element in $$nums$$ and $$count_i$$ refers to the number of times this element occurs in $$nums$$.
  Whenever, the same element occurs again, we can increment the count corresponding to the 
same. 

After this, we can consider every number from $$1$$ to $$n$$, and check for its presence in $$map$$. If it isn't present, we can update the $$missing$$ variable 
appropriately. But, if the $$count$$ corresponding to the current number is $$2$$, we can update the $$dup$$ variable with the current number.

<iframe src="https://leetcode.com/playground/kz9G9DPq/shared" frameBorder="0" width="100%" height="344" name="kz9G9DPq"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Traversing over $$nums$$ of size $$n$$ takes $$O(n)$$ time. Considering each number from $$1$$ to $$n$$ also takes $$O(n)$$ time.

* Space complexity : $$O(n)$$. $$map$$ can contain atmost $$n$$ entries for each of the numbers from $$1$$ to $$n$$.
<br>
<br>

---
#### Approach 5: Using Extra Array

**Algorithm**

In the last approach, we make use of a $$map$$ to store the elements of $$nums$$ along with their corresponding counts. But, we can note, that each entry in $$map$$ 
requires two entries. Thus, putting up $$n$$ entries requires $$2n$$ space actually. We can reduce this space required to $$n$$ by making use of an array, $$arr$$ instead.
Now, the indices of $$arr$$ can be used instead of storing the elements again. Thus, we make use of $$arr$$ in such a way that, $$arr[i]$$ is used to store 
the number of occurences of the element $$i+1$$. The rest of the process remains the same as in the last approach.

<iframe src="https://leetcode.com/playground/QJRi2ZuU/shared" frameBorder="0" width="100%" height="327" name="QJRi2ZuU"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Traversing over $$nums$$ of size $$n$$ takes $$O(n)$$ time. Considering each number from $$1$$ to $$n$$ also takes $$O(n)$$ time.

* Space complexity : $$O(n)$$. $$arr$$ can contain atmost $$n$$ elements for each of the numbers from $$1$$ to $$n$$.
<br>
<br>

---

#### Approach 6: Using Constant Space

**Algorithm**

We can save the space used in the last approach, if we can somehow, include the information regarding the duplicacy of an element or absence of an element
 in the $$nums$$ array. Let's see how this can be done.
 
 We know that all the elements in the given $$nums$$ array are positive, and lie in the range $$1$$ to $$n$$ only. Thus, we can pick up each element $$i$$ 
 from $$nums$$. For every number $$i$$ picked up, we can invert the element at the index $$\left|i\right|$$. By doing so,  if one of the elements $$j$$ occurs twice, 
when this number is encountered the second time,  the element $$nums[\left|i\right|]$$ will be found to be negative. 
Thus, while doing the inversions, we can check if a number found is already negative, to find the duplicate number.
 
 After the inversions have been done, if all the elements in $$nums$$ are present correctly, the resultant $$nums$$ array will have all the elements as 
 negative now. But, if one of the numbers, $$j$$ is missing, the element at the $$j^{th}$$ index will be positive. This  can be used to determine the missing number.
 

<iframe src="https://leetcode.com/playground/RJUw9UMo/shared" frameBorder="0" width="100%" height="327" name="RJUw9UMo"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Two traversals over the $$nums$$ array of size $$n$$ are done.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br>
<br>

---
#### Approach 7: Using XOR

**Algorithm**

Before we dive into the solution to this problem, let's consider a simple problem. Consider an array with $$n-1$$ elements containing numbers from $$1$$ to $$n$$ with one number missing out of them. Now, how to we find out this missing element. One of the solutions is to take the XOR of all the elements of this array with all the numbers from $$1$$ to $$n$$. By doing so, we get the required missing number. This works because XORing a number with itself results in a 0 result. Thus, only the number which is missing can't get cancelled with this XORing.

Now, using this idea as the base, let's take it a step forward and use it for the current problem. By taking the XOR of all the elements of the given $$nums$$ array with all the numbers from $$1$$ to $$n$$, we will get a result, $$xor$$, as $$x^y$$. Here, $$x$$ and $$y$$ refer to the repeated and the missing term in the given $$nums$$ array. This happens on the same grounds as in the first problem discussed above.

Now, in the resultant $$xor$$, we'll get a 1 in the binary representation only at those bit positions which have a 1 in one out of the numbers $$x$$ and $$y$$, and a 0 at the same bit position in the other one. In the current solution, we consider the rightmost bit which is 1 in the $$xor$$, although any bit would work. Let's say, this position is called the $$rightmostbit$$. 

If we divide the elements of the given $$nums$$ array into two parts such that the first set contains the elements which have a 1 at the $$rightmostbit$$ position and the second set contains the elements having a 0 at the same position, we'll get one out of $$x$$ or $$y$$ in one set and the other one in the second set. Now, our problem has reduced somewhat to the simple problem discussed above.

To solve this reduced problem, we can find out the elements from $$1$$ to $$n$$ and consider them as a part of the previous sets only, with the allocation of the set depending on a 1 or 0 at the $$righmostbit$$ position. 

Now, if we do the XOR of all the elements of the first set, all the elements will result in an XOR of 0, due to cancellation of the similar terms in both $$nums$$ and the numbers $$(1:n)$$, except one term, which is either $$x$$ or $$y$$. 

For the other term, we can do the XOR of all the elements in the second set as well.

Consider the example `[1 2 4 4 5 6]`

![XOR](../Figures/645_Set_Mismatch.PNG)


One more traversal over the $$nums$$ can be used to identify the missing and the repeated number out of the two numbers found.

<iframe src="https://leetcode.com/playground/USgeoHAo/shared" frameBorder="0" width="100%" height="500" name="USgeoHAo"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. We iterate over $$n$$ elements five times.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br>
<br>

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
