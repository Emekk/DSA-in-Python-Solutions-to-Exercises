import typing
import matplotlib.pyplot as plt
import numpy as np


# R-3.1
x = np.linspace(start=1, stop=5, num=100)**2
y1 = 8 * x
y2 = 4 * x * np.log2(x)
y3 = 2 * x**2
y4 = x**3
y5 = 2**x
plt.loglog(x, y1, label="8n", base=2)
plt.loglog(x, y2, label="4nlog(n)", base=2)
plt.loglog(x, y3, label="2n^2", base=2)
plt.loglog(x, y4, label="n^3", base=2)
plt.loglog(x, y5, label="2^n", base=2)
plt.legend()
plt.tight_layout()
#plt.show()

# R-3.2
# Answer: n0 = 16

# R-3.3
# Answer: n0 = 20

# R-3.4
# Answer: f(x) = x

# R-3.5
# Answer: The log-log scale corresponds to X = log(x) and Y = log(y) conversions. To do that:
#          - take log of both sides -> log(y) = clog(x)
#          - apply conversions -> Y = cX (a straight line with slope c)

# R-3.6
# Answer: = 2 + 4 + ... 2n-2 + 2n
#         = 2*(1 + 2 + ... n-1 + n)
#         = 2 * n(n+1)/2 => n(n+1)

# R-3.7
# Answer: 'Big-Oh' notation is for worst case, thus the statements are equivalent. 

# R-3.8
# Answer: 2^10 < 3n + 100logn < 4n < nlogn < 4nlogn + 2n < n^2 + 10n < n^3 < 2^logn < 2^n

# R-3.9
# Answer: if d(n) <= cf(n) for n > n0, by multiplying each side with 'a', a positive number:
#         we get -> ad(n) <= acf(n) for n > n0. Since 'c' represents an arbitrary constant,
#         it is possible to write -> ad(n) <= cf(n) for n > n0. 

# R-3.10
# Answer: if d(n) <= c1f(n) and e(n) <= c2g(n) for n > n0, then d(n)e(n) <= c1c2f(n)g(n)
#         As in R-3.9, it is possible to write (c1c2 as c) ->  d(n)e(n) <= cf(n)g(n)

# R-3.11
# Answer: if d(n) <= c1f(n) and e(n) <= c2g(n) for n > n0, then d(n) + e(n) <= c1f(n) + c2g(n). As constants 
#         are arbitrary, given c > c1 and c > c2, it is possible to write->  d(n) + e(n) <= c(f(n) + g(n))

# R-3.12
# Answer: Let's assume f(n) = g(n) = n; d(n) = 3n; e(n) = 2n
#         Since 3n - 2n = n is not O(n - n) = O(0), the statement is not necessarily true.

# R-3.13
# Answer: if d(n) <= c1f(n) and f(n) <= c2g(n) for n > n0, then d(n) <= c1c2g(n).
#         As in R-3.9, it is possible to write -> d(n) <= cg(n).

# R-3.14
# Answer: Since 'Big-Oh' only take the highest order item into account, O(f(n) + g(n)) = O(max{f(n), g(n)})

# R-3.15
# Answer: For "f(n) <= cg(n)" to be true, "g(n) >= cf(n)" must be true.

# R-3.16
# Answer: since log(n^c) = clogn, log(p(n)) is O(log(n))

# R-3.17
# Answer: highest order element in (n + 1)^5 is n^5; thus, it is O(n^5).

# R-3.18
# Answer: 2^(n+1) = 2*2^n; coefficient '2' can be omitted.

# R-3.19
# Answer: n <= nlog(n) for all n >= 2.

# R-3.20
# Answer: n^2 >= nlogn for all n >= 1.

# R-3.2
# Answer: nlogn >= n for all n >= 2.

# R-3.22
# Answer: ceil(f(n)) <= f(n) + 1 <= 2f(n)

# R-3.23
# Answer: 

# R-3.24


# R-3.25


# R-3.26


# R-3.27


# R-3.28


# R-3.29


# R-3.30


# R-3.31


# R-3.32


# R-3.33


# R-3.34


if __name__ == "__main__":
    deb = None
    print(deb)