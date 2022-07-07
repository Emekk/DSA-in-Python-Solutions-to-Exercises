import typing
import random  # for C-1.20
import sys  # for C-1.21


# C-1.13
# Pseudocode:
# function reverse(list, n):
#     i = 0
#     while i < floor(n / 2)
#         temp =  list[i]
#         list[i] = list[n - i - 1]
#         list[n - i - 1] = temp
#         i = i + 1
#     return list
def reverse(data: typing.List[int]) -> typing.List[int]:
    n = len(data)
    i = 0
    while i < n // 2:
        data[i], data[n-i-1] = data[n-i-1], data[i]
        i += 1
    return data
# or, a pythonic alternative
def reverse(data: typing.List[int]) -> typing.List[int]:
    return data[::-1]

# C-1.14
def has_odd_prod_pair(data: typing.Iterable[int]) -> bool:
    for left_num in data:
        if left_num % 2 == 0:
            continue
        for right_num in data:
            if right_num % 2 == 0 or left_num == right_num:
                continue
            return True;
    return False

# C-1.15
def is_distinct(data: typing.Iterable[int]) -> bool:
    return len(set(data)) == len(data)

# C-1.16
# Answer: the expression "data[j] *= factor" is, under the hood, equivalent to "data[j] = data[j] * factor".
#   In other words, it assigns the scaled number to "data[j]", not mutates it.

# C-1.17
# It doesn't work properly. Because 'val' is a copy of the current element of 'data', and the changes made on 
#   it wouldn't affect the original list.

# C-1.18
[i * (i+1) for i in range(0, 10)]

# C-1.19
[chr(i) for i in range(97, 123)]

# C-1.20
def my_shuffle(data: typing.List) -> typing.List:
    shuffled = []
    while data:
        index = random.randint(0, len(data) - 1)
        shuffled.append(data.pop(index))
    return shuffled

# C-1.21
def read_reverse() -> None:
    lines = []
    for line in sys.stdin:
        if 'ctrl-D' == line.rstrip():
            break
        lines.append(line.rstrip())
    print(*lines[::-1], sep="\n")

# C-1.22
def dot_product(a: typing.List[int], b: typing.List[int]) -> typing.List[int]:
    c = [ea * eb for ea, eb in zip(a, b)]
    return c

# C-1.23
def write_list(data: typing.List, elem: typing.Any, index: int) -> None:
    try:
        data[index] = elem
    except Exception as e:
        print("Don't try buffer overflow attacks in Python!")

# C-1.24
def count_vowel(string: str) -> int:
    vowels = "aeoui"
    return sum(char in vowels for char in string)

# C-1.25
def remove_punc(s: str) -> str:
    result = ""
    for char in s:
        if char.isalnum() or char.isspace():
            result += char
    return result

# C-1.26
def valid_formula(a: int, b: int, c: int) -> bool:
    return (a + b == c) or (a - b == c) or (a * b == c) or (a / b == c) or (a == b + c) or (a == b - c) or\
        (a == b * c) or (a == b / c)

# C-1.27
def factors(n: int) -> typing.Iterator[int]:
    k = 1
    bigger = []
    while k * k < n:
        if n % k == 0:
            yield k
            bigger.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for b in bigger[::-1]:
        yield b

# C-1.28
def norm(v: typing.List[int], p: int = 2) -> int:
    return sum(elem**p for elem in v)**(1/p)


if __name__ == "__main__":
    llist = [5, 12]
    x = norm(llist)
    print(x)