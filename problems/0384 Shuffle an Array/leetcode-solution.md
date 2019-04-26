# 0384 - Shuffle an Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/shuffle-an-array) | [solution](https://leetcode.com/problems/shuffle-an-array/solution/)


-----------

<p>Shuffle a set of numbers without duplicates.
</p>

<p><b>Example:</b>
<pre>
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
</pre>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

#### Initial Thoughts

Normally I would display more than two approaches, but shuffling is
deceptively easy to do _almost_ properly, and the Fisher-Yates algorithm is
both the canonical solution and asymptotically optimal.

A few notes on randomness are necessary before beginning - both approaches
displayed below assume that the languages' pseudorandom number generators
(PRNGs) are sufficiently random. The sample code uses the simplest techniques
available for getting pseudorandom numbers, but for each possible permutation
of the array to be truly equally likely, more care must be taken. For
example, an array of length $$n$$ has $$n!$$ distinct permutations. Therefore, in
order to encode all permutations in an integer space, $$\lceil lg(n!)\rceil$$
bits are necessary, which may not be guaranteed by the default PRNG.

#### Approach #1 Brute Force [Accepted]

**Intuition**

If we put each number in a "hat" and draw them out at random, the order in
which we draw them will define a random ordering.

**Algorithm**

The brute force algorithm essentially puts each number in the aforementioned
"hat", and draws them at random (without replacement) until there are none
left. Mechanically, this is performed by copying the contents of `array` into
a second auxiliary array named `aux` before overwriting each element of
`array` with a randomly selected one from `aux`. After selecting each random
element, it is removed from `aux` to prevent duplicate draws. The
implementation of `reset` is simple, as we just store the original state of
`nums` on construction.

The correctness of the algorithm follows from the fact that an element
(without loss of generality) is equally likely to be selected during all
iterations of the `for` loop. To prove this, observe that the probability of a
particular element $$e$$ being chosen on the $$k$$th iteration (indexed from 0)
is simply $$P(e$$ being chosen during the $$k$$th iteration$$)\cdot P(e$$ not being
chosen before the $$k$$th iteration$$)$$. Given that the array to be shuffled has
$$n$$ elements, this probability is more concretely stated as the following:

$$
   \frac{1}{n-k} \cdot \prod_{i=1}^{k} \frac{n-i}{n-i+1}
$$

When expanded (and rearranged), it looks like this (for sufficiently large
$$k$$):

$$
   (\frac{n-1}{n}
   \cdot \frac{n-2}{n-1}
   \cdot (\ldots)
   \cdot \frac{n-k+1}{n-k+2}
   \cdot \frac{n-k}{n-k+1})
   \cdot \frac{1}{n-k}
$$

For the base case ($$k = 0$$), it is trivial to see that
$$\frac{1}{n-k} = \frac{1}{n}$$. For $$k > 0$$, the numerator of each fraction
can be cancelled with the denominator of the next, leaving the $$n$$ from the
0th draw as the only uncancelled denominator. Therefore, no matter on which
draw an element is drawn, it is drawn with a $$\frac{1}{n}$$ chance, so each
array permutation is equally likely to arise.

<iframe src="https://leetcode.com/playground/FWMsaXQ7/shared" frameBorder="0" width="100%" height="500" name="FWMsaXQ7"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$

    The quadratic time complexity arises from the calls to `list.remove` (or
    `list.pop`), which run in linear time. $$n$$ linear list removals occur,
    which results in a fairly easy quadratic analysis.

* Space complexity : $$O(n)$$

    Because the problem also asks us to implement `reset`, we must use linear
    additional space to store the original array. Otherwise, it would be lost
    upon the first call to `shuffle`.

---

#### Approach #2 Fisher-Yates Algorithm [Accepted]

**Intuition**

We can cut down the time and space complexities of `shuffle` with a bit of
cleverness - namely, by swapping elements around within the array itself, we
can avoid the linear space cost of the auxiliary array and the linear time
cost of list modification.

**Algorithm**

The Fisher-Yates algorithm is remarkably similar to the brute force solution.
On each iteration of the algorithm, we generate a random integer between the
current index and the last index of the array. Then, we swap the elements at
the current index and the chosen index - this simulates drawing (and
removing) the element from the hat, as the next range from which we select a
random index will not include the most recently processed one. One small, yet important
detail is that it is possible to swap an element with itself - otherwise, some
array permutations would be more likely than others. To see this illustrated more
clearly, consider the animation below:

!?!../Documents/384_Shuffle_an_Array.json:697,161!?!

<iframe src="https://leetcode.com/playground/ftmztsv8/shared" frameBorder="0" width="100%" height="500" name="ftmztsv8"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$

    The Fisher-Yates algorithm runs in linear time, as generating a random
    index and swapping two values can be done in constant time.

* Space complexity : $$O(n)$$

    Although we managed to avoid using linear space on the auxiliary array
    from the brute force approach, we still need it for `reset`, so we're
    stuck with linear space complexity.

---

Analysis written by: [@emptyset](https://leetcode.com/emptyset)
