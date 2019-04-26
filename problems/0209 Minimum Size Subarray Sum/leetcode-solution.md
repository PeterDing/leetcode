# 0209 - Minimum Size Subarray Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Two Pointers, Binary Search | [Leetcode](https://leetcode.com/problems/minimum-size-subarray-sum) | [solution](https://leetcode.com/problems/minimum-size-subarray-sum/solution/)


-----------

<p>Given an array of <strong>n</strong> positive integers and a positive integer <strong>s</strong>, find the minimal length of a <b>contiguous</b> subarray of which the sum &ge; <strong>s</strong>. If there isn&#39;t one, return 0 instead.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> <code>s = 7, nums = [2,3,1,2,4,3]</code>
<strong>Output:</strong> 2
<strong>Explanation: </strong>the subarray <code>[4,3]</code> has the minimal length under the problem constraint.</pre>

<div class="spoilers"><b>Follow up:</b></div>

<div class="spoilers">If you have figured out the <i>O</i>(<i>n</i>) solution, try coding another solution of which the time complexity is <i>O</i>(<i>n</i> log <i>n</i>).&nbsp;</div>


-----------


## Similar Problems

- [Hard] [Minimum Window Substring](minimum-window-substring)

- [Medium] [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k)

- [Medium] [Maximum Length of Repeated Subarray](maximum-length-of-repeated-subarray)




## Solution:

[TOC]

## Solution
---
#### Approach #1 Brute force [Time Limit Exceeded]

**Intuition**

Do as directed in question. Find the sum for all the possible subarrays and update the $$\text{ans}$$ as and when we get a better subarray that fulfill the requirements ($$\text{sum} \geq \text{s}$$).

**Algorithm**

* Initialize $$\text{ans}=\text{INT_MAX}$$
* Iterate the array from left to right using $$i$$:
    + Iterate from the current element to the end of vector using $$j$$:
        - Find the $$\text{sum}$$ of elements from index $$i$$ to $$j$$
        - If sum is greater then $$s$$:
            * Update $$\text{ans} = \min(\text{ans}, (j - i + 1))$$
            * Start the next $$i$$th iteration, since, we got the smallest subarray with $$\text{sum} \geq s$$ starting from the current index.


<iframe src="https://leetcode.com/playground/VzAVPq7w/shared" frameBorder="0" name="VzAVPq7w" width="100%" height="360"></iframe>

**Complexity Analysis**

* Time complexity: $$O(n^3)$$.
    + For each element of array, we find all the subarrays starting from that index which is $$O(n^2)$$.
    + Time complexity to find the sum of each subarray is $$O(n)$$.
    + Thus, the total time complexity : $$O(n^2 * n) = O(n^3)$$

* Space complexity: $$O(1)$$ extra space.

---
#### Approach #2 A better brute force [Accepted]

**Intuition**

In Approach #1, you may notice that the sum is calculated for every surarray in $$O(n)$$ time. But, we could easily find the sum in O(1) time by storing the cumulative sum from the beginning(Memoization). After we have stored the cumulative sum in $$\text{sums}$$, we could easily find the sum of any subarray from $$i$$ to $$j$$.

**Algorithm**

* The algorithm is similar to Approach #1.
* The only difference is in the way of finding the sum of subarrays:
    + Create a vector $$\text{sums}$$ of size of $$\text{nums}$$
    + Initialize $$\text{sums}[0]=\text{nums}[0]$$
    + Iterate over the $$\text{sums}$$ vector:
        - Update $$\text{sums}[i] = \text{sums}[i-1] + \text{nums}[i]$$
    + Sum of subarray from $$i$$ to $$j$$ is calculated as:
    $$\text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]$$, , wherein $$\text{sums}[j] - \text{sums}[i]$$ is the sum from ($$i+1$$)th element to the $$j$$th element.


<iframe src="https://leetcode.com/playground/zpQxiiBt/shared" frameBorder="0" name="zpQxiiBt" width="100%" height="411"></iframe>

**Complexity analysis**

* Time complexity: $$O(n^2)$$.
    + Time complexity to find all the subarrays is $$O(n^2)$$.
    + Sum of the subarrays is calculated in $$O(1)$$ time.
    + Thus, the total time complexity: $$O(n^2 * 1) = O(n^2)$$

* Space complexity: $$O(n)$$ extra space.
    + Additional $$O(n)$$ space for $$\text{sums}$$ vector than in Approach #1.

---
#### Approach #3 Using Binary search [Accepted]

**Intuition**

We could further improve the Approach #2 using the binary search. Notice that we find the subarray with $$\text{sum} >=\text{s}$$ starting with an index $$i$$ in $$O(n)$$ time. But, we could reduce the time to $$O(\log(n))$$ using binary search. Note that in Approach #2, we search for subarray starting with index $$i$$, until we find $$\text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]$$ that is greater than $$\text{s}$$. So, instead of iterating linearly to find the sum, we could use binary search to find the index that is not lower than  $$\text{s}-\text{sums[i]}$$ in the $$\text{sums}$$, which can be done using $$\text{lower_bound}$$ function in C++ STL or could be implemented manually.

**Algorithm**

* Create vector $$sums$$ of size $$n+1$$ with :
$$\text{sums}[0]=0\text{, }\text{sums}[i]=\text{sums}[i-1]+\text{nums}[i-1]$$

* Iterate from $$i=1$$ to $$n$$:
    + Find the value $$\text{to_find}$$ in $$\text{sum}$$ required for minimum subarray starting from index $$i$$ to have sum greater than $$s$$, that is:
    $$\text{to_find}=\text{s}+\text{sums}[i-1]$$
    + Find the index in $$\text{sums}$$ such that value at that index is not lower than the $$\text{to_find}$$ value, say $$\text{bound}$$
    + If we find the $$\text{to_find}$$ in $$\text{sums}$$, then:
        - Size of current subarray is given by:
          $$\text{bound} - (\text{sums.begin}()+i-1)$$
        - Compare $$ans$$ with the current subarray size and store minimum in $$ans$$


<iframe src="https://leetcode.com/playground/hVhQq7az/shared" frameBorder="0" name="hVhQq7az" width="100%" height="411"></iframe>

**Complexity analysis**

* Time complexity: $$O(n\log(n))$$.
    + For each element in the vector, find the subarray starting from that index, and having sum greater than $$s$$ using binary search. Hence, the time required is $$O(n)$$ for iteration over the vector and $$O(\log(n))$$ for finding the subarray for each index using binary search.
    + Therefore, total time complexity = $$O(n*\log(n))$$
* Space complexity: $$O(n)$$. Additional $$O(n)$$ space for $$\text{sums}$$ vector

---
#### Approach #4 Using 2 pointers [Accepted]

**Intuition**

Until now, we have kept the starting index of subarray fixed, and found the last position. Instead, we could move the starting index of the current subarray as soon as we know that no better could be done with this index as the starting index. We could keep 2 pointer,one for the start and another for the end of the current subarray, and make optimal moves so as to keep the $$\text{sum}$$ greater than $$s$$ as well as maintain the lowest size possible.

**Algorithm**

* Initialize $$\text{left}$$ pointer to 0 and $$\text{sum}$$ to 0
* Iterate over the $$\text{nums}$$:
    + Add $$\text{nums}[i]$$ to $$\text{sum}$$
    + While $$\text{sum}$$ is greater than or equal to $$s$$:
        - Update $$\text{ans}=\min(\text{ans},i+1-\text{left})$$, where $$i+1-\text{left}$$ is the size of current subarray
        - It means that the first index can safely be incremented, since, the minimum subarray starting with this index with $$\text{sum} \geq s$$ has been achieved
        - Subtract $$\text{nums[left]}$$ from $$\text{sum}$$ and increment $$\text{left}$$


<iframe src="https://leetcode.com/playground/TxnK5kAo/shared" frameBorder="0" name="TxnK5kAo" width="100%" height="309"></iframe>

**Complexity analysis**

* Time complexity: $$O(n)$$. Single iteration of $$O(n)$$.
    + Each element can be visited atmost twice, once by the right pointer($$i$$) and (atmost)once by the $$\text{left}$$ pointer.
* Space complexity: $$O(1)$$ extra space. Only constant space required for $$\text{left}$$, $$\text{sum}$$, $$\text{ans}$$ and $$i$$.

---
Analysis written by [@abhinavbansal0](https://leetcode.com/abhinavbansal0).
