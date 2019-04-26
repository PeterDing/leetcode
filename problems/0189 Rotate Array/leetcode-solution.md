# 0189 - Rotate Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/rotate-array) | [solution](https://leetcode.com/problems/rotate-array/solution/)


-----------

<p>Given an array, rotate the array to the right by <em>k</em> steps, where&nbsp;<em>k</em>&nbsp;is non-negative.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[1,2,3,4,5,6,7]</code> and <em>k</em> = 3
<strong>Output:</strong> <code>[5,6,7,1,2,3,4]</code>
<strong>Explanation:</strong>
rotate 1 steps to the right: <code>[7,1,2,3,4,5,6]</code>
rotate 2 steps to the right: <code>[6,7,1,2,3,4,5]
</code>rotate 3 steps to the right: <code>[5,6,7,1,2,3,4]</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[-1,-100,3,99]</code> and <em>k</em> = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.</li>
	<li>Could you do it in-place with O(1) extra space?</li>
</ul>

-----------


## Similar Problems

- [Medium] [Rotate List](rotate-list)

- [Medium] [Reverse Words in a String II](reverse-words-in-a-string-ii)




## Solution:

[TOC]

## Summary

We have to rotate the elements of the given array k times to the right.

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

The simplest approach is to rotate all the elements of the array in k steps
 by rotating the elements by 1 unit in each step.

**Java**

```java
public class Solution {
    public void rotate(int[] nums, int k) {
        int temp, previous;
        for (int i = 0; i < k; i++) {
            previous = nums[nums.length - 1];
            for (int j = 0; j < nums.length; j++) {
                temp = nums[j];
                nums[j] = previous;
                previous = temp;
            }
        }
    }
}
```

**Complexity Analysis**

* Time complexity : $$O(n*k)$$. All the numbers are shifted by one step($$O(n)$$)
 k times($$O(k)$$).
* Space complexity : $$O(1)$$. No extra space is used.

---
#### Approach #2 Using Extra Array [Accepted]

**Algorithm**

We use an extra array in which we place every element of the array at its correct
position i.e. the number at index $$i$$ in the original array is placed at the
index $$(i+k)%(length of array)$$. Then, we copy the new array to the original one.


**Java**
```java
public class Solution {
    public void rotate(int[] nums, int k) {
        int[] a = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            a[(i + k) % nums.length] = nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = a[i];
        }
    }
}
```

**Complexity Analysis**

* Time complexity : $$O(n)$$. One pass is used to put the numbers in the new array.
 And another pass to copy the new array to the original one.

* Space complexity : $$O(n)$$. Another array of the same size is used.

---
#### Approach #3 Using Cyclic Replacements [Accepted]

**Algorithm**

We can directly place every number of the array at its required correct position.
But if we do that, we will destroy the original element. Thus, we need to store
the number being replaced in a $$temp$$ variable. Then, we can place the replaced
 number($$temp$$) at its correct position and so on, $$n$$ times, where $$n$$ is
 the length of array. We have chosen $$n$$ to be the number of replacements since we have 
 to shift all the elements of the array(which is $$n$$). But, there could be a problem with this method, if $$n%k=0$$
 where $$k = k%n$$(since a value of $$k$$ larger than $$n$$ eventually leads to a $$k$$ equivalent to $$k%n$$). In this case, while picking up numbers to be placed at the
 correct position, we will eventually reach the number from which we originally started. Thus, in such a case, when
 we hit the original number's index again, we start the same process with the number following it.
 
Now let's look at the proof of how the above method works. Suppose, we have $$n$$ as the number of elements in the array and
 $$k$$ is the number of shifts required. Further, assume $$n%k=0$$. Now, when we start placing the elements at their correct position, in the first cycle all the numbers with their index $$i$$ satisfying $$i%k=0$$ get placed at their required position. This happens because when we jump k steps every time, we will only hit the numbers k steps apart. We start with index $$i=0$$, having $$i%k=0$$. Thus, we hit all the numbers satisfying the above condition in the first cycle. When we reach back the original index, we have placed $$\frac{n}{k}$$ elements at their correct position, since we hit only that many elements in the first cycle. Now, we increment the index for replacing the numbers. This time, we place other $$\frac{n}{k}$$ elements at their correct position, different from the ones placed correctly in the first cycle, because this time we hit all the numbers satisfy the condition $$i%k=1$$. When we hit the starting number again, we increment the index and repeat the same process from $$i=1$$ for all the indices satisfying $$i%k==1$$. This happens till we reach the number with the index $$i%k=0$$ again, which occurs for $$i=k$$. We will reach such a number after a total of k cycles. Now, the total count of numbers exclusive numbers placed at their correct position will be $$k \times \frac{n}{k}=n$$. Thus, all the numbers will be placed at their correct position.

 Look at the following example to clarify the process:
 ```
nums: [1, 2, 3, 4, 5, 6]
k: 2
 ```

   ![Rotate Array](https://leetcode.com/media/original_images/189_Rotate_Array.png)



**java**
```java
public class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int count = 0;
        for (int start = 0; count < nums.length; start++) {
            int current = start;
            int prev = nums[start];
            do {
                int next = (current + k) % nums.length;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                current = next;
                count++;
            } while (start != current);
        }
    }
}
```
**Complexity Analysis**

* Time complexity : $$O(n)$$. Only one pass is used.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
#### Approach #4 Using Reverse [Accepted]

**Algorithm**

This approach is based on the fact that when we rotate the array k times, $$k%n$$ elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest $$n-k$$ elements gives us the required result.

Let $$n=7$$ and $$k=3$$.
```
Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
```


**java**
```java
public class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
```

**Complexity Analysis**

* Time complexity : $$O(n)$$. $$n$$ elements are reversed a total of three times.

* Space complexity : $$O(1)$$. No extra space is used.

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
