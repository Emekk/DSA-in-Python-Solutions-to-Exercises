import typing
import random  # for R-1.12


# R-1.1
def is_multiple(n: int, m: int) -> bool:
    return n % m == 0

# R-1.2 TODO: seek a better way
def is_even(k: int) -> bool:
    evens = ('0', '2', '4', '6', '8')
    last_digit = str(k)[-1]
    return last_digit in evens

# R-1.3
def minmax(data: typing.Iterable[int]) -> typing.Tuple[int]:
    smallest, largest = data[0], data[0]
    for num in data:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

# R-1.4
def sum_squares_range(n: int) -> int:
    return sum(elem**2 for elem in range(1, n))

# R-1.5
# refer to R-1.4

# R-1.6
def sum_odd_squares_range(n: int) -> int:
    return sum(elem**2 for elem in range(1, n, 2))

# R-1.7
# refer to R-1.6

# R-1.8
# Answer: j = k + n

# R-1.9
# Answer: start=50, stop=81, step=10

# R-1.10
# Answer: start=8, stop=-9, step=-2

# R-1.11
[2**e for e in range(9)]

# R-1.12
def my_choice(data: typing.Iterable) -> typing.Any:
    index = random.randrange(0, len(data))
    return data[index]
