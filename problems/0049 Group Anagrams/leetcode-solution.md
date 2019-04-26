# 0049 - Group Anagrams

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, String | [Leetcode](https://leetcode.com/problems/group-anagrams) | [solution](https://leetcode.com/problems/group-anagrams/solution/)


-----------

<p>Given an array of strings, group anagrams together.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>[&quot;eat&quot;, &quot;tea&quot;, &quot;tan&quot;, &quot;ate&quot;, &quot;nat&quot;, &quot;bat&quot;]</code>,
<strong>Output:</strong>
[
  [&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;],
  [&quot;nat&quot;,&quot;tan&quot;],
  [&quot;bat&quot;]
]</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All inputs will be in lowercase.</li>
	<li>The order of your output does not&nbsp;matter.</li>
</ul>


-----------


## Similar Problems

- [Easy] [Valid Anagram](valid-anagram)

- [Medium] [Group Shifted Strings](group-shifted-strings)




## Solution:

[TOC]

#### Approach 1: Categorize by Sorted String

**Intuition**

Two strings are anagrams if and only if their sorted strings are equal.

**Algorithm**

Maintain a map `ans : {String -> List}` where each key $$\text{K}$$ is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to $$\text{K}$$.

In Java, we will store the key as a string, eg. `code`.  In Python, we will store the key as a hashable tuple, eg. `('c', 'o', 'd', 'e')`.

![Anagrams](../Figures/49_groupanagrams1.png)

<iframe src="https://leetcode.com/playground/HwiBG7Pz/shared" frameBorder="0" width="100%" height="293" name="HwiBG7Pz"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NK \log K)$$, where $$N$$ is the length of `strs`, and $$K$$ is the maximum length of a string in `strs`.  The outer loop has complexity $$O(N)$$ as we iterate through each string.  Then, we sort each string in $$O(K \log K)$$ time.

* Space Complexity: $$O(NK)$$, the total information content stored in `ans`.
<br />
<br />
---
#### Approach 2: Categorize by Count

**Intuition**

Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.

**Algorithm**

We can transform each string $$\text{s}$$ into a character count, $$\text{count}$$, consisting of 26 non-negative integers representing the number of $$\text{a}$$'s, $$\text{b}$$'s, $$\text{c}$$'s, etc.  We use these counts as the basis for our hash map.

In Java, the hashable representation of our count will be a string delimited with '**#**' characters.  For example, `abbccc` will be `#1#2#3#0#0#0...#0` where there are 26 entries total.  In python, the representation will be a tuple of the counts.  For example, `abbccc` will be `(1, 2, 3, 0, 0, ..., 0)`, where again there are 26 entries total.

![Anagrams](../Figures/49_groupanagrams2.png)

<iframe src="https://leetcode.com/playground/DvDMzZTX/shared" frameBorder="0" width="100%" height="412" name="DvDMzZTX"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NK)$$, where $$N$$ is the length of `strs`, and $$K$$ is the maximum length of a string in `strs`.  Counting each string is linear in the size of the string, and we count every string.

* Space Complexity: $$O(NK)$$, the total information content stored in `ans`.
