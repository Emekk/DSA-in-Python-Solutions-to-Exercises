import typing


# R-2.1
# Answer: health, transportation, military

# R-2.2
# Answer: banking software

# R-2.3
# Answer: the find/search feature, encapsulating the methods find, next, replace. 

# R-2.4
class Flower:
    def __init__(self, name: str, npetal: int, price: float) -> None:
        self._name = name
        self._npetal = npetal
        self._price = price

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_npetal(self) -> int:
        return self._npetal

    def set_npetal(self, npetal: int) -> None:
        self._npetal = npetal

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
        self._price = price

# R-2.5
def charge(self, price: typing.Union[int, float]) -> None:
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number!")
    if price + self._balance > self. limit:
        return False
    else:
        self._balance += price
        return True

def make_payment(self, amount: typing.Union[int, float]) -> None:
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number!")
    self._balance -= amount

# R-2.6
def make_payment(self, amount: typing.Union[int, float]) -> None:
    if amount < 0:
        raise ValueError("Amount must be a nonnegative number!")
    self._balance -= amount

# R-2.7
def __init__(self, customer, bank, acnt, limit, balance=0):  # optional parameter balance
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = balance  # "= balance" instead of "= 0"

# R-2.8
for val in range(1, 59):  # 'stop' of the range is 59 instead of 17
    wallet[0].charge(val) 
    wallet[1].charge(2*val) 
    wallet[2].charge(3*val)  # is the one that goes over its credit limit

# R-2.9
def __sub__(self, other):
    result = Vector(len(self))
    for j in range(len(result)):
        result[j] = self[j] - other[j]
    return result

# R-2.10
def __neg__(self):
    result = Vector(len(self))
    for j in range(len(result)):
        result[j] = -self[j]
    return result

# R-2.11
# Answer: by defining the method __radd__ of the Vector class.

# R-2.12
def __mul__(self, factor):
    result = Vector(len(self))
    for j in range(len(result)):
        result[j] = factor * self[j]
    return result

# R-2.13
def __rmul__(self, factor):
    result = Vector(len(self))
    for j in range(len(result)):
        result[j] = factor * self[j]
    return result

# R-2.14
def __mul__(self, other):
    result = Vector(len(self))
    for j in range(len(result)):
        result[j] = self[j] * other[j]
    return result

# R-2.15
def __init__ (self, d):
    if isinstance(d, int):
        self._coords = [0] * d
    elif isinstance(d, (tuple, list)):
        self._coords = [elem for elem in d]

# R-2.16
# Answer: The inclusive range is [start, stop - 1]. To calculate the number of elements in the range,
#         substract 'start' from 'stop - 1'; add 'step' and divide the sum by 'step'. If the result
#         is negative, 0 is choosed thanks to the expression 'max(0, ...)'.  

# R-2.17
# see "R-2.17.png"

# R-2.18
FibonacciProgression(2, 2).print_progression(8)

# R-2.19
# Answer: 2^56 + 1 calls

# R-2.20
# Answer: dynamic dispatching would take a lot of time.

# R-2.21
# Answer: it reduces the reusability of the code as any change to class Z will also change the subclasses.

# R-2.22
def __eq__(self, other):
    if len(self) != len(other):
        return False
    for j in range(len(self)):
        if self[j] != other[j]:
            return False
    return True

# R-2.23
def __lt__(self, other):
    n = min(len(self), len(other))
    for j in range(n):
        if self[j] < other[j]:
            return True
        elif self[j] > other[j]:
            return False
    return len(self) < len(other)
