# 0004 - Median of Two Sorted Arrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Binary Search, Divide and Conquer | [Leetcode](https://leetcode.com/problems/median-of-two-sorted-arrays) | [solution](https://leetcode.com/problems/median-of-two-sorted-arrays/solution/)

-----------

<p>There are two sorted arrays <b>nums1</b> and <b>nums2</b> of size m and n respectively.</p>

<p>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</p>

<p>You may assume <strong>nums1</strong> and <strong>nums2</strong>&nbsp;cannot be both empty.</p>

<p><b>Example 1:</b></p>

<pre>
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
</pre>

<p><b>Example 2:</b></p>

<pre>
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
</pre>
-----------


## Similar Problems



## Thought:

We show the algorithm as following:

```
1.    a < b
                     a
    list 1     ------|------
                     b
    list 2 ----------|----------

2.
                     a
               ------|---x---    // binary-search b at the list to x
                     b
           ----------|----------
          
3.
                     a
                     |---x---++++++++++   // move right b to here
                     b
     ++++++----------|            // move left a to here

4. Use list A as next list 1, list B as next list 2
   then repeat 1,2,3, untill list 1 has one element.
                     a
                     |---x---++++++++++
                     ===== A
                     b
     ++++++----------|
           =========== B
```

