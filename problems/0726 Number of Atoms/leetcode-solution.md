# 0726 - Number of Atoms

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Hash Table, Stack, Recursion | [Leetcode](https://leetcode.com/problems/number-of-atoms) | [solution](https://leetcode.com/problems/number-of-atoms/solution/)


-----------

<p>Given a chemical <code>formula</code> (given as a string), return the count of each atom.
</p><p>
An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
</p><p>
1 or more digits representing the count of that element may follow if the count is greater than 1.  If the count is 1, no digits will follow.  For example, H2O and H2O2 are possible, but H1O2 is impossible.
</p><p>
Two formulas concatenated together produce another formula.  For example, H2O2He3Mg4 is also a formula.  
</p><p>
A formula placed in parentheses, and a count (optionally added) is also a formula.  For example, (H2O2) and (H2O2)3 are formulas.
</p><p>
Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
formula = "H2O"
<b>Output:</b> "H2O"
<b>Explanation:</b> 
The count of elements are {'H': 2, 'O': 1}.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
formula = "Mg(OH)2"
<b>Output:</b> "H2MgO2"
<b>Explanation:</b> 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> 
formula = "K4(ON(SO3)2)2"
<b>Output:</b> "K4N2O14S4"
<b>Explanation:</b> 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
</pre>
</p>

<p><b>Note:</b>
<li>All atom names consist of lowercase letters, except for the first character which is uppercase.</li>
<li>The length of <code>formula</code> will be in the range <code>[1, 1000]</code>.</li>
<li><code>formula</code> will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.</li>
</p>

-----------


## Similar Problems

- [Medium] [Decode String](decode-string)

- [Hard] [Encode String with Shortest Length](encode-string-with-shortest-length)

- [Hard] [Parse Lisp Expression](parse-lisp-expression)




## Solution:

[TOC]

#### Approach #1: Recursion [Accepted]

**Intuition and Algorithm**

Write a function `parse` that parses the formula from index `i`, returning a map `count` from names to multiplicities (the number of times that name is recorded).

We will put `i` in global state: our `parse` function increments `i` throughout any future calls to `parse`.

* When we see a `'('`, we will parse whatever is inside the brackets (up to the closing ending bracket) and add it to our count.

* Otherwise, we should see an uppercase character: we will parse the rest of the letters to get the name, and add that (plus the multiplicity if there is one.)

* At the end, if there is a final multiplicity (representing the multiplicity of a bracketed sequence), we'll multiply our answer by this.

<iframe src="https://leetcode.com/playground/pdZAZ5dG/shared" frameBorder="0" width="100%" height="500" name="pdZAZ5dG"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the length of the formula.  It is $$O(N)$$ to parse through the formula, but each of $$O(N)$$ multiplicities after a bracket may increment the count of each name in the formula (inside those brackets), leading to an $$O(N^2)$$ complexity.

* Space Complexity: $$O(N)$$.  We aren't recording more intermediate information than what is contained in the formula.

---
#### Approach #2: Stack [Accepted]

**Intuition and Algorithm**

Instead of recursion, we can simulate the call stack by using a stack of `count`s directly.

<iframe src="https://leetcode.com/playground/KLEWBfKw/shared" frameBorder="0" width="100%" height="500" name="KLEWBfKw"></iframe>

**Complexity Analysis**

* Time Complexity $$O(N^2)$$, and Space Complexity $$O(N)$$.  The analysis is the same as *Approach #1*.

---
#### Approach #3: Regular Expressions [Accepted]

**Intuition and Algorithm**

Whenever parsing is involved, we can use *regular expressions*, a language for defining patterns in text.

Our regular expression will be `"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)"`.  Breaking this down by *capture group*, this is:

* `([A-Z][a-z]*)` Match an uppercase character followed by any number of lowercase characters, then (`(\d*)`) match any number of digits.
* OR, `(\()` match a left bracket or `(\))` right bracket, then `(\d*)` match any number of digits.

Now we can proceed as in *Approach #2*.

* If we parsed a name and multiplicity `([A-Z][a-z]*)(\d*)`, we will add it to our current count.

* If we parsed a left bracket, we will append a new `count` to our stack, representing the nested depth of parentheses.

* If we parsed a right bracket (and possibly another multiplicity), we will multiply our deepest level `count`, `top = stack.pop()`, and add those entries to our current count.

<iframe src="https://leetcode.com/playground/rnaR7xpb/shared" frameBorder="0" width="100%" height="500" name="rnaR7xpb"></iframe>

**Complexity Analysis**

* Time Complexity $$O(N^2)$$, and Space Complexity $$O(N)$$.  The analysis is the same as *Approach #1*, as this regular expression did not look backwards when parsing.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Approaches #1 and #2 inspired by [@zestypanda](https://leetcode.com/zestypanda/).  Java solution for #3 by [@jianchao.li.fighter](https://discuss.leetcode.com/user/jianchao-li-fighter).
