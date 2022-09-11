#* Numbers in Nature

Fibonacci Numbers are always found in spirals, such as in counter-clockwise or clockwirse sunflower head pattern. The pair of number of spirals forms two consecutive (two numbers that follow each other in a particular sequence) numbers {21: 34, 55: 89, 89: 144} of the Fibonacci sequence.

However, the pattern is not true for all sunflowers as Swinton et al. (2016) found out that one in five flowers did not conform to Fibonacci sequence.

# Fibonacci Number

Leonardo Bigollo Pisano, also known as Fibonacci, created a problem that concerns the birth rate of rabbits.

> At the beginning o a month, you are given a pair of newborn rabbits. After a month the rabbits have produced no offspring; however every month thereafter, the pair of rabbits produces another pair of rabbits. The offspring reproduce in exactly the same manner. If none of the rabbit dies, how many pairs of rabbits will there be at the start of each succeeding month?

The solution to the previous problem created by Fibonacci is a sequence of numbers called Fibonacci sequence. He then discovered that the number of pairs of rabbits for any month after the first two months can be determined by adding the numbers of pairs of rabbits in each of the two previous months.

# Fibonacci Numbers and the Golder Ratio

Golden Ratio, also known as Divine Proportion exists when a line is divided into two parts and the ratio of the longer part, $a$, to shorter part, $b$, is equal to the ratio of the sum $a+b$ to $a$:

The value of Golden Ratio is given by the irrational number (cannot be expressed by ratio of two whole numbers), $\Phi = 1.6180339887$, that can be derived as:

$$
\frac{a}{b} = \frac{a + b}{a} = \Phi --
\text{$\Phi = \frac{a}{b}$ and $\Phi = \frac{a+b}{a}$} --
\text{From $\Phi = \frac{a}{b}$, we get $\frac{1}{\Phi} = \frac{b}{a}$} --
\text{Using $\Phi \frac{a+b}{a}$} --
\Phi = \frac{a}{a} + \frac{b}{a} --
= 1 + \frac{b}{a} --
= 1 + \frac{1}{\Phi} --
\Phi^{2} = \Phi + 1 --
\Phi^{2} - \Phi -1 = 0 --
\text{Solving the quadratic equation:} --
\Phi = \frac{1 + \sqrt{5}}{2} = 1.6180339887...
$$

Any two successive numbers in Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, ...) have a very close ratio to the golden ratio:

$$--
\frac{5}{3} = 1.6667
\frac{8}{5} = 1.6000
\frac{13}{8} = 1.6250
\frac{21}{13} = 1.6154
$$

Fibonacci spiral is also a good approximation of spirals that are present in nature such as nautilus shell, hurricanes and the human ear.

# The number e

$e \approx 2.718281828459045$, the irrational number $e$ is often referred to as Euler's number after Swiss mathematician Leonhard Euler who introduced the constant. It is also referred to as Napier's constant after John Napier who introduced it earlier in a table of appendix for his work on logarithms. But its discovery is attributed to Jacod Bernoulli when he tried to solve a problem related to continuous compound interests.

##* Compound Interest

Interest is a paymend charged for borrowing a money or an income for keeping a money in a bank or making an investment.

Simple interest is interest paid on the principal only. For example, a loan of $1000 PHP$ at $5%$ annual interest rate for 2 years will have payment of $50 PHP/year$ for two years. The amount of interest will not change as long as no additional money is borrowed.

Compound interest is the addition of interest to the original principal (interst earned also earns interest). Interest compounded continuously grows exponentially. Thus if compounding is continuous, the accumulated balance at the end of comopounding period is given by:

$$
A = Pe^{rt}
$$

Where $A$ is the accumulated balance ater a time, $t$, $P$ is the principal amount, $r$ is the interest rate in decimal, $t$, time in years, $e \approx 2.718281828459045$.

In any cases, where $t$ is the variable missing, the equation can be solved by taking the natural logarithm of both sides, since $ln x = y = e^y$, then:

$$
A = Pe^{rt}
\frac{A}{P} = e^{rt} --
ln(\frac{A}{P}) = rt --
t = \frac{ln(\frac{A}{P})}{r}
$$

And for $r$, it becomes:

$$
r = \frac{ln(\frac{A}{P})}{t}
$$

##* Population  Growth

Mathematics also a play a vital role in modeling the growth of population, specifically, the exponential and logarithmic funcctions are applied to describe the relationship between time and population size.

###* Malthusian Growth Model

Also known as exponential growth model named ater Thomas Robert Malthus. Applied in obtaining population growth o bacteria and even humans on the asumption that resources are unlimited and the population has a continuous birth rate throughout time:

$$
P(t) = P_{0} e^{rt}
$$

Where, $P(t)$ is the population after time, $t$. $P_{0}$ is the initial population, $r$ is the population growth rate in decimals, and $t$, time.

###* Logistic Growth Model

Proposed by Pierre in 1836. Alternate model that considers the constraints in population growth.

$$P(t) = \frac{K}{1 + Ae^{-kt}}$$

Where $P(t)$ is the population after time, $t$. $K$ is the constraint or the limiting value, $k$ is the relative growth rate coefficient, $P_{0}$ is the initial population at $t = 0$, and $A = \frac{K - P_{0}}{P_{0}}$. Then, $P(t)$ is:

$$P(t) = \frac{K}{1 + \big(\frac{K - P_{0}}{P_{0}}\big)e^{-kt}}$$

In missing $t$, $t$ can be isolated by:

$$
P(t) = \frac{K}{1 + \Big(\frac{K - P_{0}}{P_{0}}\Big)e^{-kt}} --
K = P(t) \cdot 1 + \Big(\frac{K - P_{0}}{P_{0}}\Big)e^{-kt} --
\frac{K}{P(t)} = 1 + \Big(\frac{K - P_{0}}{P_{0}}\Big)e^{-kt} --
$$

Then subtracting $1$ to the other side of the equation:

$$\Big(\frac{K - P_{0}}{P_{0}}\Big)e^{-kt} = \frac{K}{P(t)} - 1$$

Let $\frac{K - P_{0}}{P_0} = A$:

$$
e^{-kt} = \frac{\frac{K}{P(t)} - 1}{\big(\frac{K - P_{0}}{P_{0}}\big)} \longrightarrow \frac{\frac{K}{P(t)} - 1}{A} \\
= \frac{\frac{K - P(t)}{P(t)}}{A}
$$

Simplifying, $\frac{K}{P(t)} -1 = \frac{K - P(t)}{P(t)}$:

$$
e^{-kt} = \frac{K - P(t)}{P(t) \cdot A}
$$

And taking the natural logarithm of both sides, since: $ln_{e} X = Y \longrightarrow e^{y} = X$

$$
ln(e^{-kt}) = ln\big(\frac{K - P(t)}{P(t) \cdot A}\big) --
-kt = ln\big(\frac{K - P(t)}{P(t) \cdot A}\big)
$$

Then with the equation, we can easily find $t$:

$$\boldsymbol{t} = \boldsymbol{ln\big(\frac{K - P(t)}{P(t) \cdot A}\big) \cdot \frac{1}{|-k|}}$$

And $k$:

$$\boldsymbol{-k} = \boldsymbol{ln\big(\frac{K - P(t)}{P(t) \cdot A}\big) \cdot \frac{1}{t}}$$

###* Exponential Decay

If the quantity decreases continuously at a rate, $r$, where $r > 0$, then we have an exponential decay and it is modeled by the function:

$$P(t) = P_{0} e^{-rt}$$

Where $P(t)$ is the quantity at any time, $t$. $P_{0}$ is the initial quantity, $r$ is the rate of decay in decimals, and $t$ is time.

And time, $t$, again is:

$$
e^{-rt} = \frac{P(t)}{P_{0}} --
-rt = ln\big(\frac{P(t)}{P_{0}}\big) --
$$

Then we can find $t$ as:

$$t = ln\big(\big[\frac{P(t)}{P_{0}}\big]\big) \frac{1}{|-r|}$$

And $r$ as:

$$-r = ln\big(\big[\frac{P(t)}{P_{0}}\big]\big) \frac{1}{t}$$
