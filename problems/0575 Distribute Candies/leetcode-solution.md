# 0575 - Distribute Candies

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table | [Leetcode](https://leetcode.com/problems/distribute-candies) | [solution](https://leetcode.com/problems/distribute-candies/solution/)


-----------

Given an integer array with <b>even</b> length, where different numbers in this array represent different <b>kinds</b> of candies. Each number means one candy of the corresponding kind. You need to distribute these candies <b>equally</b> in number to brother and sister. Return the maximum number of <b>kinds</b> of candies the sister could gain. 

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> candies = [1,1,2,2,3,3]
<b>Output:</b> 3
<b>Explanation:</b>
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> candies = [1,1,2,3]
<b>Output:</b> 2
<b>Explanation:</b> For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The length of the given array is in range [2, 10,000], and will be even.</li>
<li>The number in given array is in range [-100,000, 100,000].</li>
<ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach 1: Brute Force

**Algorithm**

The brute force approach is really simple. We can generate all the permutations of the given $$nums$$ array representing the candies and determine the number of unique elements in the first half of the generated array.

In order to determine the number of unique elements in the first half of the array, we put all the required elements in a set and count the number of elements in the set. We count such unique elements in the first half of the generated arrays for all the permutations possible and return the size of the largest set.

<iframe src="https://leetcode.com/playground/5bJc432F/shared" frameBorder="0" width="100%" height="497" name="5bJc432F"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n!)$$. A total of $$n!$$ permutations are possible for $$nums$$ array of size $$n$$. 

* Space complexity : $$O(n)$$. The depth of the recursion tree can go upto $$n$$.

---
#### Approach 2: Better Brute Force

**Algorithm**

Before looking into the idea behind this approach, firstly we need to observe one point. The maximum no. of unique candies which the girl can obtain could be atmost $$n/2$$, where $$n$$ refers to the number of candies. Further, in case the number of unique candies are below $$n/2$$, to maximize the number of unique candies that the girl will obtain, we'll assign all the unique candies to the girl. Thus, in such a case, the number of unique candies the girl gets is equal to the total number of unique candies in the given $$candies$$ array. 

Now, let's look at the idea behind this approach. We need to find the total number of unique candies in the given $$candies$$ array. One way to find the number of unique candies is to traverse over the given $$candies$$ array. Whenever we encounter an element, say $$candies[j]$$, we can mark all the elements which are the same as $$candies[j]$$ as invalid and increment the count of unique elements by 1.

Thus, we need to do such markings for all the elements of $$candies$$ array. At the end, $$count$$ gives the required number of unique candies that can be given to the girl. Further, the value to be returned is given by: $$\text{min}(\frac{n}{2}, count)$$. Instead of finding the $$\text{min}$$, we can stop the traversal over the given $$candies$$ array as soon as the $$count$$ exceeds $$\frac{n}{2}$$. 

<iframe src="https://leetcode.com/playground/nLo4nPxj/shared" frameBorder="0" width="100%" height="310" name="nLo4nPxj"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. We traverse over all the elements of $$candies$$ for every new element found. In the worst case, we do so for every element of $$candies$$ array. $$n$$ refers to the size of $$candies$$ array.

* Space complexity : $$O(1)$$. Constant space is used.

---

#### Approach 3: Using Sorting

**Algorithm**

We can sort the given $$candies$$ array and find out the elements which are unique by comparing the adjacent elements of the sorted array. For every new element found(which isn't the same as the previous element), we need to update the $$count$$. At the end, we can return the required result as $$\text{min}(n/2, count)$$, as discussed in the previous approach.

<iframe src="https://leetcode.com/playground/SyAnB5Zm/shared" frameBorder="0" width="100%" height="225" name="SyAnB5Zm"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n\log n)$$. Sorting takes $$O(n\log n)$$ time.

* Space complexity : $$O(1)$$. Constant space is used.

---

#### Approach 4: Using Set

**Algorithm**

Another way to find the number of unique elements is to traverse over all the elements of the given $$candies$$ array and keep on putting the elements in a set. By the property of a set, it will contain only unique elements. At the end, we can count the number of elements in the set, given by, say $$count$$. The value to be returned will again be given by $$\text{min}(count, n/2)$$, as discussed in previous approaches. Here, $$n$$ refers to the size of the $$candies$$ array.

<iframe src="https://leetcode.com/playground/ndMnccZV/shared" frameBorder="0" width="100%" height="208" name="ndMnccZV"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. The entire $$candies$$ array is traversed only once. Here, $$n$$ refers to the size of $$candies$$ array.

* Space complexity : $$O(n)$$. $$set$$ will be of size $$n$$ in the worst case.


---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
