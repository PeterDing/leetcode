# 0704 - Binary Search

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Binary Search | [Leetcode](https://leetcode.com/problems/binary-search) | [solution](https://leetcode.com/problems/binary-search/solution/)


-----------

<p>Given a <strong>sorted</strong> (in ascending order) integer array <code>nums</code> of <code>n</code> elements and a <code>target</code> value, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index, otherwise return <code>-1</code>.</p>

<p><br />
<strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in <code>nums</code> and its index is 4

</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in <code>nums</code> so return -1
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>You may assume that all elements in <code>nums</code> are unique.</li>
	<li><code>n</code> will be in the range <code>[1, 10000]</code>.</li>
	<li>The value of each element in <code>nums</code> will be in the range <code>[-9999, 9999]</code>.</li>
</ol>


-----------


## Similar Problems

- [Medium] [Search in a Sorted Array of Unknown Size](search-in-a-sorted-array-of-unknown-size)




## Solution:

[TOC]

## Solution

---

#### Approach 1: Binary Search 

**Intuition**

[Binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
is a textbook algorithm based on the idea to 
compare the target value to the middle element of the array.

If the target value is equal to the middle element - we're done.

If the target value is smaller - continue to search on the left.

If the target value is larger - continue to search on the right.

![postorder](../Figures/704/search.png)

**Algorithm**

- Initialise left and right pointers : `left = 0`, `right = n - 1`.

- While `left <= right` :

    - Compare middle element of the array `nums[pivot]` to the target
    value `target`.
    
        - If the middle element _is_ the target `target = nums[pivot]` : return `pivot`. 
        
        - If the target is not yet found : 
        
            - If `target < nums[pivot]`, continue the search on the left 
            `right = pivot - 1`.
            
            - Else continue the search on the right 
            `left = pivot + 1`.
            
**Implementation**

!?!../Documents/704_LIS.json:1000,401!?!

<iframe src="https://leetcode.com/playground/iryawqoR/shared" frameBorder="0" width="100%" height="310" name="iryawqoR"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(\log N)$$. 

    Let's compute time complexity with the help of 
    [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) 
    $$T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)$$.
    The equation represents dividing the problem 
    up into $$a$$ subproblems of size $$\frac{N}{b}$$ in $$\Theta(N^d)$$ time. 
    Here at step there is only one subproblem `a = 1`, its size 
    is a half of the initial problem `b = 2`, 
    and all this happens in a constant time `d = 0`.
    That means that $$\log_b{a} = d$$ and hence we're dealing with 
    [case 2](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example)
    that results in $$\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)$$
    = $$\mathcal{O}(\log N)$$ time complexity.
 
* Space complexity : $$\mathcal{O}(1)$$ since it's a constant space
solution.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
