# 0042 - Trapping Rain Water

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Two Pointers, Stack | [Leetcode](https://leetcode.com/problems/trapping-rain-water) | [solution](https://leetcode.com/problems/trapping-rain-water/solution/)


-----------

<p>Given <em>n</em> non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" /><br />
<small>The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. <strong>Thanks Marcos</strong> for contributing this image!</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6</pre>


-----------


## Similar Problems

- [Medium] [Container With Most Water](container-with-most-water)

- [Medium] [Product of Array Except Self](product-of-array-except-self)

- [Hard] [Trapping Rain Water II](trapping-rain-water-ii)

- [Medium] [Pour Water](pour-water)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Brute force

**Intuition**

Do as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both the sides minus its own height.

**Algorithm**

* Initialize $$ans=0$$
* Iterate the array from left to right:
  + Initialize $$\text{max\_left}=0$$ and $$\text{max\_right}=0$$
  + Iterate from the current element to the beginning of array updating:
    * $$\text{max\_left}=\max(\text{max\_left},\text{height}[j])$$
  + Iterate from the current element to the end of array updating:
    * $$\text{max\_right}=\max(\text{max\_right},\text{height}[j])$$
  + Add $$\min(\text{max\_left},\text{max\_right}) - \text{height}[i]$$ to $$\text{ans}$$

<iframe src="https://leetcode.com/playground/bY2tPbcU/shared" frameBorder="0" width="100%" height="327" name="bY2tPbcU"></iframe>

**Complexity Analysis**

* Time complexity: $$O(n^2)$$. For each element of array, we iterate the left and right parts.

* Space complexity: $$O(1)$$ extra space.
<br />
<br />
---
#### Approach 2: Dynamic Programming

**Intuition**

In brute force, we iterate over the left and right parts again and again just to find the highest bar size upto that index. But, this could be stored. Voila, dynamic programming.

The concept is illustrated as shown:

![Dynamic programming](../Figures/42/trapping_rain_water.png){:width="500px"}
{:align="center"}

**Algorithm**

* Find maximum height of bar from the left end upto an index i in the array $$\text{left\_max}$$.
* Find maximum height of bar from the right end upto an index i in the array $$\text{right\_max}$$.
* Iterate over the $$\text{height}$$ array and update ans:
	+ Add $$\min(\text{max\_left}[i],\text{max\_right}[i]) - \text{height}[i]$$ to $$ans$$

<iframe src="https://leetcode.com/playground/uHswDycP/shared" frameBorder="0" width="100%" height="395" name="uHswDycP"></iframe>

**Complexity analysis**

* Time complexity: $$O(n)$$.
	+ We store the maximum heights upto a point using 2 iterations of $$O(n)$$ each.
	+ We finally update $$\text{ans}$$ using the stored values in $$O(n)$$.

* Space complexity: $$O(n)$$ extra space.
	+ Additional $$O(n)$$ space for $$\text{left\_max}$$ and $$\text{right\_max}$$ arrays than in [Approach 1](#approach-1-brute-force).
<br />
<br />
---
#### Approach 3: Using stacks

**Intuition**

Instead of storing the largest bar upto an index as in [Approach 2](#approach-2-dynamic-programming), we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water. Using the stack, we can do the calculations in only one iteration.

We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to $$\text{ans}$$.

**Algorithm**

* Use stack to store the indices of the bars.
* Iterate the array:
	+ While stack is not empty and $$\text{height}[current]>\text{height}[st.top()]$$
		* It means that the stack element can be popped. Pop the top element as $$\text{top}$$.
		* Find the distance between the current element and the element at top of stack, which is to be filled.
		$$\text{distance} = \text{current} - \text{st.top}() - 1$$
		* Find the bounded height
		$$\text{bounded\_height} = \min(\text{height[current]}, \text{height[st.top()]}) - \text{height[top]}$$
		* Add resulting trapped water to answer $$\text{ans} \mathrel{+}= \text{distance} \times \text{bounded\_height}$$
	+ Push current index to top of the stack
	+ Move $$\text{current}$$ to the next position


<iframe src="https://leetcode.com/playground/Xp6PoVhM/shared" frameBorder="0" width="100%" height="361" name="Xp6PoVhM"></iframe>

**Complexity analysis**

* Time complexity: $$O(n)$$.
	+ Single iteration of $$O(n)$$ in which each bar can be touched at most twice(due to  insertion and deletion from stack) and insertion and deletion from stack takes $$O(1)$$ time.
* Space complexity: $$O(n)$$. Stack can take upto $$O(n)$$ space in case of stairs-like or flat structure.
<br />
<br />
---
#### Approach 4: Using 2 pointers

**Intuition**

As in [Approach 2](#approach-2-dynamic-programming), instead of computing the left and right parts seperately, we may think of some way to do it in one iteration.
From the figure in dynamic programming approach, notice that as long as $$\text{right\_max}[i]>\text{left\_max}[i]$$ (from element 0 to 6), the water trapped depends upon the left_max, and similar is the case when $$\text{left\_max}[i]>\text{right\_max}[i]$$ (from element 8 to 11).
So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
We must maintain $$\text{left\_max}$$ and $$\text{right\_max}$$ during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

**Algorithm**

* Initialize $$\text{left}$$ pointer to 0 and $$\text{right}$$ pointer to size-1
* While $$\text{left}< \text{right}$$, do:
	+ If $$\text{height[left]}$$ is smaller than $$\text{height[right]}$$
		* If $$\text{height[left]} \geq \text{left\_max}$$, update $$\text{left\_max}$$
		* Else add $$\text{left\_max}-\text{height[left]}$$ to $$\text{ans}$$
		* Add 1 to $$\text{left}$$.
	+ Else
		* If $$\text{height[right]} \geq \text{right\_max}$$, update $$\text{right\_max}$$
		* Else add $$\text{right\_max}-\text{height[right]}$$ to $$\text{ans}$$
		* Subtract 1 from $$\text{right}$$.

Refer the example for better understanding:
!?!../Documents/42/42_trapping_rain_water.json:1000,662!?!

<iframe src="https://leetcode.com/playground/Nnks5xkT/shared" frameBorder="0" width="100%" height="344" name="Nnks5xkT"></iframe>

**Complexity analysis**

* Time complexity: $$O(n)$$. Single iteration of $$O(n)$$.
* Space complexity: $$O(1)$$ extra space. Only constant space required for $$\text{left}$$, $$\text{right}$$, $$\text{left\_max}$$ and $$\text{right\_max}$$.
