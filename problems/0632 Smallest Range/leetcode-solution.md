# 0632 - Smallest Range

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Hash Table, Two Pointers, String | [Leetcode](https://leetcode.com/problems/smallest-range) | [solution](https://leetcode.com/problems/smallest-range/solution/)


-----------

<p>You have <code>k</code> lists of sorted integers in ascending order. Find the <b>smallest</b> range that includes at least one number from each of the <code>k</code> lists. </p>

<p>We define the range [a,b] is smaller than range [c,d] if <code>b-a < d-c</code> or <code>a < c</code> if <code>b-a == d-c</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
<b>Output:</b> [20,24]
<b>Explanation:</b> 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
</pre>
</p>

<p>
<b>Note:</b><br/>
<ol>
<li>The given list may contain duplicates, so ascending order means >= here.</li>
<li>1 <= <code>k</code> <= 3500</li>
<li> -10<sup>5</sup> <= <code>value of elements</code> <= 10<sup>5</sup>.</li>
<li><b>For Java users, please note that the input type has been changed to List&lt;List&lt;Integer&gt;&gt;. And after you reset the code template, you'll see this point.</b></li>
</ol>
<br/>
</p>

-----------


## Similar Problems

- [Hard] [Minimum Window Substring](minimum-window-substring)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

The naive approach is to consider every pair of elements, $$nums[i][j]$$ and $$nums[k][l]$$ from amongst the given 
lists and consider the range formed by these elements. For every range currently considered, we can traverse over all the 
lists to find if atleast one element from these lists can be included in the current range. If so, we store the end-points of the current range 
and compare it with the previous minimum range found, if any, satisfying the required criteria, to find the smaller range from among them.

Once all the element pairs have been considered as the ranges, we can obtain the required minimum range.

<iframe src="https://leetcode.com/playground/SMprvqVp/shared" frameBorder="0" name="SMprvqVp" width="100%" height="515"></iframe>


**Complexity Analysis**

* Time complexity : $$O(n^3)$$. Considering every possible range(element pair) requires $$O(n^2)$$ time. For each range considered, 
we need to traverse over all the elements of the given lists in the worst case requiring another $$O(n)$$ time. Here, $$n$$ refers to the 
total number of elements in the given lists.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
#### Approach #2 Better Brute Force [Time Limit Exceeded]

**Algorithm**

In the last approach, we consider every possible range and then traverse over every list to check if atleast one of the 
elements from these lists lies in the required range. Instead of doing this traversal for every range, we can make use 
of Binary Search to find the index of the element just larger than(or equal to) the lower limit of the range currently 
considered. 

If all the elements in the current list are lesser than this lower limit, we'll get the index as $$nums[k].length$$
 for the $$k^{th}$$ list being currently checked. In this case, none of the elements of the current list lies in the
current range.

 On the other hand, if all the elements in this list are larger than this lower limit, we'll get the index of the first element(minimum) in the current list. If this element happens to be larger than the upper limit  of the range currently considered, then also, none of the elements of the current list lies within the current range.
 
 Whenever a range is found which satisfies the required criteria, we can compare it with the minimum range found so far 
 to determine the required minimum range.

<iframe src="https://leetcode.com/playground/uXxKqhkz/shared" frameBorder="0" name="uXxKqhkz" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O\big(n^2log(k)\big)$$. The time required to consider every possible range is $$O(n^2)$$. For every range currently considered, 
a Binary Search requiring $$O\big(log(k)\big)$$ time is required. Here, $$n$$ refers to the total number of elements in the given 
lists and $$k$$ refers to the average length of each list.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
#### Approach #3  Using Pointers [Time Limit Exceeded]

**Algorithm**

We'll discuss about the implementation used in the current approach along with the idea behind it. 

This approach makes use of an array of pointers, $$next$$, whose length is equal to the number of given lists. In this 
array, $$next[i]$$ refers to the element which needs to be considered next in the $$(i-1)^{th}$$ list. The meaning of this will become 
more clearer when we look at the process.

We start by initializing all the elements of $$next$$ to 0. Thus, currently, we are considering the first(minimum) element 
among all the lists. Now, we find out the index of the list containing the maximum($$max_i$$) and minimum($$min_i$$) 
elements from amongst the elements currently pointed by $$next$$. The range formed by these maximum and minimum elements surely  
contains atleast one element from each list. 

But, now our objective is to minimize this range. To do so, there are two options: Either decrease the maximum value or increase the 
minimum value. 

Now, the maximum value can't be reduced any further, since it already corresponds to the minimum value in one of the lists. 
Reducing it any further will lead to the exclusion of all the elements of this list(containing the last maximum value) 
from the new range. 

Thus, the only option left in our hand is to try to increase the minimum value. To do so, we now need to consider the
 next element in the list containing the last minimum value. Thus, we increment the entry at the corresponding index
  in $$next$$, to indicate that the next element in this list now needs to be considered. 
  
  Thus, at every step, we find the maximum and minimum values being pointed currently, update the $$next$$ values 
  appropriately, and also find out the range formed by these maximum and minimum values to find out the smallest range 
 satisfying the given criteria. 
 
 While doing this process, if any of the lists gets completely exhausted, it means that the minimum value being increased for 
 minimizing the range being considered can't be increased any further, without causing the exclusion of all the elements in atleast 
 one of the lists. Thus, we can stop the search process whenever any list gets completely exhausted.
 
 We can also stop the process, when all the elements of the given lists have been exhausted.
 
 Summarizing the statements above, the process becomes:
 
 1. Initialize $$next$$ array(pointers) with all 0's.
 
 2. Find the indices of the lists containing the minimum($$min_i$$) and the maximum($$max_i$$) elements amongst the elements pointed by the $$next$$ array.
 
 3. If the range formed by the maximum and minimum elements found above is larger than the previous maximum range, update the boundary values used for the maximum range.
 
 4. Increment the pointer $$nums[min_i]$$.
 
 5. Repeat steps 2 to 4 till any of the lists gets exhausted.
 
 The animation below illustrates the process for a visual understanding of the process.
 
 !?!../Documents/632_Smallest_Range.json:1000,563!?!


<iframe src="https://leetcode.com/playground/rnPo3vGZ/shared" frameBorder="0" name="rnPo3vGZ" width="100%" height="513"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n*m)$$. In the worst case, we need to traverse over $$next$$ array(of length $$m$$) for all the elements of the given lists.
Here, $$n$$ refers to the total number of elements in all the lists. $$m$$ refers to the total number of lists.

* Space complexity : $$O(m)$$. $$next$$ array of size $$m$$ is used.

---
#### Approach #4 Using Priority Queue [Accepted]:

**Algorithm**

In the last approach, at each step, we update the pointer corresponding to the current minimum element and traverse over the whole
$$next$$ array to determine the new maximum and minimum values. We can do some optimization here, by making use of a simple observation.

Whenever we update a single entry of $$next$$ to consider the new maximum and minimum values(if we already know the last maximum 
and minimum values), all the elements to be considered for finding the maximum and minimum values remain the same except the new element 
being pointed by a single updated entry in $$next$$.  This new entry is certainly larger than the last minimum value(since that was the 
reasoning behind the updation). 

Thus, we can't be sure whether this is the new minimum element or not. But, since it is larger than the last 
value being considered, it could be a potential competitor for the new maximum value. Thus, we can directly compare it with the last 
maximum value to determine the current maximum value.

Now, we're left with finding the minimum value iteratively at every step. To avoid this iterative process, a better idea 
is to make use of a Min-Heap, which stores the values being pointed currently by the $$next$$ array. Thus, the minimum value always 
lies at the top of this heap, and we need not do the iterative search process. 

At every step, we remove the minimum element from this heap and find out the range formed by the current maximum and minimum values, and 
compare it with the minimum range found so far to determine the required minimum range. We also update the increment the index in $$next$$ 
corresponding to the list containing this minimum entry and add this element to the heap as well.

The rest of the process remains the same as the last approach.

<iframe src="https://leetcode.com/playground/kBqfu7ju/shared" frameBorder="0" name="kBqfu7ju" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O\big(n*log(m)\big)$$. Heapification of $$m$$ elements requires $$O\big(log(m)\big)$$ time. This step could be done 
for all the elements of the given lists in the worst case. Here, $$n$$ refers to the total number of elements in 
all the lists. $$m$$ refers to the total number of lists.


* Space complexity : $$O(m)$$. $$next$$ array of size $$m$$ is used. A Min-Heap with $$m$$ elements is also used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
