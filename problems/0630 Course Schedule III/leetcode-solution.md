# 0630 - Course Schedule III

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Greedy | [Leetcode](https://leetcode.com/problems/course-schedule-iii) | [solution](https://leetcode.com/problems/course-schedule-iii/solution/)


-----------

<p>There are <code>n</code> different online courses numbered from <code>1</code> to <code>n</code>. Each course has some duration(course length) <code>t</code> and closed on <code>d<sub>th</sub></code> day. A course should be taken <b>continuously</b> for <code>t</code> days and must be finished before or on the <code>d<sub>th</sub></code> day. You will start at the <code>1<sub>st</sub></code> day.</p>

<p>Given <code>n</code> online courses represented by pairs <code>(t,d)</code>, your task is to find the maximal number of courses that can be taken.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
<b>Output:</b> 3
<b>Explanation:</b> 
There&#39;re totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The integer 1 &lt;= d, t, n &lt;= 10,000.</li>
	<li>You can&#39;t take two courses simultaneously.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Course Schedule](course-schedule)

- [Medium] [Course Schedule II](course-schedule-ii)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

**Algorithm**

The most naive solution will be to consider every possible permutation of the given courses and to try to take as much courses as possible by  taking the courses in a serial order in every permutation. We can find out the maximum number of courses that can be taken from out of values obtained from these permutations.

**Complexity Analysis**

* Time complexity : $$O\big((n+1)!\big)$$. A total of $$n!$$ permutations are possible for the $$courses$$ array of length $$n$$. For every permutation, we scan over the $$n$$ elements of the permutation to find the number of courses that can be taken in each case.

* Space complexity : $$O(n)$$. Each permutation needs $$n$$ space.

---
#### Approach #2 Using Recursion with memoization[Time Limit Exceeded]

**Algorithm**

Before we move on to the better approaches, let's discuss one basic idea to solve the given problem. Suppose, we are considering only two courses $$(a,x)$$ and $$(b,y)$$. Let's assume $$y>x$$. Now, we'll look at the various relative values which $$a$$ and $$b$$ can take, and which course should be taken first in each of these cases. In all the cases, we assume that the course's duration is always lesser than its end day i.e. $$a<x$$ and $$b<y$$.

1. $$(a+b) &le; x$$: In this case, we can take the courses in any order. Both the courses can be taken irrespective of the order in which the courses are taken.

![Courses](../Figures/630/630_Course_Schedule_III_1.PNG)
{align="center"}

2. $$(a+b)>x$$, $$a>b$$, $$(a+b) &leq; y$$: In this case, as is evident from the figure, both the courses can be taken only by taking course $$a$$ before $$b$$.

![Courses](../Figures/630/630_Course_Schedule_III_2.PNG)
{align="center"}

3. $$(a+b)>x$$, $$b>a$$, $$(a+b) &leq; y$$: In this case also, both the courses can be taken only by taking course $$a$$ before $$b$$.

![Courses](../Figures/630/630_Course_Schedule_III_3.PNG)
{align="center"}

4. $$(a+b)>y$$: In this case, irrespective of the order in which we take the courses, only one course can be taken.

![Courses](../Figures/630/630_Course_Schedule_III_4.PNG)
{align="center"}

From the above example, we can conclude that it is always profitable to take the course with a smaller end day prior to a course with a larger end day. This is because, the course with a smaller duration, if can be taken, can surely be taken only if it is taken prior to a course with a larger end day. 

Based on this idea, firstly, we sort the given $$courses$$ array based on their end days. Then, we try to take the courses in a serial order from this sorted $$courses$$ array. 

In order to solve the given problem, we make use of a recursive function `schedule(courses, i, time)` which returns the maximum number of courses that can be taken starting from the $$i^{th}$$ course(starting from 0), given the time aleady consumed by the other courses is $$time$$, i.e. the current time is $$time$$, given a $$courses$$ array as the schedule.

Now, in each function call to `schedule(courses, i, time)`, we try to include the current course in the taken courses. But, this can be done only if $$time + duration_i < end\_day_i$$. Here, $$duration_i$$ refers to the duration of the $$i^{th}$$ course and $$end\_day_i$$ refers to the end day of the $$i^{th}$$ course. 

If the course can be taken, we increment the number of courses taken and obtain the number of courses that can be taken by passing the updated time and courses' index. i.e. we make the function call `schedule(courses, i + 1, time + duration_i)`. Let's say, we store the number of courses that can be taken by taking the current course in $$taken$$ variable.

Further, for every current course, we also leave the current course, and find the number of courses that can be taken thereof. Now, we need not update the time, but we need to update the courses' index. Thus, we make the function call, `schedule(courses, i + 1, time)`. Let's say, we store the count obtained in $$not\_taken$$ variable. 

While returning the number of courses at the end of each function call, we return the maximum value out of $$taken$$ and $$not\_taken$$.

Thus, the function call `schedule(courses, 0, 0)` gives the required result.


In order to remove this redundancy, we make use of a memoization array $$memo$$, such that $$memo[i][j]$$ is used to store the result of the function call `schedule(courses, i, time)`. Thus, whenever the same function call is made again, we can return the result directly from the $$memo$$ array. This helps to prune the search space to a great extent.

<iframe src="https://leetcode.com/playground/JuEBXYU7/shared" frameBorder="0" name="JuEBXYU7" width="100%" height="377"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n*d)$$. $$memo$$ array of size $$n$$x$$d$$ is filled once. Here, $$n$$ refers to the number of courses in the given $$courses$$ array and $$d$$ refers to the maximum value of the end day from all the end days in the $$courses$$ array.

* Space complexity : $$O(n*d)$$. $$memo$$ array of size $$n$$x$$d$$ is used.

---
#### Approach #3  Iterative Solution [Time Limit Exceeded]

For the current approach, the idea goes as follows. As discussed in the previous approaches, we need to sort the given $$courses$$ array based on the end days. Thus, we consider the courses in the ascending order of their end days. We keep a track of the current time in a $$time$$ variable. Along with this, we also keep a track of the number of courses taken till now in $$count$$ variable.

For each course being considered currently(let's say $$i^{th}$$ course), we try to take this course. But, to be able to do so, the current course should end before its corresponding end day i.e. $$time + duration_i &leq; end\day_i$$. Here, $$duration_i$$ refers to the duration of the $$i^{th}$$ course and $$end\_day_i$$ refers to the end day of the $$i^{th}$$ course. 

If this course can be taken, we update the current time to $$time + duration_i$$ and also increment the current $$count$$ value to indicate that one more course has been taken. 

But, if we aren't able to take the current course i.e. $$time + duration_i > end\_day_i$$, we can try to take this course by removing some other course from amongst the courses that have already been taken. But, the current course can fit in by removing some other course, only if the duration of the course($$j^{th}$$) being removed $$duration_j$$ is larger than the current course's duration, $$duration_i$$ i.e. $$duration_j > duration_i$$. 

We are sure of the fact that by removing the $$j^{th}$$ course, we can fit in the current course, because, $$course_j$$ was already fitting in the duration available till now. Since, $$duration_i < duration_j$$, the current course can surely take its place. Thus, we look for a course from amongst the taken courses having a duration larger than the current course.

But why are we doing this replacement? The answer to this question is as follows. By replacing the $$j^{th}$$ course, with the $$i^{th}$$ course of a relatively smaller duration, we can increase the time available for upcoming courses to be taken. An extra $$duration_j - duration_i$$ time can be made available by doing so. 

Now, for this saving in time to be maximum, the course taken for the replacement should be the one with the maximum duration. Thus, from amongst the courses that have been taken till now, we find the course having the maximum duration which should be more than the duration of the current course(which can't be taken). 

Let's say, this course be called as $$max\_i$$. Thus, now, a saving of $$duration_{max\_i} - duration_i$$ can be achived, which could help later in fitting in more courses to be taken.

If such a course, $$max\_i$$, is found, we remove this course from the taken courses and consider the current course as taekn. We also mark this course with $$\text{-1}$$ to indicate that this course has not been taken and should not be considered in the future again for replacement. 

But, if such a course isn't found, we can't take the current course at any cost. Thus, we mark the current course with $$\text{-1}$$ to indicate that the current course has not been taken.

At the end, the value of $$count$$ gives the required result.

The following animation illustrates the process.

!?!../Documents/630_Course_Schedule_III.json:1000,563!?!

<iframe src="https://leetcode.com/playground/HnKoFCWN/shared" frameBorder="0" name="HnKoFCWN" width="100%" height="462"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$.  We iterate over the $$count$$ array of size $$n$$ once. For every element currently considered, we could scan backwards till the first element, giving $$O(n^2)$$ complexity. Sorting the $$count$$ array takes $$O\big(nlog(n)\big)$$ time for $$count$$ array.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
#### Approach #4  Optimized Iterative [Accepted]

In the last approach, we've seen that, in the case of current course which can't be taken direclty, i.e. for $$time + duration_i > end\_day_i$$, we need to traverse back in the $$courses$$ array till the beginning to find a course with the maximum duration which is larger than the current course's duration. This backward traversal also goes through the courses which aren't  taken and thus, can't be replaced, and have been marked as $$\text{-1}$$. 

We can bring in some optimization here. For this, we should search among only those courses which have been taken(and not the ones which haven't been taken). 

To do so, as we iterate over the $$courses$$ array, we also keep on updating it, such that the first $$count$$ number of elements in this array now correspond to only those $$count$$ number of courses which have been taken till now. 

Thus, whenever we update the $$count$$ to indicate that one more course has been taken, we also update the $$courses[count]$$ entry to 
reflect the current course that has just been taken. 

Whenever, we find a course for which $$time + duration_i > end\_day_i$$, we find a $$max_i$$ course from only amongst these first $$count$$ number of courses in the $$courses$$ array, which indicate the courses that have been taken till now. 

Also, instead of marking this $$max_i^{th}$$ course with a $$\text{-1}$$, we can simply replace this course with the current course. Thus, the first $$count$$ courses still reflect the courses that have been taken till now.

<iframe src="https://leetcode.com/playground/v7EjYVQp/shared" frameBorder="0" name="v7EjYVQp" width="100%" height="479"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n*count)$$. We iterate over a total of $$n$$ elements of the $$courses$$ array. For every element, we can traverse backwards upto atmost $$count$$(final value) number of elements.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
#### Approach #5 Using Extra List [Accepted]

**Algorithm**

In the last approach, we updated the $$course$$ array itself so that the first $$count$$ elements indicate the $$count$$ number of courses that have been taken till now. If it is required to retain the $$courses$$ array as such, we can do the same job by maintaining a separate list $$valid\_list$$ which is the list of those courses that have been taken till now. 

Thus, to find the $$max_i$$ course, we need to search in this list only. Further, when replacing this $$max_i^{th}$$ course with the current course, we can replace this $$max_i$$ course in the list with current course directly. The rest of the method remains the same as the last approach.


<iframe src="https://leetcode.com/playground/esu9eSya/shared" frameBorder="0" name="esu9eSya" width="100%" height="479"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n*m)$$. We iterate over a total of $$n$$ elements of the $$courses$$ array. For every element, we can traverse over atmost $$m$$ number of elements. Here, $$m$$ refers to the final length of the $$valid\_list$$.

* Space complexity : $$O(n)$$. The $$valid\_list$$ can contain atmost $$n$$ courses.

---
#### Approach #6 Using Priority Queue [Accepted]

**Algorithm**

This approach is inspired by [@stomach_ache](http://leetcode.com/stomach_ache)

In the last few approaches, we've seen that we needed to traverse over the courses which have been taken to find the course(with the maximum duration) which can be replaced by the current course(if it can't be taken directly). These traversals can be saved, if we make use of a Priority Queue, $$queue$$(which is implemented as a Max-Heap) which contains the durations of all the courses that have been taken till now. 

The iteration over the sorted $$courses$$ remains the same as in the last approaches. Whenver the current course($$i^{th}$$ course) can be taken($$time + duration_i &leq; end\_day_i$$), it is added to the $$queue$$ and the value of the current time is updated to $$time + duration_i$$. 

If the current course can't be taken directly, as in the previous appraoches, we need to find a course whose duration $$duration_j$$ is maximum from amongst the courses taken till now. Now, since we are maintaing a Max-Heap, $$queue$$, we can obtain this duration directly from this $$queue$$. If the duration $$duration_j > duration_i$$, we can replace the $$j^{th}$$ course, with the current one. 

Thus, we remove the $$duration_j$$ from the $$queue$$ and add the current course's duration $$duration_i$$ to the $$queue$$. We also need to make proper adjustments to the $$time$$ to account for this replacement done.

At the end, the number of elements in the $$queue$$ represent the number of courses that have been taken till now.


<iframe src="https://leetcode.com/playground/AaRNrEU7/shared" frameBorder="0" name="AaRNrEU7" width="100%" height="343"></iframe>
**Complexity Analysis**

* Time complexity : $$O\big(nlog(n)\big)$$. At most $$n$$ elements are added to the $$queue$$. Adding each element is followed by heapification, which takes $$O\big(log(n)\big)$$ time.

* Space complexity : $$O(n)$$. The $$queue$$ containing the durations of the  courses taken can have atmost $$n$$ elements

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
