# 0472 - Concatenated Words

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Depth-first Search, Trie | [Leetcode](https://leetcode.com/problems/concatenated-words/description/) |


-----------

```
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".



Note:

The number of elements of the given array will not exceed 10,000 
The length sum of elements in the given array will not exceed 600,000. 
All the input string will only include lower case letters.
The returned elements order does not matter.
```

-----------

## Thought:
