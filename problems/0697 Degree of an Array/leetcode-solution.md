# 0697 - Degree of an Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/degree-of-an-array) | [solution](https://leetcode.com/problems/degree-of-an-array/solution/)


-----------

<p>Given a non-empty array of non-negative integers <code>nums</code>, the <b>degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>
<p>Your task is to find the smallest possible length of a (contiguous) subarray of <code>nums</code>, that has the same degree as <code>nums</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1, 2, 2, 3, 1]
<b>Output:</b> 2
<b>Explanation:</b> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2,2,3,1,4,2]
<b>Output:</b> 6
</pre>
</p>

<p><b>Note:</b>
<li><code>nums.length</code> will be between 1 and 50,000.</li>
<li><code>nums[i]</code> will be an integer between 0 and 49,999.</li>
</p>

-----------


## Similar Problems

- [Easy] [Maximum Subarray](maximum-subarray)




## Solution:

[TOC]

#### Approach #1: Left and Right Index [Accepted]

**Intuition and Algorithm**

An array that has degree `d`, must have some element `x` occur `d` times.  If some subarray has the same degree, then some element `x` (that occured `d` times), still occurs `d` times.  The shortest such subarray would be from the first occurrence of `x` until the last occurrence.

For each element in the given array, let's know `left`, the index of its first occurrence; and `right`, the index of its last occurrence.  For example, with `nums = [1,2,3,2,5]` we have `left[2] = 1` and `right[2] = 3`.

Then, for each element `x` that occurs the maximum number of times, `right[x] - left[x] + 1` will be our candidate answer, and we'll take the minimum of those candidates.

**Python**
```python
class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
```

**Java**
```java
class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> left = new HashMap(),
            right = new HashMap(), count = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (left.get(x) == null) left.put(x, i);
            right.put(x, i);
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        int ans = nums.length;
        int degree = Collections.max(count.values());
        for (int x: count.keySet()) {
            if (count.get(x) == degree) {
                ans = Math.min(ans, right.get(x) - left.get(x) + 1);
            }
        }
        return ans;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `nums`.  Every loop is through $$O(N)$$ items with $$O(1)$$ work inside the for-block.

* Space Complexity: $$O(N)$$, the space used by `left`, `right`, and `count`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
