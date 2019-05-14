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




## Thought:

This problem can be converted to the problem in which all elements of an array form a triangle mountain where all element are local tips. We only need to solve the same problem with the triangle.

1. Find the tiangle mountain O(n)

   ```python
   def remove(r):
       if len(r) < 3:
           return
       a = r.pop()
       b = r.pop()
       c = r.pop()
       if c > b and b < a:
           r.append(c)
           r.append(a)
           return remove(r)
       else:
           r.append(c)
           r.append(b)
           r.append(a)
           return
   
   
   def find_mountain(array):
       r = []
       for i, e in enumerate(array):
           r.append(e)
           remove(r)
       return r
   
   # r is the triangle mountain
   ```

2. Find the two elements which have maximum area.

   ```python
   # code is easy
   def max_area(r):
       rs = 0
       N = len(r)
       for i, e in enumerate(r):
           if i == N - 1 or r[i] > e:
               return rs
           else:
               for ii, j in enumerate(r[i + 1:]):
                   if e >= j or ii + i == N - 1:
                       m = min(e, j)
                       m = m * m * (ii)
                       rs = max(rs, m)
       return rs
   ```

