# 0544 - Output Contest Matches

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/output-contest-matches/description/) |


-----------

```
During the NBA playoffs, we always arrange the rather strong team to play with
the rather weak team, like make the rank 1 team play with the rank nth team,
which is a good strategy to make the contest more interesting. Now, you're
given n teams, you need to output their final contest matches in the form of a
string.

The n teams are given in the form of positive integers from 1 to n, which
represents their initial rank. (Rank 1 is the strongest team and Rank n is the
weakest team.) We'll use parentheses('(', ')') and commas(',') to represent
the contest team pairing - parentheses('(' , ')') for pairing and commas(',')
for partition. During the pairing process in each round, you always need to
follow the strategy of making the rather strong one pair with the rather weak
one.

Example 1:



    Input: 2



Example 2:



    Input: 4



Example 3:



    Input: 8



Note:

  1. The n is in range [2, 212].
  2. We ensure that the input n can be converted into the form 2k, where k is a positive integer.
```

-----------

## Thought: