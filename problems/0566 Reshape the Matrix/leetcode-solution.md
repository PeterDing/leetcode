# 0566 - Reshape the Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/reshape-the-matrix) | [solution](https://leetcode.com/problems/reshape-the-matrix/solution/)


-----------

<p>In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
</p>

<p>
You're given a matrix represented by a two-dimensional array, and two <b>positive</b> integers <b>r</b> and <b>c</b> representing the <b>row</b> number and <b>column</b> number of the wanted reshaped matrix, respectively.</p>

 <p>The reshaped matrix need to be filled with all the elements of the original matrix in the same <b>row-traversing</b> order as they were.
</p>

<p>
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
<b>Output:</b> 
[[1,2,3,4]]
<b>Explanation:</b><br>The <b>row-traversing</b> of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
<b>Output:</b> 
[[1,2],
 [3,4]]
<b>Explanation:</b><br>There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The height and width of the given matrix is in range [1, 100].</li>
<li>The given r and c are all positive.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1 Using queue [Accepted]

**Algorithm**

The simplest method is to extract all the elements of the given matrix by reading the elements in a row-wise fashion. In this implementation, we use a queue to put the extracted elements. Then, we can take out the elements of the queue formed in a serial order and arrange the elements in the resultant required matrix in a row-by-row order again.

The formation of the resultant matrix won't be possible if the number of elements in the original matrix isn't equal to the number of elements in the resultant matrix.

<iframe src="https://leetcode.com/playground/QiYrHtjz/shared" frameBorder="0" name="QiYrHtjz" width="100%" height="428"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m*n)$$. We traverse over $$m*n$$ elements twice. Here, $$m$$ and $$n$$ refer to the number of rows and columns of the given matrix respectively.

* Space complexity : $$O(m*n)$$. The queue formed will be of size $$m*n$$.

---
#### Approach #2 Without using extra Space [Accepted]

**Algorithm**

Instead of unnecessarily using the queue as in the brute force approach, we can keep putting the numbers in the resultant matrix directly while iterating over the given matrix in a row-by-row order. While putting the numbers in the resultant array, we fix a particular row and keep on incrementing the column numbers only till we reach the end of the required columns indicated by $$c$$. At this moment, we update the row index by incrementing it and reset the column index to start from 0 again. Thus, we can save the space consumed by the queue for storing the data that just needs to be copied into a new array.

<iframe src="https://leetcode.com/playground/JvBHJ8mJ/shared" frameBorder="0" name="JvBHJ8mJ" width="100%" height="394"></iframe>

**Complexity Analysis**

* Time complexity : $$O(m*n)$$. We traverse the entire matrix of size $$m*n$$ once only. Here, $$m$$ and $$n$$ refers to the number of rows and columns in the given matrix.

* Space complexity : $$O(m*n)$$. The resultant matrix of size $$m*n$$ is used. 

---

#### Approach #3  Using division and modulus [Accepted]

**Algorithm**

In the last approach, we needed to keep a track of when we reached the end of columns for the resultant matrix and needed to update the current row and column number for putting the extracted elements by checking the current indices every time. Instead of doing these limit checks at every step, we can make use of maths to help ease the situation. 

The idea behind this approach is as follows. Do you know how a 2-D array is stored in the main memory(which is 1-D  in nature)? It is internally represented as a 1-D array only. The element $$nums[i][j]$$ of $$nums$$ array is represented in the form of a one dimensional array by using the index in the form: $$nums[n*i + j]$$, where $$m$$ is the number of columns in the given matrix. Looking at the same in the reverse order, while putting the elements in the elements in the resultant matrix, we can make use of a $$count$$ variable which gets incremented for every element traversed as if we are putting the elements in a 1-D resultant array. But, to convert the $$count$$ back into 2-D matrix indices with a column count of $$c$$, we can obtain the indices as $$res[count/c][count\%c]$$ where $$count/c$$ is the row number and $$count\%c$$ is the coloumn number. Thus, we can save the extra checking required at each step.

<iframe src="https://leetcode.com/playground/3U3C5txm/shared" frameBorder="0" name="3U3C5txm" width="100%" height="309"></iframe>
**Complexity Analysis**

* Time complexity : $$O(m*n)$$. We traverse the entire matrix of size $$m*n$$ once only. Here, $$m$$ and $$n$$ refers to the number of rows and columns in the given matrix.

* Space complexity : $$O(m*n)$$. The resultant matrix of size $$m*n$$ is used. 

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
