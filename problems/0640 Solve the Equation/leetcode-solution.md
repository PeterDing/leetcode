# 0640 - Solve the Equation

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math | [Leetcode](https://leetcode.com/problems/solve-the-equation) | [solution](https://leetcode.com/problems/solve-the-equation/solution/)


-----------

<p>
Solve a given equation and return the value of <code>x</code> in the form of string "x=#value". The equation contains only '+', '-' operation, the variable <code>x</code> and its coefficient.
</p>

<p>
If there is no solution for the equation, return "No solution".
</p>
<p>
If there are infinite solutions for the equation, return "Infinite solutions".
</p>
<p>
If there is exactly one solution for the equation, we ensure that the value of <code>x</code> is an integer.
</p>

<p><b>Example 1:</b><br/>
<pre>
<b>Input:</b> "x+5-3+x=6+x-2"
<b>Output:</b> "x=2"
</pre>
</p>

<p><b>Example 2:</b><br/>
<pre>
<b>Input:</b> "x=x"
<b>Output:</b> "Infinite solutions"
</pre>
</p>

<p><b>Example 3:</b><br/>
<pre>
<b>Input:</b> "2x=x"
<b>Output:</b> "x=0"
</pre>
</p>

<p><b>Example 4:</b><br/>
<pre>
<b>Input:</b> "2x+3x-6x=x+2"
<b>Output:</b> "x=-1"
</pre>
</p>

<p><b>Example 5:</b><br/>
<pre>
<b>Input:</b> "x=x+2"
<b>Output:</b> "No solution"
</pre>
</p>

-----------


## Similar Problems

- [Medium] [Fraction Addition and Subtraction](fraction-addition-and-subtraction)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Partioning Coefficients [Accepted]

In the current approach, we start by splitting the given $$equation$$ based on `=` sign. This way, we've separated the left and right hand side of this equation. Once this is done, we need to extract the individual elements(i.e. `x`'s and the numbers) from both sides of the equation. To do so, we make use of `breakIt` function, in which we traverse over the given equation(either left hand side or right hand side), and put the separated parts into an array. 

Now, the idea is as follows. We treat the given equation as if we're bringing all the `x`'s on the left hand side and all the rest of the numbers on the right hand side as done below for an example.

`x+5-3+x=6+x-2`

`x+x-x=6-2-5+3`

Thus, every `x` in the left hand side of the given equation is treated as positive, while that on the right hand side is treated as negative, in the current implementation. 

Likewise, every number on the left hand side is treated as negative, while that on the right hand side is treated as positive. Thus, by doing so, we obtain all the `x`'s in the new $$lhs$$ and all the numbers in the new $$rhs$$ of the original equation. 

Further, in case of an `x`, we also need to find its corresponding coefficients in order to evaluate the final effective coefficient of `x` on the left hand side. We also evaluate the final effective number on the right hand side as well.

Now, in case of a unique solution, the ratio of the effective $$rhs$$ and $$lhs$$ gives the required result. In case of infinite solutions, both the effective $$lhs$$ and $$rhs$$ turns out to be zero e.g. `x+1=x+1`. In case of no solution, the coefficient of `x`($$lhs$$) turns out to be zero, but the effective number on the $$rhs$$ is non-zero.


<iframe src="https://leetcode.com/playground/5qsPscf9/shared" frameBorder="0" name="5qsPscf9" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Generating coefficients and findinn $$lhs$$ and $$rhs$$ will take $$O(n)$$.

* Space complexity : $$O(n)$$. ArrayList $$res$$ size can grow upto $$n$$.

---
#### Approach #2 Using regex for spliting [Accepted]

**Algorithm**

In the last approach, we made use of a new function `breakIt` to obtain the individual components of either the left hand side or the right hand side. Instead of doing so, we can also make use of splitting based on `+` or `-` sign, to obtain the individual elements. The rest of the process remains the same as in the last approach. 

In order to do the splitting, we make use of an expression derived from regular expressions(regex). Simply speaking, regex is a functionality used to match a target string based on some given criteria. The ?=n quantifier, in regex, matches any string that is followed by a specific string $$n$$. What it's saying is that the captured match must be followed by $$n$$ but the $$n$$ itself isn't captured.

By making use of this kind of expression in the `split` functionality, we make sure that the partitions are obtained such that the `+` or `-` sign remains along with the parts(numbers or coefficients) even after the splitting.

<iframe src="https://leetcode.com/playground/9JbHjYgz/shared" frameBorder="0" name="9JbHjYgz" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Generating coefficients and finding $$lhs$$ and $$rhs$$ will take $$O(n)$$.

* Space complexity : $$O(n)$$. ArrayList $$res$$ size can grow upto $$n$$.

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
