## Data Structure and Algorithm 1 | Algorithm Analysis Theory

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

### 0. Environment Installation

- Download the jar file [`algs4.jar`](https://algs4.cs.princeton.edu/code/algs4.jar) to root directory

```bash
$ sudo curl -O "https://algs4.cs.princeton.edu/code/algs4.jar"
```

- Install the command line tools

```bash
$ sudo curl -O "https://algs4.cs.princeton.edu/linux/{javac,java}-{algs4,cos226,coursera}"
$ sudo chmod 755 {javac,java}-{algs4,cos226,coursera}
$ sudo mv {javac,java}-{algs4,cos226,coursera} /usr/local/bin
```

- [Download](https://www.jetbrains.com/idea/download/#section=mac) and install the latest version IntelliJ IDEA community version

### 1. Basic Concepts

> As soon as an Analytic Engine exists, it will necessarily guide the future course of the science. Whenever any result is sought by its aid, the question will arise — By what course of calculation can these results be arrived at by the machine in the shortest time?
>
> *— Charles Babbage (1864)*

In Java, we can time the running time of an algorithm by `Stopwatch` class, which is a part of the `stdlib.jar`. We should use `Stopwatch()` for creating a new stopwatch and then call `elapsedTime()` to get the time in seconds since the `Stopwatch` is created.

```java
public class Stopwatch {
    private final long start;
    public Stopwatch() {
        start = System.currentTimeMillis();
    }
    public double elapsedTime() {
        long now = System.currentTimeMillis();
        return (now - start) / 1000.0;
    }
}
```

#### (1) Scientific Method

In the 1970s, Donald Knuth introduces the scientific method for understanding computing performance. Nowadays, the scientific method is explained in the following steps,

- Observe some features of the natural world.
- Hypothesize a model that is consistent with the observations.
- Predict events using the hypothesis.
- Verify the predictions by making further observations.
- Validate by repeating until the hypothesis and observations agree

There are two principles for the scientific method,

- Experiments must be reproducible
- Hypotheses must be falsifiable

### 2. Examples of Successful Algorithms

#### **(1) Discrete Fourier Transform (DFT) Problem**

Break down waveform of N samples into periodic components. The applications are on DVDs, JPEG files, MRI, astrophysics, etc.

- Brute Force: N² steps
- Fast Fourier Transform: NlogN steps (called linearithmic)

#### **(2) N-Body Simulation Problem**

Simulate gravitational interactions among *N* bodies.

- Brute Force: N² steps
- Barnes-Hut algorithm: NlogN steps

#### **(3) Three Sum Problem**

Given N distinct integers, how many triples sum to exactly zero?

For example,

```
1 2 -1 0 -2
```

The answer should be,

```
2
1 + -1 + 0 = 0
2 + -2 + 0 = 0
```

- Brute Force: Grid-search (n³ complexity)

```java
for (int i = 0; i < n; i++) 
    for (int j = i + 1; j < n; j++) 
        for (int k = j + 1; k < n; k++) 
            if (a[i] + a[j] + a[k] == 0) 
               count++;
```

The Grid-search program should be,

```java
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class ThreeSum {

    private ThreeSum() {
    }

    public static int count(int[] a) {
        int n = a.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (a[i] + a[j] + a[k] == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        int[] a = in.readAllInts();

        Stopwatch timer = new Stopwatch();
        int count = count(a);
        StdOut.println("elapsed time = " + timer.elapsedTime());
        StdOut.println(count);
    }
}
```

We can download the testing files of [`1Kint.txt`](https://raw.githubusercontent.com/aistrate/AlgorithmsSedgewick/master/1-Fundamentals/1-4-AnalysisOfAlgorithms/1Kints.txt), [`2Kint.txt`](https://raw.githubusercontent.com/aistrate/AlgorithmsSedgewick/master/1-Fundamentals/1-4-AnalysisOfAlgorithms/2Kints.txt) , [`4Kint.txt`](https://raw.githubusercontent.com/aistrate/AlgorithmsSedgewick/master/1-Fundamentals/1-4-AnalysisOfAlgorithms/4Kints.txt) , and [`8Kint.txt`](https://raw.githubusercontent.com/aistrate/AlgorithmsSedgewick/master/1-Fundamentals/1-4-AnalysisOfAlgorithms/8Kints.txt) (`nKint` means we have n thousand integers in that file) from these links. And then we are able to test these files by,

```bash
$ java-algs4 ThreeSum 1Kints.txt
$ java-algs4 ThreeSum 2Kints.txt
$ java-algs4 ThreeSum 4Kints.txt
$ java-algs4 ThreeSum 8Kints.txt
```

The results are, 

```
Name                Time                Result         
1Kints.txt          0.296               70
2Kints.txt          2.679               528
4Kints.txt          22.225              4039
8Kints.txt          170.302             32074
```

If we plot this result with the standard plot and the log-log plot, we will have the following relationships,

![img](https://miro.medium.com/max/700/1*ZLf46oMS58_11-rSuRGOmw.png)

This is because we have,

```
T(N) = a * N^b
```

So,

```
log(T(N)) = blog(N) + c
```

where,

```
a = exp(c)
```

Because we have a slope in this plot of about 3, then we can say,

```
b = 3
```

And the order of growth of the running time is about,

```
N^3
```

- Quick ThreeSum: Applying the binary search algorithm as the last loop. We will leave the discussion of `binarySearch` later in this series.

```java
for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
        int k = Arrays.binarySearch(a, -(a[i] + a[j]));
        if (k > j) cnt++;
    }
}
```

```java
import java.util.Arrays;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.In;

public class ThreeSumFast {

    public static int count(int[] a) {
        int N = a.length;
        Arrays.sort(a);
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int k = Arrays.binarySearch(a, -(a[i] + a[j]));
                if (k > j) cnt++;
            }
        }
        return cnt;
    }

    public static void main(String[] args)  {
        In in = new In(args[0]);
        int[] a = in.readAllInts();

        Stopwatch timer = new Stopwatch();
        int count = count(a);
        StdOut.println("elapsed time = " + timer.elapsedTime());
        StdOut.println(count);
    }
}
```

Again, we can simulate the time by,

```bash
$ java-algs4 ThreeSumFast 1Kints.txt
$ java-algs4 ThreeSumFast 2Kints.txt
$ java-algs4 ThreeSumFast 4Kints.txt
$ java-algs4 ThreeSumFast 8Kints.txt
```

The results are,

```
Name                Time                Result         
1Kints.txt          0.019               70
2Kints.txt          0.090               528
4Kints.txt          0.257               4039
8Kints.txt          1.504               32074
```

Here, we can spot a big improvement in the time complexity.

### **3. Algorithm Theory**

#### (1) **The Definition of Algorithm Analysis**

The algorithm analysis theory is invented in the book *The Art Of Computer Programming* by Donald Knuth. It explains the mathematical models for calculating the total running time of a computer program, which should physically be the sum of cost times frequency for all operations.

- Cost depends on machine and compiler
- Frequency depends on algorithm and input data

#### (2) **Cost of Basic Operations**

![img](https://miro.medium.com/max/700/1*DsFRoNNKCvGEE8JMNHkbrQ.png)

#### **(3) Brute-Force TwoSum Cost Example**

Now, let’s analyze the cost of a `TwoSum` program. In this program, we have,

```java
int count = 0; 
for (int i = 0; i < N; i++) 
    for (int j = i+1; j < N; j++) 
        if (a[i] + a[j] == 0) 
           count++;
```

Then, the frequency for each operation should be,

```
// 1 time int count; 1 time int i; N times int j;
variable declaration                                    N + 2

// 1 time count = 0; 1 time i = 0; N times j = i + 1;
assignment statement                                    N + 2

// N+1 times i < N; N(N+1)/2 times j < N
less than compare                N+1 + N(N+1)/2 =    (N+1)(N+2)/2

// (N-1) + ... + 2 + 1 + 0 times x == 0;
equal to compare                                       N(N-1)/2

// N(N-1)/2 times a[i]; N(N-1)/2 times a[j];
array access                                            N(N-1)

// at worst: N(N-1)/2 times count++; N(N-1)/2 times a[i] + a[j];
// at best: no count++; N(N-1)/2 times a[i] + a[j];
// ignore i++ and j++;
increment                                         N(N-1)/2 to N(N-1)
```

The cost model is to use some basic operations as a proxy for running time and here we can simply choose array access with the cost model `N(N-1)`.

#### **(4) Tilde Notation**

The tilde notation `~` is used when we are able to ignore lower order terms, so technically,
$$
f(N) \sim g(N)
$$
When,
$$
\lim _{N \rightarrow \infty} \frac{f(N)}{g(N)}=1
$$
Then, for the Brute-Force TwoSum problem, the can be cost model with N inputs can be simplified to N².

```
N(N-1) ~ N²
```

#### (5) **Big-Oh Notation**

The most commonly used notation in algorithm analysis is the big-oh notation O. It also has two friends, big-theta Θ and big-omega Ω.

- Big-Theta: Θ(*f*(N)) is a notation that stands for a polynomial with the highest order term ~ *f*(N). For example,

```
N² + 2N + 1  ~  Θ(N²)
```

- Big-Oh (upper bound): O(*f*(N)) is a notation that stands for a polynomial with the highest order term ~ *f*(N) or smaller. For example,

```
N² + 2N + 1  ~  O(N²)
2N + 1       ~  O(N²)
```

- Big-Omega (lower bound): Ω(*f*(N)) is a notation that stands for a polynomial with the highest order term ~ *f*(N) or larger. For example,

```
N² + 2N + 1  ~  Ω(N²)
N³ + 2N + 1  ~  Ω(N²)
```

#### **(6) Common Order of Growth Classifications**

![img](https://miro.medium.com/max/700/1*L3Ky0YFDzGmJ56aG4wFGlw.png)

#### **(7) Problem Sizes Per Minute for Different Order of Growth in the 2000s**

```
growth-rate                       Problem Size
1                                          any
logN                                       any
N                                1,000,000,000
NlogN                              100,000,000
N²                                      10,000
N²logN                                  10,000
N³                                       1,000
2^N                                         30
```

#### **(8) Memory Cost for Common Data Type**

```
boolean                 1
byte                    1
char                    2
int                     4
float                   4
long                    8
double                  8
char[]            2N + 24
int[]             4N + 24
double[]          8N + 24
char[][]          ~ 2 M N
int[][]           ~ 4 M N
double[][]        ~ 8 M N
```