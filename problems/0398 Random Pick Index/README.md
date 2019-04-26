# 0398 - Random Pick Index

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Reservoir Sampling | [Leetcode](https://leetcode.com/problems/random-pick-index) | [solution](https://leetcode.com/problems/random-pick-index/solution/)


-----------

<p>Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.</p>

<p><b>Note:</b><br />
The array size can be very large. Solution that uses too much extra space will not pass the judge.</p>

<p><b>Example:</b></p>

<pre>
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
</pre>


-----------


## Similar Problems

- [Medium] [Linked List Random Node](linked-list-random-node)

- [Hard] [Random Pick with Blacklist](random-pick-with-blacklist)

- [Medium] [Random Pick with Weight](random-pick-with-weight)




## Thought:
