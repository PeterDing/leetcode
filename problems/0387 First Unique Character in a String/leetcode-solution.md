# 0387 - First Unique Character in a String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table, String | [Leetcode](https://leetcode.com/problems/first-unique-character-in-a-string) | [solution](https://leetcode.com/problems/first-unique-character-in-a-string/solution/)


-----------

<p>
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
</p>
<p><b>Examples:</b>
<pre>
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
</pre>
</p>

<p>
<b>Note:</b> You may assume the string contain only lowercase letters.
</p>

-----------


## Similar Problems

- [Medium] [Sort Characters By Frequency](sort-characters-by-frequency)




## Solution:

[TOC]

## Solution

---

#### Approach 1: Linear time solution

The best possible solution here could be of a linear time 
because to ensure 
that the character is unique 
you have to check the whole string anyway. 

The idea is to go through the string and 
save in a hash map the number of times 
each character appears in the string. 
That would take $$\mathcal{O}(N)$$ time, 
where `N` is a number of characters in the string.
 
And then we go through the string the second time, this time 
we use the hash map as a reference to check if a character 
is unique or not.   
If the character is unique, one could just return its index. 
The complexity of the second iteration is $$\mathcal{O}(N)$$ as well.

<!--![LIS](../Figures/387/387_tr.gif)-->
!?!../Documents/387_LIS.json:1000,621!?!

<iframe src="https://leetcode.com/playground/LJEcGz4C/shared" frameBorder="0" width="100%" height="361" name="LJEcGz4C"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ since we go 
through the string of length `N` two times. 
* Space complexity : $$\mathcal{O}(N)$$ since we have to keep a hash map 
with `N` elements.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
