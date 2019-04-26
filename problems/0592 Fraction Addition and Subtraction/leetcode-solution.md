# 0592 - Fraction Addition and Subtraction

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math | [Leetcode](https://leetcode.com/problems/fraction-addition-and-subtraction) | [solution](https://leetcode.com/problems/fraction-addition-and-subtraction/solution/)


-----------

<p>Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be <a href = "https://en.wikipedia.org/wiki/Irreducible_fraction">irreducible fraction</a>. If your final result is an integer, say <code>2</code>, you need to change it to the format of fraction that has denominator <code>1</code>. So in this case, <code>2</code> should be converted to <code>2/1</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>"-1/2+1/2"
<b>Output:</b> "0/1"
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>"-1/2+1/2+1/3"
<b>Output:</b> "1/3"
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b>"1/3-1/2"
<b>Output:</b> "-1/6"
</pre>
</p>

<p><b>Example 4:</b><br />
<pre>
<b>Input:</b>"5/3+1/3"
<b>Output:</b> "2/1"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input string only contains <code>'0'</code> to <code>'9'</code>, <code>'/'</code>, <code>'+'</code> and <code>'-'</code>. So does the output.</li>
<li>Each fraction (input and output) has format <code>±numerator/denominator</code>. If the first input fraction or the output is positive, then <code>'+'</code> will be omitted.</li>
<li>The input only contains valid <b>irreducible fractions</b>, where the <b>numerator</b> and <b>denominator</b> of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.</li> 
<li>The number of given fractions will be in the range [1,10].</li>
<li>The numerator and denominator of the <b>final result</b> are guaranteed to be valid and in the range of 32-bit int.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Solve the Equation](solve-the-equation)




## Solution:

[TOC]


## Solution

---
#### Approach #1  Using LCM[Accepted]

The first obvious step to be undertaken is to split the given string into individual fractions. We split the string based on `+` and `-` sign. We store the signs in the order in which they appear in the string in $$sign$$ array. Further, after getting the individual fractions, we further split the fractions based on `/` sign. Thus, we obtain the individual numerator and denominator parts. We store the same in $$num$$ and $$den$$ arrays respectively.

Now, we've got the data ready to be worked upon. In order to see the method we've used in this implementation, we'll take an example and understand the way we work on it.

Let's say, the given fraction is:

$$\frac{3}{2} + \frac{5}{3} -\frac{7}{6}$$

We need to equalize all the denominators so as to be able to add and subtract the numerators easily. The nearest value the denominators can be scaled upto is the LCM of all the denominators. Thus, we need to find the LCM of all the denominators and then multiply all the denominators with appropriate integer factors to make them equal to the LCM. But, in order to keep the individual fraction values unchanged, we need to multiply the individual numerators also with the same factors. 

In order to find the LCM, we can go as follows. We use the method $$lcm(a,b,c) = lcm( lcm(a,b), c)$$. Thus, if we can compute the lcm of two denominators, we can keep on repeating the process iteratively over the denominators to get the overall lcm. To find the lcm of two numbers $$a$$ and $$b$$, we use $$lcm(a,b) = (a*b)/gcd(a,b)$$. For the above example, the $$lcm$$ turns out to be 6.

Thus, we scale up the denominators to 6 as follows:

$$\frac{3*3}{2*3} + \frac{5*2}{3*2} -\frac{7}{6}$$

Thus, we can observe that, the scaling factor for a fraction $$\frac{num}{den}$$ is given by: $${num*x}/{den*x}$$, where $$x$$ is the corresponding scaling factor. Note that, $$den*x=lcm$$. Thus, $$x=lcm/den$$. Thus, we find out the corresponding scaling factor $$x_i$$ for each fraction.

After this, we can directly add or subtract the new scaled numerators.

In the current example, we obtain $$\frac{12}{6}$$ as the result. Now, we need to convert this into an irreducible fraction. Thus, if we obtain $$\frac{num_i}{den_i}$$ as the final result, we need to find a largest factor $$y$$, which divides both $$num_i$$ and $$den_i$$. Such a number, as we know, is the gcd of $$num_i$$ and $$den_i$$.

Thus, to convert the result $$\frac{num_i}{den_i}$$, we divide both the numerator and denominator by the gcd of the two numbers $$y$$ to obtain the final irreducible $$\frac{num_i/y}{den_i/y}$$.

Note: A problem with this approach is that we find the lcm of all the denominators in a single go and then reduce the overall fraction at the end. Thus, the lcm value could become very large and could lead to an overflow. But, this solution suffices for the current range of numbers.

<iframe src="https://leetcode.com/playground/8oKguDZy/shared" frameBorder="0" name="8oKguDZy" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(nlogx)$$. Euclidean GCD algorithm takes $$O(log(a.b))$$ time for finding gcd of two numbers $$a$$ and $$b$$. Here $$n$$ refers to the number of fractions in the input string and $$x$$ is the maximum possible value of denominator.

* Space complexity : $$O(n)$$. Size of $$num$$, $$den$$ and $$sign$$ list grows upto $$n$$.

---
#### Approach #2  Using GCD[Accepted]

**Algorithm**

We know that we can continue the process of evaluating the given fractions by considering pairs of fractions at a time and continue the process considering the result obtained and the new fraction to be evaluated this time. We make use of this observation, and thus, instead of segregating the signs, numerators and denominators first, we directly start scanning the given strings and operate on the fractions obtained till now whenever a new sign is encountered.

We operate on the pairs of fractions, and keep on reducing the result obtained to irreducible fractions on the way. By doing this, we can reduce the chances of the problem of potential overflow possible in case the denominators lead to a large value of lcm.

We also observed from the last approach, that we need to equalize the denominators of a pair of fractions say:

$$\frac{a}{b} + \frac{c}{d}$$

We used a scaling factor of $$x$$ for the first fraction(both numerator and denominator). Here, $$x=lcm(b,d)/b$$. For the second fraction, the scaling factor $$y$$ is given by $$y=lcm(b,d)/d$$. Here, $$$lcm(b,d)=b*d/gcd(b,d)$$. Thus, instead of finding the lcm and then again determining the scaling factor, we can directly use: $$x=(b*d)/(gcd(b,d)*b) = d/gcd(b,d)$$, and $$y=(b*d)/(gcd(b,d)*d)$$. Thus, we need to scale the numerators appropriately and add/subtract them in terms of pairs. The denominators are scaled in the same manner to the lcm of the two denominators involved.

After evaluting every pair of fractions, we again reduce them to irreducible fractions by diving both the numerator and denominator of the resultant fraction by the gcd of the two.


<iframe src="https://leetcode.com/playground/Nt5WV8C2/shared" frameBorder="0" name="Nt5WV8C2" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(nlogx)$$. Euclidean GCD algorithm takes $$O(log(a.b))$$ time for finding gcd of two numbers $$a$$ and $$b$$. Here $$n$$ refers to the number of fractions in the input string and $$x$$ is the maximum possible value of denominator.

* Space complexity : $$O(n)$$. Size of $$sign$$ list grows upto $$n$$.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
