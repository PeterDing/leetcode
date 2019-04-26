# 0557 - Reverse Words in a String III

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/reverse-words-in-a-string-iii) | [solution](https://leetcode.com/problems/reverse-words-in-a-string-iii/solution/)


-----------

<p>Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "Let's take LeetCode contest"
<b>Output:</b> "s'teL ekat edoCteeL tsetnoc"
</pre>
</p>

<p><b>Note:</b>
In the string, each word is separated by single space and there will not be any extra space in the string.
</p>

-----------


## Similar Problems

- [Easy] [Reverse String II](reverse-string-ii)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Simple Solution[Accepted]

The first method is really simple. We simply split up the given string based on whitespaces and put the individual words in an array of strings. Then, we reverse each individual string and concatenate the result. We return the result after removing the additional whitespaces at the end.


<iframe src="https://leetcode.com/playground/DjRyo9vA/shared" frameBorder="0" name="DjRyo9vA" width="100%" height="207"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. where $$n$$ is the length of the string.

* Space complexity : $$O(n)$$. $$res$$ of size $$n$$ is used.

---
#### Approach #2 Without using pre-defined split and reverse function [Accepted]

**Algorithm**

We can create our own split and reverse function. Split function splits the string based on the delimiter " "(space) and returns the array of words. Reverse function returns the string after reversing the characters.



<iframe src="https://leetcode.com/playground/oxasWgHd/shared" frameBorder="0" name="oxasWgHd" width="100%" height="515"></iframe>
**Complexity Analysis**

* Time complexity : $$O(n)$$. where $$n$$ is the length of the string.
* Space complexity : $$O(n)$$. $$res$$ of size $$n$$ is used.

---
#### Approach #3 Using StringBuilder and reverse method [Accepted]

**Algorithm**

Instead of using split method, we can use temporary string $$word$$ to store the word. We simply append the characters to the $$word$$ until `' '` character is not found. On getting `' '` we append the reverse of the $$word$$ to the resultant string $$result$$. Also after completion of loop , we still have to append the $$reverse$$ of the $$word$$(last word) to the $$result$$ string. 

Below code is inspired by [@ApolloX](http://leetcode.com/apolloX).


<iframe src="https://leetcode.com/playground/Xt8eMTKv/shared" frameBorder="0" name="Xt8eMTKv" width="100%" height="343"></iframe>
**Complexity Analysis**

* Time complexity : $$O(n)$$. Single loop upto $$n$$ is there, where $$n$$ is the length of the string.
* Space complexity : $$O(n)$$. $$result$$ and $$word$$ size will grow upto $$n$$.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
