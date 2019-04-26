# 0011 - Container With Most Water

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Two Pointers | [Leetcode](https://leetcode.com/problems/container-with-most-water) | [solution](https://leetcode.com/problems/container-with-most-water/solution/)


-----------

<p>Given <i>n</i> non-negative integers <i>a<sub>1</sub></i>, <i>a<sub>2</sub></i>, ..., <i>a<sub>n&nbsp;</sub></i>, where each represents a point at coordinate (<i>i</i>, <i>a<sub>i</sub></i>). <i>n</i> vertical lines are drawn such that the two endpoints of line <i>i</i> is at (<i>i</i>, <i>a<sub>i</sub></i>) and (<i>i</i>, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.</p>

<p><strong>Note:&nbsp;</strong>You may not slant the container and <i>n</i> is at least 2.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" /></p>

<p><small>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49. </small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49</pre>


-----------


## Similar Problems

- [Hard] [Trapping Rain Water](trapping-rain-water)




## Solution:

[TOC]

## Summary
We have to maximize the Area that can be formed between the vertical lines using the shorter line as length and the distance between the lines as the width of the rectangle forming the area.

## Solution
---

#### Approach 1: Brute Force

**Algorithm**

In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.

<iframe src="https://leetcode.com/playground/gL3JYnab/shared" frameBorder="0" width="100%" height="208" name="gL3JYnab"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Calculating area for all $$\dfrac{n(n-1)}{2}$$ height pairs.
* Space complexity : $$O(1)$$. Constant extra space is used.
<br />
<br />
---
#### Approach 2: Two Pointer Approach

**Algorithm**

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable $$\text{maxarea}$$ to store the maximum area obtained till now. At every step, we find out the area formed between them, update $$\text{maxarea}$$ and move the pointer pointing to the shorter line towards the other end by one step.

The algorithm can be better understood by looking at the example below:
```
1 8 6 2 5 4 8 3 7
```

<!--![Water_Continer](https://leetcode.com/media/original_images/11_Container_Water.gif)-->
!?!../Documents/11_Container_Water.json:1000,563!?!

How this approach works?

Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.

For further clarification click [here](https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm) and for the proof click [here](https://leetcode.com/problems/container-with-most-water/discuss/6089/Anyone-who-has-a-O(N)-algorithm/7268).

<iframe src="https://leetcode.com/playground/f9MCyxXg/shared" frameBorder="0" width="100%" height="276" name="f9MCyxXg"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Single pass.

* Space complexity : $$O(1)$$. Constant space is used.
